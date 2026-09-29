# Methods review

I am using this document to collect the methodological decisions that can change the design of the ECG study. It is a synthesis of the evidence, not the full literature record.

The detailed evidence is now recorded in [methods_literature_review.md](methods_literature_review.md).

## Current methodological position

The study is a secondary-data computational study using the PTB-XL research dataset. Secondary-data guidance makes it important to define the data flow, unit of analysis, label construction, exclusions and analysis decisions explicitly before the main result.

The current methodological evidence also changes how I think about normalization. Normalization is not one operation. Record-local global z-score, record-local per-lead z-score, min-max transformations and population-fitted transformations answer different questions.

The primary representation comparison is fixed as the original 100 Hz waveform versus a global record-wise z-score applied across all retained leads and time points within each record. This transformation changes both location and scale. The record-wise per-lead z-score is the prespecified sensitivity condition because it additionally removes lead-specific scale.

## Secondary-data design

STROSA, STROSA-2 and the 2026 Good Practice Secondary Data Analysis recommendations reinforce the need to document

- data source and version
- data flow and selection
- unit of analysis
- variable and label definitions
- analysis strategy
- registration and deviations
- reproducibility information

I will use these as transferable guidance rather than claim direct compliance with a German secondary-data standard.

## Label construction

PTB-XL is multilabel. HYP, MI, NORM and other diagnostic superclasses can overlap, and diagnostic statements carry likelihood information.

The primary rule is frozen at a common >=50% likelihood threshold for both target and NORM labels. Target-plus-NORM records remain target-positive. Records reaching neither threshold are excluded.

The unthresholded superclass-presence rule is the prespecified label-definition sensitivity analysis.

## Leakage and data splitting

The primary split should remain patient-aware.

Any population-fitted preprocessing must be fit on training data and then applied to validation and test data. A record-local transformation needs to be described explicitly because its parameters are derived from the record itself.

The study should distinguish this from preprocessing that shares information across records.

## Paired evaluation and uncertainty

The raw and normalized representations use the same underlying held-out records, so the performance comparison is paired.

A patient-level paired percentile bootstrap is the primary inferential procedure because PTB-XL can contain multiple records for one patient. DeLong is not used as the primary procedure because its standard formulation does not account for repeated records within patients.

The current primary estimand candidate is the difference in AUROC between the raw and normalized representations for a predefined task on the same held-out evaluation population.

A final statistical analysis plan should define the interval construction before the result is inspected.

## Calibration and class imbalance

AUROC and AUPRC should be reported together, with the positive-class prevalence stated for each task. AUPRC is especially useful when the positive class is uncommon, but it should not be interpreted without its prevalence.

Calibration remains a secondary analysis. I am currently planning a calibration plot and Brier score, with calibration slope and intercept considered if the final model and sample size make them informative.

## Information preservation

I am no longer treating information preservation as a single measurable object.

I am separating numerical signal preservation, clinically meaningful waveform structure and task-relevant information available to the model.

The primary result should therefore be described as a change in predictive behaviour under a defined representation. A performance change by itself is not proof that clinical information was destroyed.

## Model input

The primary input representation is fixed as the native PTB-XL v1.0.3 records100 waveform.

Each record enters the model as a 12-lead, 1,000-sample waveform at 100 Hz. I selected this because the representation is supplied directly by the dataset, the actual waveform headers and binary files inspected match that specification, and contemporary PTB-XL work uses the same 100 Hz representation.

No additional resampling will be performed for the primary analysis.

The primary model is a compact three-block 1D convolutional network with max pooling, dropout, global average pooling and a single-logit output. No BatchNorm, LayerNorm or other internal normalization layer is used because the study is testing the effect of an input representation change.

I am not using logistic regression or random forest as primary baselines. Applying them to the full waveform would require flattening or feature engineering and would add another representation decision.

## Robustness

The most relevant robustness analysis is likely to be a reasoned alternative normalization or label definition rather than a large collection of extra models.

The recent PTB-XL preprocessing literature also shows that preprocessing effects can depend on architecture. This supports keeping the model fixed when testing the representation effect.

## Reproducibility

The repository should record the dataset version, environment, preprocessing definitions, model configuration, random seeds where applicable, analysis commands, output provenance and repository commit associated with a result.

Zaid's independent reproduction should begin from a clean copy of the public repository without being given the expected result.

## AI-assisted research

AI is being used as a research accelerator, not as the authority for scientific claims.

It can assist with literature discovery, search-term generation, code drafts, debugging, documentation and adversarial review. Claims and citations still have to be checked against the original sources or the project's own outputs.

The current evidence on AI-assisted evidence synthesis supports keeping human verification in the loop.

## Reporting guidance I will use

- TRIPOD+AI for relevant prediction-model reporting
- PROBAST+AI for risk of bias and applicability
- STROBE for relevant observational reporting
- STROSA and Good Practice Secondary Data Analysis for secondary-data issues
- SPIRIT 2025 only for transferable protocol discipline
- PRISMA-S only if the literature search becomes systematic
- FAIR for research objects and provenance
- the NeurIPS checklist as a secondary transparency check

## Remaining work before the formal protocol

1. Freeze the exact task construction and exclusions in the primary analysis plan.
2. Freeze the final CNN architecture and its training configuration in a small pilot without interpreting the primary result.
3. Define the primary statistical estimand and patient-level uncertainty procedure.
4. Write the formal protocol and statistical analysis plan.
5. Register the study before the primary result is inspected.
