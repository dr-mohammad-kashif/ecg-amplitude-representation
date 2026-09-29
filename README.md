# ECG amplitude representation

I started this study because I became interested in a small assumption that is easy to leave unquestioned in ECG machine learning. Amplitude normalization is often treated as a routine preprocessing step. I want to know whether it is actually neutral.

I am using the PTB-XL dataset to compare the native ECG representation with a defined record-wise standardized representation across two diagnostic tasks. I am interested in whether the representation change produces a different predictive effect for HYP and MI when the model and evaluation setup are held fixed.

## Where I am now

I have finished the main scientific and methodological literature passes. The metadata and waveform integrity audits are complete. The primary analysis has not been run, so there are no model results here.

I have completed the PTB-XL metadata and label audit and a targeted waveform integrity audit. The primary input representation, label rule, model structure and statistical estimand are now frozen. The remaining work is implementation verification and formal protocol registration.

## Who is working on it

I am leading the study.

Zaid Wani is joining me as a research collaborator and will independently reproduce the primary analysis once the first version is stable.

## The question

Under a fixed direct-waveform model, does global record-wise z-score standardization change ECG classification performance differently for PTB-XL hypertrophy and myocardial infarction phenotypes?

## Why I chose it

I am testing one specific representation change rather than normalization in general.

That question led me to the current study design.

## What I plan to do

I will

- compare an original signal representation with one defined amplitude-normalized representation
- keep the diagnostic task, model, input handling and evaluation setup fixed when comparing the two representations
- use patient-aware train, validation and test splits
- look at AUROC, AUPRC and calibration instead of relying on accuracy alone
- inspect errors and run a small number of reasoned robustness checks
- have Zaid reproduce the main comparison from the repository

The label rule, normalization, waveform representation, model structure and primary estimand are now frozen before the primary comparison.

## Files

[research_question.md](research_question.md) contains the question and the working hypotheses.

[data_audit.md](data_audit.md) records the PTB-XL metadata and label audit performed before the primary analysis.
[LABEL_SPECIFICATION.md](LABEL_SPECIFICATION.md) contains the frozen binary task definitions.


[analysis_plan.md](analysis_plan.md) contains the current experimental plan.
[PROTOCOL.md](PROTOCOL.md) contains the prespecified study protocol.

[STATISTICAL_ANALYSIS_PLAN.md](STATISTICAL_ANALYSIS_PLAN.md) contains the statistical analysis specification.


[literature_review.md](literature_review.md) records the scientific and clinical literature that shaped the research question.

[methods_literature_review.md](methods_literature_review.md) records the evidence used to design the study and justify methodological choices.

[methods_review.md](methods_review.md) records the current methodological synthesis and final design choices.

[literature_search.md](literature_search.md) records the current search process and what changed because of it.

[work_plan.md](work_plan.md) is my running map of decisions, open questions and next steps.

[references.md](references.md) contains the citations.

[data_provenance.md](data_provenance.md) records where the PTB-XL data come from and how I am handling the dataset.

[research_log.md](research_log.md) is where I am recording decisions and changes as the work develops.

[ai_notes.md](ai_notes.md) records where I use AI tools and what I check myself.

## Current evidence boundary

This is an ongoing study. I have not established that normalization improves or harms diagnostic performance, that one representation is clinically better, or that any future finding will generalize beyond the dataset and evaluation used here.

## Data

I am not storing the PTB-XL data in this repository. The study uses PTB-XL version 1.0.3 from PhysioNet.

[Dataset page](https://physionet.org/content/ptb-xl/1.0.3/)

[Download the version 1.0.3 ZIP](https://physionet.org/content/ptb-xl/get-zip/1.0.3/)

The version, source files and provenance details are recorded in data_provenance.md.

## Citation

This repository includes a CITATION.cff file for machine-readable citation metadata. Formal study documents use numbered Vancouver-style references following biomedical citation conventions.

## Reproducibility

I am keeping the analysis in small steps so I can rerun it from the repository instead of relying on a single notebook or an undocumented sequence of commands. The current implementation includes reusable label and preprocessing functions, a fixed CNN definition, unit tests and a waveform smoke test.
