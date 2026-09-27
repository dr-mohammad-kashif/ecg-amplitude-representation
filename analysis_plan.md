# Analysis plan

This plan is written before the primary model comparison.

## 1. Dataset

The study will use PTB-XL and a documented version of the dataset. The exact version, access date and files used will be recorded in `DATA_PROVENANCE.md`.

The unit of analysis will be an ECG record, with patient identity retained so that repeated records from one patient are not separated across evaluation sets.

## 2. Diagnostic tasks

The initial candidate tasks are binary classification problems that can be defined directly from PTB-XL diagnostic labels.

The first two candidate comparisons are hypertrophy versus normal and myocardial infarction versus normal. These will be checked against the dataset labels and the relevant literature before being frozen.

No task will be selected because it produces a more favorable result.

## 3. Signal representations

The first comparison will use

1. the original signal representation
2. one explicitly defined amplitude-normalized representation

The normalization rule will be documented in code and in the methods section before the main results are interpreted.

## 4. Evaluation split

Patient identity will be respected throughout evaluation. PTB-XL's recommended patient-level folds will be preferred where they fit the final task definition.

A naive row-level random split will not be used as the primary estimate because repeated recordings from the same patient can create leakage.

## 5. Models

The initial models will be deliberately simple

- logistic regression
- random forest

A third model may be added later if it answers a specific methodological question. A more complex model will not be added merely to improve the headline score.

## 6. Metrics

Primary reporting will include AUROC and AUPRC where appropriate.

Calibration will be examined with a calibration curve and Brier score where the task and sample size make this meaningful.

The final report will include uncertainty or variability measures appropriate to the evaluation design.

## 7. Error analysis

The analysis will inspect

- class distribution
- signal quality
- difficult or misclassified records
- whether errors cluster around particular patient or recording characteristics
- whether the representation comparison is driven by a small subset of observations

## 8. Robustness

At least one sensitivity analysis will test whether the main qualitative conclusion changes under a reasonable methodological variation.

Potential variations include a second simple classifier or a clearly justified alternative preprocessing definition.

## 9. Interpretation

The main comparison will be interpreted as an investigation of representation and model behavior within the PTB-XL study design.

A change in predictive performance will not, by itself, be described as proof that clinical information has been lost.

## 10. Reproduction

Once the main analysis is stable, Zaid Wani will reproduce the primary comparison from the repository without being given the expected result in advance. Any discrepancy will be logged and investigated.

## 11. Stopping rule

No new preprocessing variants, models or diagnostic tasks will be added simply because the first result is uninteresting. Extensions must answer a defined methodological question.
