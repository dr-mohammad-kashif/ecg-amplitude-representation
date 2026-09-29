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

### A. Verify the implementation

- run the repository unit tests
- run the waveform smoke test on a supplied records100 file
- verify the metadata audit script reproduces the frozen cohort counts
- verify runtime and memory use on the available hardware

### B. Register and freeze the study record

- review PROTOCOL.md
- review STATISTICAL_ANALYSIS_PLAN.md
- record the final environment specification
- create the preregistration record before inspecting the primary test result

### C. Run the primary analysis

- prepare the full PTB-XL v1.0.3 records100 data locally
- verify all required waveform reads before training
- train the four primary task-condition models with seed 1
- save validation checkpoints and test predictions
- run the primary patient-level bootstrap
- report the prespecified secondary metrics

### D. Run prespecified sensitivity analyses

- per-lead record-wise z-score
- unthresholded superclass labels
- training seeds 1, 2 and 3

### E. Reproduce and report

- independent Zaid reproduction
- reconcile any discrepancies
- final results
- final report
- release metadata when there is a meaningful citable version

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
