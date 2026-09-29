from __future__ import annotations

from pathlib import Path

import numpy as np
import torch

from src.ecg_pipeline import global_record_zscore, per_lead_record_zscore
from src.model import CompactECGCNN


def read_ptbxl_int16(path: Path) -> np.ndarray:
    raw = np.fromfile(path, dtype="<i2")
    expected = 12 * 1000
    if raw.size != expected:
        raise ValueError(f"expected {expected} int16 values, got {raw.size}")
    return (raw.reshape(1000, 12).T / 1000.0).astype(np.float32)


def main() -> None:
    data_dir = Path("/mnt/data")
    raw = read_ptbxl_int16(data_dir / "02010_lr.dat")
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

    print("raw shape:", raw.shape)
    print("global z-score mean:", float(normalized.mean()))
    print("global z-score sd:", float(normalized.std(ddof=0)))
    print("model output shape:", tuple(logits.shape))
    print("model parameters:", sum(p.numel() for p in model.parameters()))


if __name__ == "__main__":
    main()
