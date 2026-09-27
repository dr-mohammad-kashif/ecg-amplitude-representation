# ECG amplitude representation

I started this study because I became interested in a small assumption that is easy to leave unquestioned in ECG machine learning. Amplitude normalization is often treated as a routine preprocessing step. I want to know whether it is actually neutral.

I am using the PTB-XL dataset and comparing an original ECG representation with a defined amplitude-normalized representation across a small number of diagnostic tasks. I am less interested in which version gives the better score. I want to see whether changing the representation changes the information available to a model, and whether that changes from one task to another.

## Where I am now

I have finished the first literature pass and written the initial analysis plan. I have not run the data audit or the main analysis yet, so there are no results here.

## Who is working on it

I am leading the study.

Zaid Wani is joining me as a research collaborator and will independently reproduce the primary analysis once the first version is stable.

## The question

Does ECG amplitude normalization remove or alter information relevant to some diagnostic tasks, and is that effect different across tasks?

## Why I chose it

Normalization may help, do very little, or remove information that matters for a particular task. I want to see which of those possibilities the data support.

That distinction is what led me to the current study design.

## What I plan to do

I will

- compare an original signal representation with one defined amplitude-normalized representation
- keep the diagnostic task, model and evaluation setup fixed when comparing the two representations
- use patient-aware train, validation and test splits
- look at AUROC, AUPRC and calibration rather than relying on accuracy alone
- inspect errors and run a small number of robustness checks
- have Zaid reproduce the main comparison from the repository

I am freezing the task definitions and normalization rule before running the primary comparison.

## Files

[research_question.md](research_question.md) contains the question and the working hypotheses.

[analysis_plan.md](analysis_plan.md) contains the current experimental plan.

[literature_review.md](literature_review.md) records what I read before settling on the study design and why each source was useful.

[references.md](references.md) contains the citations.

[data_provenance.md](data_provenance.md) records where the PTB-XL data come from and how I am handling the dataset.

[research_log.md](research_log.md) is where I am recording decisions and changes as the work develops.

[ai_notes.md](ai_notes.md) records where I use AI tools and what I check myself.

## Current evidence boundary

This is an ongoing study. I have not established that normalization improves or harms diagnostic performance, that one representation is clinically better, or that any future finding will generalize beyond the dataset and evaluation used here.

## Data

I am not storing the PTB-XL data in this repository. The dataset comes from PhysioNet. The version and source information are recorded in data_provenance.md.

## Reproducibility

I am keeping the analysis in small steps so that I can rerun it from the repository rather than relying on a single notebook or an undocumented sequence of commands.
