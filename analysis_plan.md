# Analysis plan

I am writing this before the primary comparison. The main choices below are frozen before the test set is used for model selection or result interpretation.

## Dataset

I will use PTB-XL version 1.0.3 from PhysioNet.

The version I am using contains 21,799 clinical 12-lead ECG records from 18,869 patients. The recordings are 10 seconds long. PTB-XL provides the waveforms at 500 Hz and in a 100 Hz version and includes 71 ECG statements organised into diagnostic, form and rhythm categories.

I will keep patient identity throughout data preparation so repeated records from one patient remain within one evaluation fold.

## Diagnostic tasks

I will study two prespecified binary PTB-XL phenotype tasks

- HYP versus NORM-labelled records
- MI versus NORM-labelled records

The primary label rule uses a common SCP likelihood threshold of at least 50% for both the target and NORM labels.

For each task

- Positive = target superclass present at likelihood >= 50%
- Negative = NORM present at likelihood >= 50% and target absent at likelihood >= 50%
- Excluded = neither target nor NORM reaches 50%
- Target plus NORM = positive

The resulting version 1.0.3 cohorts are

| Task | Positive | Negative | Excluded |
| --- | ---: | ---: | ---: |
| HYP vs NORM | 2,258 | 9,434 | 10,107 |
| MI vs NORM | 4,134 | 9,438 | 8,227 |

The unthresholded superclass-presence rule is the prespecified label-definition sensitivity analysis.

I describe the control population as NORM-labelled rather than healthy because the PTB-XL NORM label is an ECG phenotype and is not an independent adjudication of overall patient health.

## Signal representations

I will compare

1. the original native 100 Hz ECG signal in physical mV
2. the same signal after a global record-wise z-score standardization

The primary normalized representation is

z(l,t) = (x(l,t) - mu_r) / sigma_r

where mu_r and sigma_r are calculated from all 12 leads and all 1,000 time points in that record using the population standard deviation, ddof = 0.

No parameters are learned from other records. The transformation is applied independently to each record after the patient-aware split.

A record with non-finite waveform values or zero global standard deviation is technically unusable and is excluded before model fitting. Such exclusions will be recorded by record identifier and reported by task and fold.

The main normalization sensitivity is a per-lead record-wise z-score, with each lead standardized from its own 1,000 samples.

The primary comparison contains no additional filtering, denoising, beat segmentation, resampling or amplitude augmentation. The only representation change is the prespecified normalization operation.

## Evaluation

I will use the official patient-aware PTB-XL fold structure

- folds 1 to 8 = training
- fold 9 = validation
- fold 10 = held-out test

The dataset documentation recommends this arrangement and keeps records from one patient in the same fold.

I will not use a random row-level split as the primary result.

Before waveform-level technical exclusions, the expected primary cohorts are

| Task | Train records | Validation records | Test records |
| --- | ---: | ---: | ---: |
| HYP vs NORM | 9,361 | 1,157 | 1,174 |
| MI vs NORM | 10,849 | 1,354 | 1,369 |

Any technical waveform exclusions will be applied identically to both representation conditions and reported before the final analysis.

## Model

The primary model is a compact 1D convolutional network operating directly on the native 100 Hz, 12-lead waveform.

Input shape is 12 channels by 1,000 time points.

The architecture is

1. Conv1D, 32 filters, kernel 15, same padding, ReLU
2. MaxPool1D, pool size 2
3. Dropout, 0.10
4. Conv1D, 64 filters, kernel 11, same padding, ReLU
5. MaxPool1D, pool size 2
6. Dropout, 0.10
7. Conv1D, 128 filters, kernel 7, same padding, ReLU
8. MaxPool1D, pool size 2
9. Dropout, 0.10
10. Global average pooling over time
11. Linear output layer with one logit

The model contains no BatchNorm, LayerNorm or other internal normalization layer. This is deliberate because the study is testing an input representation change.

The same architecture and parameterisation will be used for raw and normalized conditions.

