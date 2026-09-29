from __future__ import annotations

import ast
from pathlib import Path
from typing import Mapping

import numpy as np
import pandas as pd


LEAD_ORDER = ["I", "II", "III", "AVR", "AVL", "AVF", "V1", "V2", "V3", "V4", "V5", "V6"]
EXPECTED_FS = 100
EXPECTED_SAMPLES = 1000
EXPECTED_CHANNELS = 12


def parse_scp_codes(value: str | Mapping[str, float]) -> dict[str, float]:
    """Parse a PTB-XL SCP-code mapping into a code-to-likelihood dictionary."""
    if isinstance(value, Mapping):
        return {str(k): float(v) for k, v in value.items()}
    parsed = ast.literal_eval(value)
    if not isinstance(parsed, dict):
        raise ValueError("scp_codes must decode to a dictionary")
    return {str(k): float(v) for k, v in parsed.items()}


def load_diagnostic_class_map(scp_statements_path: str | Path) -> dict[str, str]:
    """Load SCP code to PTB-XL diagnostic-superclass mapping."""
    table = pd.read_csv(scp_statements_path, index_col=0)
    diagnostic = table.loc[table["diagnostic"] == 1, "diagnostic_class"]
    return {
        str(code): str(label)
        for code, label in diagnostic.items()
        if pd.notna(label)
    }


def max_class_likelihood(
    scp_codes: Mapping[str, float],
    class_map: Mapping[str, str],
    diagnostic_class: str,
) -> float:
    """Return the maximum likelihood attached to one diagnostic superclass."""
    values = [
        float(likelihood)
        for code, likelihood in scp_codes.items()
        if class_map.get(code) == diagnostic_class
    ]
    return max(values, default=0.0)


def build_binary_labels(
    metadata: pd.DataFrame,
    scp_statements_path: str | Path,
    target_class: str,
    threshold: float = 50.0,
) -> pd.Series:
    """Build the prespecified binary label for one PTB-XL task.

    Returns 1 for target-positive, 0 for NORM-negative, and NaN for exclusions.
    Target plus NORM is retained as target-positive.
    """
    if target_class == "NORM":
        raise ValueError("target_class must be a non-NORM diagnostic superclass")

    class_map = load_diagnostic_class_map(scp_statements_path)

    def label_one(value: str) -> float:
        codes = parse_scp_codes(value)
        target = max_class_likelihood(codes, class_map, target_class) >= threshold
        norm = max_class_likelihood(codes, class_map, "NORM") >= threshold
        if target:
            return 1.0
        if norm:
            return 0.0
        return np.nan

    return metadata["scp_codes"].map(label_one).astype("float64")


def global_record_zscore(signal: np.ndarray) -> np.ndarray:
    """Standardize one ECG using one mean and SD across all leads and samples."""
    x = np.asarray(signal, dtype=np.float32)
    if x.ndim != 2:
        raise ValueError("signal must have shape (channels, time)")
    if not np.isfinite(x).all():
        raise ValueError("signal contains non-finite values")
    mean = float(x.mean())
    std = float(x.std(ddof=0))
    if std == 0.0:
        raise ValueError("global record standard deviation is zero")
    return (x - mean) / std


def per_lead_record_zscore(signal: np.ndarray) -> np.ndarray:
    """Standardize each lead independently using its own record-local mean and SD."""
    x = np.asarray(signal, dtype=np.float32)
    if x.ndim != 2:
        raise ValueError("signal must have shape (channels, time)")
    if not np.isfinite(x).all():
        raise ValueError("signal contains non-finite values")
    mean = x.mean(axis=1, keepdims=True)
    std = x.std(axis=1, keepdims=True, ddof=0)
    if np.any(std == 0.0):
        raise ValueError("at least one lead has zero standard deviation")
    return (x - mean) / std


def validate_records100_array(
    signal: np.ndarray,
    fs: int,
    lead_names: list[str] | None = None,
) -> None:
    """Validate the representation expected by the primary experiment."""
    x = np.asarray(signal)
    if x.shape != (EXPECTED_CHANNELS, EXPECTED_SAMPLES):
        raise ValueError(
            f"expected {(EXPECTED_CHANNELS, EXPECTED_SAMPLES)}, got {x.shape}"
        )
    if int(fs) != EXPECTED_FS:
        raise ValueError(f"expected {EXPECTED_FS} Hz, got {fs}")
    if not np.isfinite(x).all():
        raise ValueError("waveform contains non-finite values")
    if lead_names is not None and list(lead_names) != LEAD_ORDER:
        raise ValueError("unexpected lead order")


def load_records100_wfdb(record_path: str | Path) -> np.ndarray:
    """Load a PTB-XL records100 WFDB record as float32, channels first.

    The wfdb dependency is imported inside the function so metadata-only
    utilities can be tested without loading waveform data.
    """
    try:
        import wfdb
    except ImportError as exc:
        raise ImportError("wfdb is required to load PTB-XL waveform records") from exc

    record = wfdb.rdrecord(str(record_path), physical=True)
    signal = np.asarray(record.p_signal, dtype=np.float32).T
    validate_records100_array(signal, int(record.fs), list(record.sig_name))
    return signal
