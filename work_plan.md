# Work plan

## What this file is for

I am using this file as the running map for the study. I want one place that tells me what has already been decided, what is still open, and what I need to do next.

This is not the study protocol. The protocol will be written only after the design questions below have been checked against the literature and the PTB-XL data.

## Current state

The repository is public and now contains separate scientific and methodological literature records.

The first scientific literature pass is complete.

The methodological literature reconnaissance is substantially complete for the major design questions.

The main analysis has not started.

No model result has been produced.

The next phase is the PTB-XL data audit and the final model input decision.

## Current research question

Does ECG amplitude normalization remove or alter information relevant to some diagnostic tasks, and is that effect different across tasks?

## Working hypothesis

The effect of normalization may not be identical across diagnostic tasks.

This remains a hypothesis. I will let the data and the planned analysis determine the result.

## Decisions already made

- Use PTB-XL version 1.0.3 from PhysioNet.
- Keep patient identity through data preparation.
- Use patient-aware evaluation.
- Start with raw versus one clearly defined normalized representation.
- Keep the model and evaluation procedure fixed when comparing representations.
- Treat HYP versus NORM and MI versus NORM as candidate tasks until the data audit is complete.
- Record label construction and exclusion rules before the primary comparison.
- Evaluate with AUROC, AUPRC and calibration where appropriate.
- Include error analysis and at least one reasoned robustness check.
- Do not add models or preprocessing variants just to make the result look stronger.
- Have Zaid independently reproduce the primary comparison after the first analysis is stable.
- Keep AI use documented, but do not treat AI output as scientific evidence.

## Evidence-supported candidates

These are not yet frozen protocol decisions.

### Normalization

A global record-wise z-score across retained leads and time points is currently the clearest primary candidate.

A record-wise per-lead z-score is currently the clearest sensitivity candidate.

### Uncertainty

A patient-level paired bootstrap is currently the strongest candidate because multiple ECG records can belong to one patient.

DeLong remains a candidate for the correlated AUROC comparison.

### Calibration

Calibration plot plus Brier score is the current simple secondary plan.

## Next research phase

### A. Audit the actual PTB-XL task structure

- inspect all label combinations
- quantify target and NORM overlaps
- count records and patients under candidate task definitions
- test the effect of reasonable pre-specified exclusion rules
- document unusable waveform cases
- check class balance
- decide the scientific unit of observation

### B. Decide the model input representation

This is now the main unresolved methodological issue.

- determine whether the waveform will be used directly or through a defined feature representation
- check computational feasibility of each option
- keep the same input construction for raw and normalized conditions
- avoid adding dimensionality reduction solely to make one representation work better
- decide whether logistic regression and random forest remain appropriate after the input is defined
- record the reason for the final choice

### C. Freeze preprocessing

- write the exact normalization formula
- specify record-local versus population-fitted parameters
- specify whether the transform is applied independently within each split
- define any handling of missing or unusable signal
- define the sensitivity normalization before the primary analysis

### D. Freeze the statistical target

- choose the primary task
- choose the primary model
- choose the primary outcome
- define the AUROC difference precisely
- define the patient-level bootstrap and interval method
- decide how AUPRC uncertainty will be reported
- define the calibration summary
- define what is primary versus secondary versus exploratory

### E. Write the protocol and SAP

Only after A-D are complete

- PROTOCOL.md
- STATISTICAL_ANALYSIS_PLAN.md
- preregistration record

### F. Then code and analyse

- reusable preprocessing functions
- validation tests
- primary analysis
- results
- error analysis
- reasoned robustness checks
- Zaid independent reproduction
- final report

## Current documents

- README.md
- research_question.md
- analysis_plan.md
- literature_review.md
- methods_literature_review.md
- methods_review.md
- literature_search.md
- references.md
- data_provenance.md
- research_log.md
- ai_notes.md
- requirements.txt
- .gitignore

## Future study documents

I expect the research record to grow as real work is completed.

- study protocol
- statistical analysis plan
- label specification
- data dictionary
- evidence extraction matrix if it becomes useful
- bias and leakage register if the design becomes complex enough to warrant it
- replication note
- tests
- results
- report
- release metadata when there is a meaningful citable version

I will add a document only when it has real content and a clear role.

## Writing and repository rules

The repository should read like a real working research record.

I write in first person when that is the natural way to describe what I did or decided.

I prefer concrete observations over polished summaries.

I do not add generic motivational language.

I do not add claims just to make the project sound more advanced.

I do not use em dashes.

I keep punctuation simple and avoid colon-heavy prose.

I avoid stock contrasts and neat wrap-up sentences when a direct sentence is clearer.

I do not turn ordinary decisions into dramatic methodological claims.

The documents should reflect the actual state of the work. A future plan is labelled as a plan. A result is reported only after it has been run and checked.

AI-use documentation stays brief and factual. It should record real assistance and verification, not become a long explanation of how AI was used.

## Context recovery rule

Before continuing the study in a new session, I should read this file, README.md, research_question.md, analysis_plan.md, literature_review.md, methods_literature_review.md, methods_review.md, literature_search.md, data_provenance.md, research_log.md and ai_notes.md.

Then I should check the latest git commit and the current file tree.

No methodological decision from an earlier session should be silently dropped. If a later decision changes an earlier one, record the change in research_log.md.

## Immediate next task

Audit PTB-XL version 1.0.3 and resolve the model input representation.

The formal protocol should be written only after those decisions are supported by the actual dataset and the literature.
