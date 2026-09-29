# OSF preregistration draft

This draft is aligned with the frozen study protocol and statistical analysis plan.

## Study title

Task-dependent effects of global record-wise z-score standardization on ECG classification using PTB-XL

## Existing data status

The dataset already exists and has been accessed.

The metadata and representative waveform files have been audited before this registration. Those checks include dataset structure, label distributions, fold structure, representative waveform integrity and the prespecified task cohort definitions.

No primary model has been fit on the held-out test set and no primary test-set performance has been used to choose the model, normalization rule, task definitions, or statistical estimand.

For the OSF existing-data question, this should be described as registration following analysis of the existing data, while making clear that the confirmatory primary model comparison and held-out test analysis have not yet been conducted.

## Research question

Under a fixed direct-waveform model, does global record-wise z-score standardization change ECG classification performance differently for PTB-XL hypertrophy and myocardial infarction phenotypes?

## Hypothesis

The change in AUROC under global record-wise z-score standardization will not be identical for the HYP and MI tasks.

This is a non-directional research hypothesis about task-dependent representation effects, not a hypothesis that standardization will improve or worsen performance overall.

## Dataset

PTB-XL version 1.0.3 from PhysioNet.

The release contains 21,799 clinical 12-lead ECG records from 18,869 patients. Each recording is 10 seconds long.

The primary waveform input is the native 100 Hz records100 representation.

## Unit of analysis

The scientific unit is the ECG record.

Patient identity is retained for patient-aware splitting and clustered uncertainty estimation because some patients contribute multiple records.

## Primary phenotype definitions

Two binary PTB-XL phenotype tasks are prespecified

- HYP versus NORM-labelled records
- MI versus NORM-labelled records

The primary label rule uses a common SCP likelihood threshold of at least 50% for both target and NORM.

Positive

- target superclass present at likelihood >= 50%

Negative

- NORM present at likelihood >= 50%
- target absent at likelihood >= 50%

Excluded

- neither target nor NORM reaches 50%

Target plus NORM is assigned to the target-positive class.

The unthresholded superclass-presence rule is the prespecified label-definition sensitivity analysis.

## Primary representation comparison

Raw condition

Use the native 100 Hz waveform in physical mV.

Normalized condition

For every record calculate

z(l,t) = (x(l,t) - mu_r) / sigma_r

where the mean and population standard deviation are calculated across all 12 leads and all 1,000 time points in that record.

The transformation is record-local. No parameters are learned from other records.

No filtering, denoising, beat segmentation, independent resampling or amplitude augmentation is used in the primary comparison.

## Sensitivity normalization

A record-wise per-lead z-score is the prespecified normalization-scope sensitivity.

Each lead is centered and scaled using its own 1,000 samples.

A record with a zero-variance lead is excluded from this sensitivity analysis only.

## Data splitting

Use the official patient-aware PTB-XL folds

- folds 1 to 8 training
- fold 9 validation
- fold 10 held-out test

No random row-level split is used.

## Primary model

A compact direct-waveform 1D CNN

1. Conv1D 32 filters, kernel 15, same padding, ReLU
2. MaxPool1D 2
3. Dropout 0.10
4. Conv1D 64 filters, kernel 11, same padding, ReLU
5. MaxPool1D 2
6. Dropout 0.10
7. Conv1D 128 filters, kernel 7, same padding, ReLU
8. MaxPool1D 2
9. Dropout 0.10
10. Global average pooling
11. Linear one-logit output

There is no BatchNorm, LayerNorm or other internal normalization layer.

## Training

PyTorch.

- BCE with logits
- no class weighting
- AdamW
- learning rate 0.001
- weight decay 0.0001
- batch size 128
- maximum 50 epochs
- early stopping patience 8
- best checkpoint by validation AUROC
- primary seed 1

The same initialization seed, record order, optimizer settings and stopping rule are used between raw and normalized fits within each task.

The test set is not used for model selection, hyperparameter selection, checkpoint selection or threshold selection.

Training-stability sensitivity uses seeds 1, 2 and 3 with the same frozen pipeline.

## Primary estimand

For each task t

Delta_t = AUROC_normalized,t - AUROC_raw,t

The primary estimand is

Delta_HYP - Delta_MI

This is a descriptive cross-task representation-effect contrast and is not treated as a causal treatment effect.

## Primary uncertainty

Use a patient-level paired percentile bootstrap with 5,000 resamples.

Sample unique test-set patients with replacement and retain all eligible test records belonging to sampled patients.

Keep raw and normalized predictions paired.

Use the same patient resample across HYP and MI when patients contribute to both task populations.

Reject and resample a bootstrap draw if a task contains only one outcome class.

Report the point estimate and 95% percentile bootstrap confidence interval for the primary contrast.

## Secondary outcomes

For each task and representation report

- AUROC
- average precision using scikit-learn average_precision_score
- positive-class prevalence
- Brier score

Within-task raw-versus-normalized differences in average precision and Brier score use the same patient-level bootstrap framework.

Calibration is secondary. Reliability plots use fixed probability bins of width 0.10 with empty bins omitted.

No recalibration is performed.

## Prespecified sensitivity analyses

1. global record-wise z-score versus record-wise per-lead z-score
2. >=50% likelihood labels versus unthresholded superclass-presence labels
3. training stability using seeds 1, 2 and 3

## Technical exclusions

Before model fitting, records must

- exist as the required records100 waveform file
- be readable
- have 12 leads
- have 1,000 samples per lead
- have 100 Hz sampling
- contain finite signal values
- satisfy the primary global-standardization feasibility check

Technical failures are excluded identically from raw and normalized conditions, logged by record identifier, and reported by task and fold.

No waveform imputation is performed.

## Confirmatory versus exploratory analysis

The primary cross-task AUROC contrast is confirmatory within the scope of this preregistration.

Task-specific AUROC changes, average precision, Brier score, calibration plots and prespecified sensitivity analyses are supporting analyses.

Any analysis prompted by inspection of the primary test result is exploratory and will be labelled as such.

## Deviations

Any change after registration will be recorded in the research log with the reason for the change and whether the primary test-set result had already been inspected.

## Reproducibility

The repository will retain the exact preprocessing definitions, model configuration, random seeds, software environment, dataset version, run commands and result provenance needed to reproduce the analysis.

The raw PTB-XL data will not be stored in the public repository.

## Registration timing

The registration should be submitted after the protocol and statistical analysis plan have been reviewed and before the primary held-out test-set analysis is interpreted.

The existing metadata audit and waveform integrity checks are documented as pre-registration exploratory/data-preparation work rather than represented as if the dataset had not previously been accessed.
