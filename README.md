# ECG amplitude representation

I started this study because I became interested in a small assumption that is easy to leave unquestioned in ECG machine learning. Amplitude normalization is often treated as a routine preprocessing step. I want to know whether it is actually neutral.

I am using the PTB-XL dataset to compare the native ECG representation with a defined record-wise standardized representation across two diagnostic tasks. I am interested in whether the representation change produces a different predictive effect for HYP and MI when the model and evaluation setup are held fixed.

## Where I am now

I have finished the main scientific and methodological literature passes. The metadata and waveform integrity audits are complete. The primary analysis has not been run, so there are no model results here.

I have completed the PTB-XL metadata and label audit and a targeted waveform integrity audit. The primary input representation, label rule, model structure and statistical estimand are now frozen. The remaining work is implementation verification and preregistration.

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

- compare the native 100 Hz waveform with one global record-wise z-score representation
- hold the task, model, training setup and held-out evaluation data fixed between representations
- use the official patient-aware folds
- estimate the task interaction in AUROC change with a patient-level paired bootstrap
- report average precision, Brier score and calibration as secondary measures
- run the prespecified normalization, label-definition and seed sensitivity analyses
- have Zaid independently reproduce the primary analysis

The label rule, normalization, waveform representation, model structure and primary estimand are now frozen before the primary comparison.

## Files

[02 RESEARCH QUESTION.md](02%20RESEARCH%20QUESTION.md) contains the question and the working hypotheses.

[08 DATA AUDIT.md](08%20DATA%20AUDIT.md) records the PTB-XL metadata and label audit performed before the primary analysis.
[09 LABEL SPECIFICATION.md](09%20LABEL%20SPECIFICATION.md) contains the frozen binary task definitions.


[10 ANALYSIS PLAN.md](10%20ANALYSIS%20PLAN.md) contains the current experimental plan.
[01 STUDY PROTOCOL.md](01%20STUDY%20PROTOCOL.md) contains the prespecified study protocol.

[11 STATISTICAL ANALYSIS PLAN.md](11%20STATISTICAL%20ANALYSIS%20PLAN.md) contains the statistical analysis specification.


[03 LITERATURE REVIEW.md](03%20LITERATURE%20REVIEW.md) records the scientific and clinical literature that shaped the research question.

[05 METHODS LITERATURE REVIEW.md](05%20METHODS%20LITERATURE%20REVIEW.md) records the evidence used to design the study and justify methodological choices.

[06 METHODS REVIEW.md](06%20METHODS%20REVIEW.md) records the current methodological synthesis and final design choices.

[04 LITERATURE SEARCH.md](04%20LITERATURE%20SEARCH.md) records the current search process and what changed because of it.

[14 WORK PLAN.md](14%20WORK%20PLAN.md) is my running map of decisions, open questions and next steps.

[15 REFERENCES.md](15%20REFERENCES.md) contains the citations.

[07 DATA PROVENANCE.md](07%20DATA%20PROVENANCE.md) records where the PTB-XL data come from and how I am handling the dataset.

[13 RESEARCH LOG.md](13%20RESEARCH%20LOG.md) is where I am recording decisions and changes as the work develops.

[16 AI NOTES.md](16%20AI%20NOTES.md) records where I use AI tools and what I check myself.

## Current evidence boundary

This is an ongoing study. I have not established that normalization improves or harms diagnostic performance, that one representation is clinically better, or that any future finding will generalize beyond the dataset and evaluation used here.

## Data

I am not storing the PTB-XL data in this repository. The study uses PTB-XL version 1.0.3 from PhysioNet.

[Dataset page](https://physionet.org/content/ptb-xl/1.0.3/)

[Download the version 1.0.3 ZIP](https://physionet.org/content/ptb-xl/get-zip/1.0.3/)

The version, source files and provenance details are recorded in 07 DATA PROVENANCE.md.

## Citation

This repository includes a CITATION.cff file for machine-readable citation metadata. Formal study documents use numbered Vancouver-style references following biomedical citation conventions.

## Reproducibility

I am keeping the analysis in small steps so I can rerun it from the repository instead of relying on a single notebook or an undocumented sequence of commands. The current implementation includes reusable label and preprocessing functions, a fixed CNN definition, unit tests and a waveform smoke test.
