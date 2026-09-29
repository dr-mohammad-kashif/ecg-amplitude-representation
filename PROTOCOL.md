# Study protocol

## Study title

Task-dependent effects of global record-wise z-score standardization on ECG classification using PTB-XL

## Study status

This is a prespecified secondary-data computational study. No new participant recruitment or clinical data collection is planned.

The primary analysis has not been run.

## Research question

Under a fixed direct-waveform model, does global record-wise z-score standardization change ECG classification performance differently for PTB-XL hypertrophy and myocardial infarction phenotypes?

The primary contrast is the difference between the raw-versus-standardized AUROC change for HYP and the corresponding change for MI.

## Objectives

### Primary objective

Estimate whether the representation-related change in AUROC differs between the HYP and MI tasks.

### Secondary objectives

Estimate the representation-related AUROC change within each task.

Compare raw and normalized representations using average precision and Brier score within each task.

Describe calibration behaviour with reliability plots.

Examine whether the main result is stable to the prespecified normalization, label-definition and random-seed sensitivity analyses.

## Dataset and provenance

The study uses PTB-XL version 1.0.3 from PhysioNet.

The dataset contains 21,799 ten-second clinical 12-lead ECG records from 18,869 patients. The official release supplies native 500 Hz waveforms and a 100 Hz records100 version.

Raw PTB-XL data are not stored in this repository.

Dataset provenance, local metadata hashes, fold structure and the metadata audit are recorded in [data_provenance.md](data_provenance.md) and [data_audit.md](data_audit.md).

## Unit of analysis

The primary scientific unit is the ECG record.

Patient identity is retained because some patients contribute multiple ECG records.

Patient clustering is handled in the uncertainty analysis.

## Eligibility and task construction

Two binary phenotype tasks are prespecified

- HYP versus NORM
- MI versus NORM

The primary label rule uses a common SCP likelihood threshold of at least 50% for both the target superclass and NORM.

For a given task

- target-positive = target superclass present at likelihood >= 50%
- target-negative = NORM present at likelihood >= 50% and target absent at likelihood >= 50%
- excluded = neither target nor NORM reaches 50%
- target plus NORM = target-positive

The primary cohort counts in the metadata audit are

| Task | Positive | Negative | Excluded |
| --- | ---: | ---: | ---: |
| HYP vs NORM | 2,258 | 9,434 | 10,107 |
| MI vs NORM | 4,134 | 9,438 | 8,227 |

The unthresholded superclass-presence rule is a prespecified sensitivity analysis.

NORM-labelled is used instead of healthy when describing the comparison group because the PTB-XL NORM label is an ECG phenotype and not an independent adjudication of overall patient health.

## Waveform representation

The primary input is the native PTB-XL v1.0.3 records100 waveform.

Each record is represented as

- 12 leads
- 1,000 samples per lead
- 100 Hz
- 10 seconds
- physical signal values in mV after WFDB conversion

The actual paired waveform files inspected during the integrity audit matched the documented structure.

No independent resampling is performed in the primary analysis.

A full ingestion check will verify that each required waveform file exists, can be read, has the expected dimensions and sampling rate, and contains finite values.

Technical waveform failures are excluded before model fitting, identically from both representation conditions, logged by record identifier and reported by task and fold.

## Representation conditions

### Raw condition

The physical 100 Hz waveform is used without the study's normalization transformation.

### Primary normalized condition

For each record, calculate

z(l,t) = (x(l,t) - mu_r) / sigma_r

where mu_r and sigma_r are calculated across all 12 leads and all 1,000 samples in that record.

The standard deviation uses ddof = 0.

This transformation is record-local. No parameters are estimated from other records.

### Sensitivity normalization

A record-wise per-lead z-score is used as the prespecified normalization-scope sensitivity.

Each lead is centered and scaled using its own 1,000 samples. If any lead has zero standard deviation, the record is excluded from this sensitivity analysis only; this does not alter primary analysis eligibility.

No other normalization, denoising, beat segmentation, filtering, augmentation or amplitude perturbation is part of the primary experiment.

## Data splitting and leakage control

The official patient-aware PTB-XL folds are used

- folds 1 to 8 for training
- fold 9 for validation
- fold 10 for held-out testing

No random row-level split is used.

The final model and all preprocessing decisions are made without using held-out test performance.

The primary normalisation transformation is record-local, so its parameters are derived only from the individual record. Any future population-level preprocessing would be fit on training data only.

## Primary model

The primary classifier is a compact 1D convolutional network.

Architecture

1. Conv1D, 32 filters, kernel 15, same padding, ReLU
2. MaxPool1D, pool 2
3. Dropout 0.10
4. Conv1D, 64 filters, kernel 11, same padding, ReLU
5. MaxPool1D, pool 2
6. Dropout 0.10
7. Conv1D, 128 filters, kernel 7, same padding, ReLU
8. MaxPool1D, pool 2
9. Dropout 0.10
10. Global average pooling
11. Linear output with one logit

