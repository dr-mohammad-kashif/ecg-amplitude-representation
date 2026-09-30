from __future__ import annotations

import argparse
from pathlib import Path

import numpy as np
import torch

from src.ecg_pipeline import global_record_zscore, per_lead_record_zscore
from src.model import CompactECGCNN


EXPECTED_VALUES = 12 * 1000


def read_ptbxl_int16(path: Path) -> np.ndarray:
    """Read one records100 binary file using the documented PTB-XL layout."""
    raw = np.fromfile(path, dtype="<i2")
    if raw.size != EXPECTED_VALUES:
        raise ValueError(
            f"expected {EXPECTED_VALUES} int16 values, got {raw.size}"
        )
    return (raw.reshape(1000, 12).T / 1000.0).astype(np.float32)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Smoke-test one PTB-XL records100 waveform and the frozen CNN."
    )
    parser.add_argument("dat_file", type=Path, help="Path to a records100 .dat file")
    args = parser.parse_args()

    raw = read_ptbxl_int16(args.dat_file)
    normalized = global_record_zscore(raw)
    sensitivity = per_lead_record_zscore(raw)

    assert raw.shape == (12, 1000)
    assert normalized.shape == raw.shape
    assert sensitivity.shape == raw.shape
    assert np.isclose(float(normalized.mean()), 0.0, atol=1e-6)
    assert np.isclose(float(normalized.std(ddof=0)), 1.0, atol=1e-6)

    model = CompactECGCNN().eval()
    batch = torch.from_numpy(np.stack([raw, normalized])).float()

    with torch.no_grad():
        logits = model(batch)

    print("waveform:", args.dat_file)
    print("raw shape:", raw.shape)
    print("global z-score mean:", float(normalized.mean()))
    print("global z-score sd:", float(normalized.std(ddof=0)))
    print("model output shape:", tuple(logits.shape))
    print("model parameters:", sum(p.numel() for p in model.parameters()))


if __name__ == "__main__":
    main()
