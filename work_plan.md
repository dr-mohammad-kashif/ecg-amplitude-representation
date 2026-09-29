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

The metadata and label audit is complete for the uploaded PTB-XL v1.0.3 files.

A targeted waveform integrity audit is complete, and the primary waveform representation has been selected.

## Current research question

Does ECG amplitude normalization remove or alter information relevant to some diagnostic tasks, and is that effect different across tasks?

## Working hypothesis

The effect of normalization may not be identical across diagnostic tasks.

This remains a hypothesis. I will let the data and the planned analysis determine the result.

## Frozen design decisions

- Use PTB-XL version 1.0.3 from PhysioNet.
- Preserve patient identity throughout preparation and evaluation.
- Use patient-aware folds 1 to 8 for training, 9 for validation and 10 for held-out testing.
- Compare the native 100 Hz waveform with one global record-wise z-score representation.
- Use HYP versus NORM and MI versus NORM as the two prespecified phenotype tasks.
- Apply the same >=50% SCP likelihood threshold to target and NORM labels.
- Retain target-plus-NORM records as target-positive and exclude records reaching neither threshold.
- Use a compact direct-waveform 1D CNN with no internal normalization layers.
- Keep architecture, training procedure, input handling and evaluation data fixed between raw and standardized conditions.
- Use a patient-level paired percentile bootstrap with 5,000 resamples for primary uncertainty.
- Use the cross-task contrast of AUROC changes as the primary estimand.
- Keep unthresholded label construction, per-lead normalization and three-seed training stability as prespecified sensitivity analyses.
- Report AUROC, average precision, prevalence and Brier score, with calibration plots as secondary analysis.
- Do not add analyses because they produce a more favourable result.
- Have Zaid independently reproduce the primary analysis from a clean repository state.
## Next research phase

### A. Freeze the primary task construction

- confirm the target-present versus NORM-present rule
- confirm the handling of target plus NORM overlap
- record exclusions for records with neither label
- record the final record and patient counts

### B. Freeze the CNN implementation

- choose the smallest architecture that can learn the direct waveform representation without introducing engineered features
- fix optimizer, learning-rate schedule, batch size, epochs and early-stopping rule
- fix random seeds and model-selection rule
- confirm that the same configuration is used for raw and normalized conditions

### C. Freeze the statistical target

- choose the primary estimand
- define the AUROC difference precisely
- define the patient-level paired bootstrap and interval method
- decide how AUPRC uncertainty will be reported
- define the calibration summary
- define what is primary versus secondary versus exploratory

### D. Write the protocol and SAP

Only after A-C are complete

- PROTOCOL.md
- STATISTICAL_ANALYSIS_PLAN.md
- preregistration record

### E. Then code and analyse

- reusable preprocessing functions
- validation tests
- primary training and evaluation
- results
- error analysis
- reasoned robustness checks
- Zaid independent reproduction
- final report

- choose the primary task
- choose the primary model
- choose the primary outcome
- define the AUROC difference precisely
- define the patient-level bootstrap and interval method
- decide how AUPRC uncertainty will be reported
- define the calibration summary
- define what is primary versus secondary versus exploratory

### F. Write the protocol and SAP

Only after A-E are complete

- PROTOCOL.md
- STATISTICAL_ANALYSIS_PLAN.md
- preregistration record

### G. Then code and analyse

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
- data_audit.md
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
- src/
- tests/
- scripts/

## Future study documents

I expect the research record to grow as real work is completed.

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

Before continuing the study in a new session, I should read this file, README.md, research_question.md, analysis_plan.md, literature_review.md, methods_literature_review.md, methods_review.md, literature_search.md, data_provenance.md, data_audit.md, research_log.md and ai_notes.md.

Then I should check the latest git commit and the current file tree.

No methodological decision from an earlier session should be silently dropped. If a later decision changes an earlier one, record the change in research_log.md.

## Immediate next task

Implement and unit-test the frozen pipeline, then run a train-and-validation smoke test without using test performance for selection.

The formal protocol should be written after those decisions are stable.