## Training

The primary implementation will use PyTorch.

I will use

- binary cross-entropy with logits without class weighting
- AdamW optimizer
- learning rate = 0.001
- weight decay = 0.0001
- batch size = 128
- maximum 50 epochs
- early stopping patience = 8 epochs
- best checkpoint selected by validation AUROC
- fixed primary random seed = 1

No data augmentation, mixup, random amplitude scaling, denoising or other signal perturbation will be used in the primary analysis.

The test set will not be used for architecture, hyperparameter, checkpoint or threshold selection.

As a training-stability sensitivity, the same frozen pipeline will be repeated with seeds 1, 2 and 3. This does not change the primary seed-1 estimand.

## Primary estimand

For task t, define

Delta_t = AUROC_normalized,t - AUROC_raw,t

The primary estimand is the cross-task representation-effect contrast

Delta_HYP - Delta_MI

This asks whether the change in AUROC caused by the prespecified representation change differs between the two tasks.

The task-specific Delta values are secondary estimands and will also be reported.

This is an observational performance contrast within a benchmark dataset. It is not interpreted as a causal treatment effect.

## Uncertainty and paired comparison

The raw and normalized conditions use the same held-out records, so predictions are paired.

The primary uncertainty procedure is a patient-level paired percentile bootstrap with 5,000 resamples.

For each bootstrap resample, patients in the held-out fold are sampled with replacement. All eligible test records belonging to a sampled patient are retained, preserving within-patient clustering and the pairing between raw and normalized predictions.

The same patient resample is used for both tasks. A sampled patient contributes to a task-specific bootstrap calculation only when that patient has eligible records for that task.

The primary report will give a point estimate and 95% percentile bootstrap confidence interval for Delta_HYP - Delta_MI. Task-specific Delta values will receive their own 95% confidence intervals.

Bootstrap resamples that contain only one class for a task will be rejected and resampled again so that the AUROC is defined.

I will not use DeLong as the primary inferential procedure because the standard formulation does not account for repeated records within patients.

## Secondary metrics

For each task and representation I will report

- AUROC
- average precision from scikit-learn's fixed average_precision_score definition
- positive-class prevalence in the held-out test cohort
- Brier score

I will provide calibration plots using 10 equal-frequency bins when each task has sufficient variation in predicted probabilities.

AUPRC and Brier-score differences will be evaluated within task. I will not compare raw AUPRC or Brier values across HYP and MI as if they were on a common prevalence scale.

## Error analysis

I will inspect

- class balance
- waveform technical quality and technical exclusions
- difficult and misclassified records
- patient or recording characteristics around errors
- whether the representation comparison is driven by a small part of the evaluation set

Demographic variables will be descriptive only and will not be model inputs.

## Prespecified robustness analyses

The following sensitivity analyses are fixed before the primary test result

1. global record-wise z-score versus record-wise per-lead z-score
2. the primary >=50% likelihood label rule versus the unthresholded superclass-presence rule
3. training stability across seeds 1, 2 and 3 using the frozen pipeline

These address normalization scope, annotation certainty, and optimization variability.

I will not add further robustness analyses because one produces a more favourable result. Any analysis that becomes relevant only after seeing the primary result will be labelled exploratory.

## Interpretation

If the two representations perform differently, I will treat that as a finding about representation and model behaviour under the evaluation I actually used.

The primary claim will concern the difference in observed AUROC change between the two prespecified tasks.

A performance change on its own will not be described as proof that clinical information has been lost.

## Independent reproduction

Once the primary comparison is stable, Zaid will work from a clean copy of the repository and reproduce the primary result without being given the expected value in advance.

The reproduction record will identify the repository commit, dataset version, environment, command and any discrepancy.

## Stopping rule

I will not add new tasks, models or preprocessing variants simply because the primary result is weak or uninteresting. An extension requires a methodological reason.

The held-out test set will not be inspected for model or analysis selection.
