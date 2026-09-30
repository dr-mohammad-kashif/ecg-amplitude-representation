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
                "{'IMI': 50}",
                "{'IMI': 35, 'NORM': 50}",
                "{'STTC': 100}",
            ]
        }
    )

    hyp = build_binary_labels(metadata, scp_path, "HYP", threshold=50)
    mi = build_binary_labels(metadata, scp_path, "MI", threshold=50)

    assert hyp.iloc[0] == 1.0
    assert hyp.iloc[1] == 0.0
    assert hyp.iloc[2] == 1.0
    assert hyp.iloc[3] == 0.0
    assert np.isnan(hyp.iloc[4])
    assert hyp.iloc[5] == 0.0
    assert np.isnan(hyp.iloc[6])
    assert np.isnan(mi.iloc[0])
    assert mi.iloc[1] == 0.0
    assert mi.iloc[2] == 0.0
    assert mi.iloc[3] == 0.0
    assert mi.iloc[4] == 1.0
    assert mi.iloc[5] == 0.0
    assert np.isnan(mi.iloc[6])


def test_unthresholded_label_rule(tmp_path):
    scp_path = tmp_path / "scp_statements.csv"
    write_scp_fixture(scp_path)

    metadata = pd.DataFrame(
        {
            "scp_codes": [
                "{'LVH': 15}",
                "{'NORM': 1}",
                "{'LVH': 0, 'NORM': 1}",
                "{'STTC': 100}",
            ]
        }
    )

    hyp = build_binary_labels(metadata, scp_path, "HYP", threshold=None)

    assert hyp.iloc[0] == 1.0
    assert hyp.iloc[1] == 0.0
    assert hyp.iloc[2] == 1.0
    assert np.isnan(hyp.iloc[3])


def test_records100_validation():
    x = np.zeros((12, 1000), dtype=np.float32)
    names = ["I", "II", "III", "AVR", "AVL", "AVF", "V1", "V2", "V3", "V4", "V5", "V6"]
    validate_records100_array(x, 100, names)
