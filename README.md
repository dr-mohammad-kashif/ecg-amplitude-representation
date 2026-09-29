# ECG amplitude representation

I started this study because I became interested in a small assumption that is easy to leave unquestioned in ECG machine learning. Amplitude normalization is often treated as a routine preprocessing step. I want to know whether it is actually neutral.

I am using the PTB-XL dataset and comparing an original ECG representation with a defined amplitude-normalized representation across a small number of diagnostic tasks. I am less interested in which version gives the better score. I want to see whether changing the representation changes the information available to a model, and whether that differs from one task to another.

## Where I am now

I have finished the first scientific literature pass and the main methodological literature reconnaissance. I have not run the data audit or the main analysis yet, so there are no results here.

I am now checking the actual PTB-XL label structure and the model input representation before I lock the formal protocol.

## Who is working on it

I am leading the study.

Zaid Wani is joining me as a research collaborator and will independently reproduce the primary analysis once the first version is stable.

## The question

Does ECG amplitude normalization remove or alter information relevant to some diagnostic tasks, and is that effect different across tasks?

## Why I chose it

Normalization may help, do very little, or remove information that matters for a particular task. I want to see which of those possibilities the data support.

That question led me to the current study design.

## What I plan to do

I will

- compare an original signal representation with one defined amplitude-normalized representation
- keep the diagnostic task, model, input handling and evaluation setup fixed when comparing the two representations
- use patient-aware train, validation and test splits
- look at AUROC, AUPRC and calibration instead of relying on accuracy alone
- inspect errors and run a small number of reasoned robustness checks
- have Zaid reproduce the main comparison from the repository

I am freezing the task definitions, normalization rule and model input representation before running the primary comparison.

## Files

[research_question.md](research_question.md) contains the question and the working hypotheses.

[analysis_plan.md](analysis_plan.md) contains the current experimental plan.

[literature_review.md](literature_review.md) records the scientific and clinical literature that shaped the research question.

[methods_literature_review.md](methods_literature_review.md) records the evidence used to design the study and justify methodological choices.

[methods_review.md](methods_review.md) records the current methodological synthesis and unresolved decisions.

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

I am keeping the analysis in small steps so I can rerun it from the repository instead of relying on a single notebook or an undocumented sequence of commands.