The network has no BatchNorm, LayerNorm or other internal normalization layer.

The architecture is used identically for all representation conditions and tasks.

## Model training

Implementation framework: PyTorch.

Primary training settings

- binary cross-entropy with logits
- no class weighting
- AdamW
- learning rate 0.001
- weight decay 0.0001
- batch size 128
- maximum 50 epochs
- early stopping patience 8 epochs
- best checkpoint selected by validation AUROC
- primary random seed 1

The same initialization seed, record order, optimizer settings and stopping rule are used for the raw and normalized fits within each task.

No augmentation, mixup, random amplitude scaling or denoising is used.

The test set is never used for model selection or threshold selection.

The implementation will record the software environment and repository commit associated with the primary run.

## Technical exclusions

A waveform is technically unusable for the primary model if it

- is missing
- cannot be read
- does not match the expected 12 x 1,000 representation
- has the wrong sampling rate
- contains non-finite values
- has a zero global standard deviation for the primary normalization

The same eligibility decision is applied to raw and normalized conditions.

Technical exclusions are not based on model performance.

## Primary estimand

For each task t

Delta_t = AUROC_normalized,t - AUROC_raw,t

The primary estimand is

Delta_HYP - Delta_MI

This is a descriptive cross-task representation-effect contrast. It is not interpreted as a causal treatment effect.

## Statistical analysis

The primary evaluation uses the held-out fold 10 predictions.

The primary uncertainty procedure is a patient-level paired percentile bootstrap with 5,000 resamples.

For each bootstrap draw

1. sample test-set patients with replacement
2. include all eligible test records belonging to sampled patients
3. preserve the raw/normalized prediction pairing
4. calculate the task-specific AUROC values and representation effects
5. calculate the cross-task representation-effect contrast when both task-level AUROCs are defined

The same patient resample is used for HYP and MI. The two task-specific test populations share 939 patients before technical waveform exclusions.

A bootstrap draw with only one class for a task is rejected and resampled.

The primary result is the point estimate and 95% percentile bootstrap confidence interval for Delta_HYP - Delta_MI.

The task-specific Delta values also receive 95% bootstrap confidence intervals.

## Secondary metrics

For each task and representation

- AUROC
- average precision using scikit-learn average_precision_score
- positive-class prevalence
- Brier score

Within each task, raw-versus-normalized differences in average precision and Brier score will use the same patient-level bootstrap framework for 95% confidence intervals.

Calibration plots use fixed probability bins of width 0.10. Empty bins are omitted.

## Robustness analyses

Three analyses are prespecified

1. global record-wise z-score versus record-wise per-lead z-score
2. primary >=50% likelihood labels versus unthresholded superclass-presence labels
3. training stability using seeds 1, 2 and 3 with the frozen pipeline

No additional robustness analysis will be introduced because it produces a more favourable result.

Analyses prompted only by inspection of the primary result will be labelled exploratory.

## Error analysis

After the primary endpoint is computed, I will inspect errors and subgroup patterns descriptively.

The error analysis will consider

- waveform technical quality
- difficult and misclassified records
- patient and recording characteristics available in PTB-XL
- whether performance differences are concentrated in a small subset of records

The error analysis cannot trigger changes to the primary model, task definition or primary estimand.

## Reproduction

Zaid will reproduce the primary analysis from a clean copy of the repository and the stated environment.

The expected primary result will not be provided in advance.

The reproduction record will report the repository commit, environment, dataset version and any discrepancy.

## Deviations

Any change to this protocol after registration or before the primary result is interpreted will be documented with

- what changed
- why it changed
- whether the change was made before or after test-set performance was inspected
- whether the analysis remains primary, secondary or exploratory

## Interpretation boundaries

The study does not establish clinical utility, clinical superiority, patient benefit or a causal effect of normalization.

It tests a specific representation change in a public research dataset under a fixed model and prespecified evaluation design.

A performance decrease after standardization will not, by itself, be described as proof that clinical information was destroyed.

## Ethical and governance considerations

The project uses a public secondary research dataset and does not recruit participants or collect new identifiable data.

The study will follow the access and use conditions stated by the PTB-XL data provider.

This repository does not contain the raw PTB-XL waveform collection.

## Relationship to other study documents

- [research_question.md](research_question.md) states the research question and hypothesis.
- [analysis_plan.md](analysis_plan.md) contains the operational analysis specification.
- [data_audit.md](data_audit.md) records the data and waveform integrity audits.
- [methods_literature_review.md](methods_literature_review.md) records methodological evidence.
- [research_log.md](research_log.md) records design changes and deviations.
- [STATISTICAL_ANALYSIS_PLAN.md](STATISTICAL_ANALYSIS_PLAN.md) contains the statistical analysis details.
