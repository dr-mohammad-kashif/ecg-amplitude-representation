from __future__ import annotations

import argparse
from pathlib import Path

import pandas as pd

from src.ecg_pipeline import build_binary_labels


def summarize_task(metadata: pd.DataFrame, labels: pd.Series, task: str) -> None:
    valid = labels.notna()
    task_df = metadata.loc[valid, ["patient_id", "strat_fold"]].copy()
    task_df["label"] = labels.loc[valid].astype(int)

    fold_counts = (
        task_df.groupby(["strat_fold", "label"]).size().unstack(fill_value=0).rename(columns={0: "negative", 1: "positive"})
    )

    patient_counts = task_df.groupby("strat_fold")["patient_id"].nunique()

    print(f"\n{task}")
    print("Records by class")
    print(fold_counts.to_string())
    print("Unique patients by fold")
    print(patient_counts.to_string())
    print("Total positive:", int((labels == 1).sum()))
    print("Total negative:", int((labels == 0).sum()))
    print("Excluded:", int(labels.isna().sum()))

    # Check that the official fold variable remains patient-disjoint.
    patient_fold_counts = metadata.groupby("patient_id")["strat_fold"].nunique()
    if int((patient_fold_counts > 1).sum()) != 0:
        raise RuntimeError("patient appears in more than one stratified fold")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--database", type=Path, required=True)
    parser.add_argument("--scp-statements", type=Path, required=True)
    parser.add_argument("--threshold", type=float, default=50.0)
    parser.add_argument(
        "--unthresholded",
        action="store_true",
        help="Use superclass presence regardless of SCP likelihood.",
    )
    args = parser.parse_args()

    metadata = pd.read_csv(args.database, index_col=0)

    threshold = None if args.unthresholded else args.threshold

    for target in ("HYP", "MI"):
        labels = build_binary_labels(
            metadata,
            args.scp_statements,
            target,
            threshold=threshold,
        )
        summarize_task(metadata, labels, target)


if __name__ == "__main__":
    main()
