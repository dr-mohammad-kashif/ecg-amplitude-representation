# ECG amplitude representation

This study looks at a simple question in ECG machine learning. When amplitude normalization is treated as a routine preprocessing step, does it actually leave the information used for diagnosis unchanged?

The work uses the PTB-XL dataset and compares raw and normalized ECG representations across selected diagnostic tasks. The main interest is not to find a preprocessing method that gives the highest score. It is to test whether a preprocessing choice changes what the model can use, and whether that change depends on the task.

## Status

Research design and literature review are underway. No results are reported yet.

## Study team

Mohammad Kashif, study lead and primary researcher  
Zaid Wani, research collaborator

## Current question

Does ECG amplitude normalization remove or alter information relevant to some diagnostic tasks, and is that effect different across tasks?

## Why this question

Preprocessing choices are often treated as technical steps that can be applied before the actual analysis. That makes sense when the transformation is only removing nuisance variation. It becomes less straightforward when the quantity being changed may itself contain information relevant to a clinical task.

This study starts from that distinction and tests it rather than assuming it.

## Study plan

The current plan is to

- compare a raw signal representation with a defined amplitude-normalized representation
- evaluate the same diagnostic tasks under the same patient-level split and model settings
- examine discrimination and calibration rather than relying on accuracy alone
- inspect errors and test whether the main result is stable under a limited set of robustness checks
- have a second researcher reproduce the primary analysis from the repository

The exact tasks and preprocessing definition are being fixed in the analysis plan before the main comparison is run.

## Repository

`research_question.md` records the current question and working hypotheses.

`analysis_plan.md` contains the planned preprocessing, splitting, models, metrics and robustness checks.

`literature_review.md` records the work reviewed before the main analysis.

`DATA_PROVENANCE.md` records the PTB-XL version, source, access information and data handling decisions.

`RESEARCH_LOG.md` records decisions, failed approaches and changes made during the study.

`AI_USE.md` records where AI tools were used during research and coding and what was independently checked.

The code, notebooks and results folders will be populated as the analysis progresses.

## Evidence boundary

This repository is an ongoing study. It does not currently establish that normalization improves or harms diagnostic performance, that any representation is clinically superior, or that a particular finding generalizes beyond the data and evaluation used here.

## Data

The PTB-XL data are not stored in this repository. Instructions and provenance information will be kept separately in `DATA_PROVENANCE.md`.

## Reproducibility

The goal is to keep the analysis reproducible from the documented environment and code. Later releases will preserve the state of the work at major stages of the study.
