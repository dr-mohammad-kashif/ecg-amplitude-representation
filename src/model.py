from __future__ import annotations

import torch
from torch import nn


class CompactECGCNN(nn.Module):
    """Frozen primary model for the direct 100 Hz PTB-XL representation."""

    def __init__(self) -> None:
        super().__init__()
        self.features = nn.Sequential(
            nn.Conv1d(12, 32, kernel_size=15, padding="same"),
            nn.ReLU(),
            nn.MaxPool1d(kernel_size=2),
            nn.Dropout(p=0.10),
            nn.Conv1d(32, 64, kernel_size=11, padding="same"),
            nn.ReLU(),
            nn.MaxPool1d(kernel_size=2),
            nn.Dropout(p=0.10),
            nn.Conv1d(64, 128, kernel_size=7, padding="same"),
            nn.ReLU(),
            nn.MaxPool1d(kernel_size=2),
            nn.Dropout(p=0.10),
        )
        self.pool = nn.AdaptiveAvgPool1d(1)
        self.output = nn.Linear(128, 1)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        if x.ndim != 3 or x.shape[1] != 12 or x.shape[2] != 1000:
            raise ValueError("expected input shape (batch, 12, 1000)")
        x = self.features(x)
        x = self.pool(x).squeeze(-1)
        return self.output(x)
