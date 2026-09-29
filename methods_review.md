# Methods review

I am using this document to collect the methodological decisions that can change the design of the ECG study. It is a synthesis of the evidence, not the full literature record.

The detailed evidence is now recorded in [methods_literature_review.md](methods_literature_review.md).

## Current methodological position

The study is a secondary-data computational study using the PTB-XL research dataset. Secondary-data guidance makes it important to define the data flow, unit of analysis, label construction, exclusions and analysis decisions explicitly before the main result.

The current methodological evidence also changes how I think about normalization. Normalization is not one operation. Record-local global z-score, record-local per-lead z-score, min-max transformations and population-fitted transformations answer different questions.

The clearest current candidate for the primary representation comparison is a global record-wise z-score applied across all retained leads and time points within each record. A record-wise per-lead z-score is a useful sensitivity candidate because it removes lead-specific scale as well as overall record scale. I am not freezing either condition until the data audit and model input decision are complete.

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

PTB-XL is multilabel. HYP, MI, NORM and other diagnostic superclasses can overlap.

The data audit therefore has to quantify label combinations before the binary tasks are frozen. I do not want to define the positive and negative groups after seeing model performance.

## Leakage and data splitting

The primary split should remain patient-aware.

Any population-fitted preprocessing must be fit on training data and then applied to validation and test data. A record-local transformation needs to be described explicitly because its parameters are derived from the record itself.

The study should distinguish this from preprocessing that shares information across records.

## Paired evaluation and uncertainty

The raw and normalized representations use the same underlying held-out records, so the performance comparison is paired.

DeLong is a candidate method for the correlated AUROC comparison. A patient-level bootstrap is also a strong candidate because PTB-XL can contain multiple records for one patient.

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

The data audit confirmed that the study can use the official 100 Hz waveform version as a direct 12-lead input.

The current candidate is a small fixed 1D convolutional model operating directly on the 100 Hz waveform. This keeps the representation comparison close to the signal and avoids a feature-engineering stage that could itself alter amplitude information.

This is still a candidate until the waveform files are inspected and the computational cost is measured. Logistic regression and random forest remain possible secondary baselines only if a principled compact feature representation is defined.

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

1. Inspect the waveform files and signal quality.
2. Decide the model input representation.
3. Freeze the normalization definition.
4. Freeze the task construction and exclusions.
5. Freeze the primary model and evaluation procedure.
6. Define the patient-level uncertainty procedure.
7. Write the formal protocol and statistical analysis plan.
8. Register the study before the primary result is inspected.
