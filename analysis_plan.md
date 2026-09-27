# Analysis plan

This plan is written before the primary model comparison.

## 1. Dataset

The study will use PTB-XL version 1.0.3 from PhysioNet. The current release contains 21799 clinical 12-lead ECG records from 18869 patients. The waveforms are available at 500 Hz and in a 100 Hz version, and diagnostic statements are organized into superclasses and subclasses.

The unit of analysis will be an ECG record, with patient identity retained so that repeated records from one patient are not separated across evaluation sets.

## 2. Diagnostic tasks

The initial candidates are

- HYP versus NORM
- MI versus NORM

These are candidate tasks, not yet frozen labels. The data audit will confirm the exact label construction and exclusion rules before analysis.

The choice is not based on which task is expected to produce a stronger score. HYP gives a clinically grounded case in which QRS voltage has a direct role in traditional ECG criteria, while MI provides a second diagnostic phenotype with a different clinical basis. The study will test whether the preprocessing effect actually differs rather than assuming that it will.

## 3. Signal representations

The primary comparison will use

1. the original signal representation
2. one explicitly defined amplitude-normalized representation

The normalization rule will be written in plain mathematical terms and implemented once in a shared preprocessing function.

No alternative normalization will be added until the primary analysis is complete unless a methodological problem requires it.

## 4. Evaluation split

Patient identity will be respected throughout evaluation.

The PTB-XL recommended patient-aware folds will be used where they fit the final task definition. Fold 10 is intended for held-out testing and fold 9 for validation in the dataset documentation.

A row-level random split will not be used as the primary estimate because repeated recordings from the same patient can otherwise leak across evaluation sets.

## 5. Models

The initial models will be deliberately simple

- logistic regression
- random forest

A more complex model may be added later if it answers a defined methodological question. It will not be added simply to improve the headline score.

## 6. Metrics

Primary reporting will include AUROC and AUPRC where appropriate.

Calibration will be examined with a calibration curve and Brier score where the sample size and class balance make this meaningful.

The final report will include uncertainty or variability measures appropriate to the final evaluation design.

## 7. Error analysis

The analysis will inspect

- class distribution
- signal quality
- difficult or misclassified records
- whether errors cluster around particular patient or recording characteristics
- whether the representation comparison is driven by a small subset of observations

## 8. Robustness

At least one sensitivity analysis will test whether the main qualitative conclusion changes under a reasonable methodological variation.

Potential variations include a second simple classifier or a clearly justified alternative normalization definition.

## 9. Interpretation

The main comparison will be interpreted as an investigation of representation and model behavior within the PTB-XL study design.

A change in predictive performance will not, by itself, be described as proof that clinical information has been lost.

## 10. Reproduction

Once the main analysis is stable, Zaid Wani will reproduce the primary comparison from the repository without being given the expected result in advance. Any discrepancy will be logged and investigated.

## 11. Stopping rule

No new preprocessing variants, models or diagnostic tasks will be added simply because the first result is uninteresting. Extensions must answer a defined methodological question.
