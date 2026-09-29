from __future__ import annotations

import pandas as pd
import numpy as np

from src.ecg_pipeline import build_binary_labels, validate_records100_array


def write_scp_fixture(path):
    table = pd.DataFrame(
        {
            "diagnostic": [1, 1, 1],
            "diagnostic_class": ["NORM", "HYP", "MI"],
        },
        index=["NORM", "LVH", "IMI"],
    )
    table.to_csv(path)


def test_primary_label_rule(tmp_path):
    scp_path = tmp_path / "scp_statements.csv"
    write_scp_fixture(scp_path)

    metadata = pd.DataFrame(
        {
            "scp_codes": [
                "{'LVH': 100}",
                "{'NORM': 100}",
                "{'LVH': 100, 'NORM': 100}",
                "{'LVH': 35, 'NORM': 100}",
                "{'MI': 50}",
                "{'MI': 35, 'NORM': 50}",
                "{'STTC': 100}",
            ]
        }
    )

    hyp = build_binary_labels(metadata, scp_path, "HYP", threshold=50)
    mi = build_binary_labels(metadata, scp_path, "MI", threshold=50)

    assert hyp.tolist() == [1.0, 0.0, 1.0, 0.0, np.nan, np.nan, np.nan]
    assert mi.tolist() == [np.nan, 0.0, 0.0, 0.0, 1.0, 0.0, np.nan]


def test_records100_validation():
    x = np.zeros((12, 1000), dtype=np.float32)
    names = ["I", "II", "III", "AVR", "AVL", "AVF", "V1", "V2", "V3", "V4", "V5", "V6"]
    validate_records100_array(x, 100, names)
