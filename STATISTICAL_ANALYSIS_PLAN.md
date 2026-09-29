# Statistical analysis plan

This plan is aligned with PROTOCOL.md and analysis_plan.md.

## Primary estimand

For each task t

Delta_t = AUROC_normalized,t - AUROC_raw,t

The primary estimand is Delta_HYP - Delta_MI.

This is a descriptive cross-task representation-effect contrast and is not a causal treatment effect.

## Primary fits

The primary analysis consists of four fits

- HYP raw
- HYP normalized
- MI raw
- MI normalized

The architecture, training settings, folds and evaluation records are fixed across conditions. The primary seed is 1.

## Uncertainty

The primary interval is a 95% percentile bootstrap confidence interval with 5,000 patient-level resamples.

Patients are sampled with replacement. All eligible test records belonging to a sampled patient are retained together.

The same patient resample is used for both tasks. Raw and normalized predictions for a record remain paired.

A bootstrap draw with only one class for a task is rejected and resampled.

The task-specific Delta values and the primary cross-task contrast are calculated within each bootstrap draw.

## Secondary metrics

Report AUROC, average precision, positive-class prevalence and Brier score.

Average precision uses scikit-learn average_precision_score.

Within each task, raw-versus-normalized differences in average precision and Brier score use the same patient-level bootstrap framework.

## Calibration

Calibration is secondary.

Use fixed probability bins from 0.0 to 1.0 in increments of 0.10.

For each non-empty bin report mean predicted probability, observed positive fraction and number of records.

No recalibration is performed in the primary analysis.

## Thresholds

No classification threshold is optimized on the held-out test set.

AUROC and average precision use continuous predictions. A fixed 0.50 threshold may be used only for secondary error summaries.

## Sensitivity analyses

The prespecified sensitivity analyses are

1. global record-wise z-score versus record-wise per-lead z-score
2. >=50% likelihood labels versus unthresholded superclass-presence labels
3. training seeds 1, 2 and 3

Exploratory analyses are reported separately.

## Missing and technical failures

Technical waveform failures are excluded before model fitting and recorded by task and fold.

No waveform imputation is performed.

## Reproducibility

The final run will record Python, PyTorch, NumPy, pandas, scikit-learn, SciPy and WFDB versions, random seeds, dataset version, repository commit and the exact run command.

The final environment specification will be stored with the analysis release.

## Reporting

The final analysis will report cohort counts, positive prevalence, AUROC, task-specific Delta AUROC, the primary Delta_HYP - Delta_MI contrast, 95% confidence intervals, average precision, Brier score, calibration plots, sensitivity analyses and technical exclusions.
