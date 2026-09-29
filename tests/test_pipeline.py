from __future__ import annotations

import numpy as np
import torch

from src.ecg_pipeline import global_record_zscore, per_lead_record_zscore
from src.model import CompactECGCNN


def test_global_record_zscore_has_zero_mean_and_unit_sd() -> None:
    rng = np.random.default_rng(7)
    x = rng.normal(size=(12, 1000)).astype(np.float32)
    z = global_record_zscore(x)
    assert z.shape == (12, 1000)
    assert np.isclose(float(z.mean()), 0.0, atol=1e-6)
    assert np.isclose(float(z.std(ddof=0)), 1.0, atol=1e-6)


def test_per_lead_zscore_standardizes_each_lead() -> None:
    rng = np.random.default_rng(11)
    x = rng.normal(size=(12, 1000)).astype(np.float32)
    z = per_lead_record_zscore(x)
    means = z.mean(axis=1)
    sds = z.std(axis=1, ddof=0)
    assert np.allclose(means, 0.0, atol=1e-6)
    assert np.allclose(sds, 1.0, atol=1e-6)


def test_cnn_shape_and_backward_pass() -> None:
    model = CompactECGCNN()
    x = torch.randn(4, 12, 1000)
    y = torch.tensor([[0.0], [1.0], [0.0], [1.0]])
    logits = model(x)
    assert logits.shape == (4, 1)
    loss = torch.nn.functional.binary_cross_entropy_with_logits(logits, y)
    loss.backward()
    assert torch.isfinite(loss)
