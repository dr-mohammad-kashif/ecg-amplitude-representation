# Analysis plan

I am writing this before I run the primary comparison. I want the main choices to be decided before I see the result.

## Dataset

I will use PTB-XL version 1.0.3 from PhysioNet.

The version I am using contains 21799 clinical 12-lead ECG records from 18869 patients. The recordings are 10 seconds long. PTB-XL provides the waveforms at 500 Hz and in a 100 Hz version and includes 71 ECG statements organised into diagnostic, form and rhythm categories.

I will keep patient identity throughout the data preparation so that repeated records from one patient do not end up across different evaluation sets.

## Diagnostic tasks

My initial candidates are

- HYP versus NORM
- MI versus NORM

These are still candidates. I will check the actual PTB-XL label structure, overlaps and exclusions before I freeze them.

I chose HYP because amplitude has a direct role in traditional ECG criteria for hypertrophy, and MI gives me a second diagnostic phenotype with a different clinical basis. The comparison is only useful if I am willing to let the data disagree with that expectation.

## Signal representations

I will compare

1. the original ECG signal
2. one clearly defined amplitude-normalized version

I will write the exact normalization rule down before running the main comparison and implement it once in a shared preprocessing function.

I will not keep adding different normalization methods just because one produces a more interesting result.

## Evaluation

I will use the patient-aware PTB-XL fold structure if it fits the final label definitions.

The dataset documentation recommends folds 1 to 8 for training, fold 9 for validation and fold 10 for testing. The folds were created while keeping records from the same patient together.

I will not use a random row-level split as the primary result.

## Model

The current model candidate is a small 1D convolutional model applied directly to the 100 Hz, 12-lead waveform.

I am considering this because the scientific question is about the signal representation itself. A direct waveform model avoids adding a feature-engineering stage that could change amplitude information before the model sees it.

The architecture will be kept identical between the raw and normalized conditions.

I will not freeze the architecture until I inspect the waveform files and measure the computational cost. Logistic regression and random forest remain possible secondary baselines only if I later define a compact feature representation with a clear methodological reason.

## Metrics

I will report AUROC and AUPRC where appropriate.

I will also look at calibration using calibration curves and the Brier score when the final class balance and sample size make that useful.

The final report will include an uncertainty or variability measure that fits the final evaluation design.

## Error analysis

I want to know whether any observed difference comes from a small group of records or a broader pattern. I will therefore inspect

- class balance
- signal quality
- difficult and misclassified records
- patient or recording characteristics around errors
- whether the representation comparison is being driven by a small part of the dataset

## Robustness

Before the primary analysis, I will choose at least one sensitivity analysis and record its rationale in the protocol.

The check may involve a second simple classifier, a defensible alternative normalization definition, or another change that addresses a specific methodological concern identified before the primary result is interpreted.

I will not choose a sensitivity analysis because it produces a more favourable result. Any additional analysis that becomes relevant only after seeing the primary result will be labelled exploratory and kept separate from the prespecified robustness analysis.

## Interpretation

If the two representations perform differently, I will treat that as a finding about the representation and model under the evaluation I actually used.

A performance change on its own will not be described as proof that clinical information has been lost.

## Independent reproduction

Once the primary comparison is stable, Zaid will work from a clean copy of the repository and reproduce the main result without being given the expected value in advance.

Any difference between our results will be recorded and investigated.

## Stopping rule

I am not planning to add new tasks, models or preprocessing variants simply because the first result is weak or uninteresting. An extension needs a methodological reason.
