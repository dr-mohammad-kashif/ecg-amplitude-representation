# Work plan

## What this file is for

I am using this file as the running map for the study. I want one place that tells me what has already been decided, what is still open, and what I need to do next.

This is not the study protocol. The protocol will be written only after the design questions below have been checked against the literature and the PTB-XL data.

## Current state

The repository is public and contains the first research question, analysis plan, literature review, methodological review, literature search record, data provenance note, research log, AI-use note, requirements file, and gitignore.

The first literature pass is complete.

The main analysis has not started.

No model result has been produced.

The next phase is methodological groundwork.

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
- Start with simple models before considering more complex models.
- Treat HYP versus NORM and MI versus NORM as candidate tasks until the data audit is complete.
- Record label construction and exclusion rules before the primary comparison.
- Evaluate with AUROC, AUPRC and calibration where appropriate.
- Include error analysis and at least one reasoned robustness check.
- Do not add models or preprocessing variants just to make the result look stronger.
- Have Zaid independently reproduce the primary comparison after the first analysis is stable.
- Keep AI use documented, but do not treat AI output as scientific evidence.

## Next research phase

Before I lock the protocol, I need to investigate the study design itself.

### A. Define the scientific target

- What exactly should count as information preservation?
- Is the study about numerical signal preservation, morphological preservation, task-relevant information, or several of these?
- What can be measured without making the study much larger than it needs to be?
- What claims would each measure support?

### B. Define the preprocessing question

- Which normalization method is most defensible for the primary comparison?
- Should normalization be record-wise, lead-wise, or use another scheme?
- Which properties of the original signal change under each option?
- Which choices can cause leakage?
- Which normalization choices are common enough in ECG machine learning to make the study useful?

### C. Define the diagnostic tasks

- What exactly do the PTB-XL HYP and NORM labels mean?
- What exactly do the MI and NORM labels mean?
- How should overlapping diagnostic labels be handled?
- What records should be excluded?
- Do the candidate tasks have enough usable data after the label rules are applied?
- Are there task definitions that are cleaner than the current candidates?

### D. Define the experimental design

- What is the unit of observation?
- What stays fixed across raw and normalized comparisons?
- What is the primary model?
- What is the primary outcome?
- What is the primary estimand?
- What uncertainty method is appropriate?
- What should be pre-specified and what can remain exploratory?
- What is the minimum robustness analysis that would materially improve the study?

### E. Check research quality and reporting standards

Review the parts of the following that actually fit this study

- TRIPOD+AI
- PROBAST+AI
- STROBE
- SPIRIT 2025 where its protocol principles are relevant
- NeurIPS research checklist for machine learning reproducibility and transparency
- FAIR principles for data and research objects
- published guidance for statistical analysis plans in observational and secondary-data work

I will not claim compliance with a guideline that was designed for a different study type. I will use relevant items as design and reporting checks.

### F. Literature search method

Build a transparent record of

- databases and search engines used
- search dates
- exact search strings
- inclusion rules
- exclusion rules
- citation chaining
- papers added after the first pass
- why a paper changed the design or was not needed

Do not call this a systematic review unless the search and screening process actually meets the requirements for one.

### G. AI-assisted research

Review evidence on

- AI-assisted literature discovery
- screening
- extraction
- citation checking
- coding
- analysis support
- hallucination and citation errors
- human verification
- audit trails
- speed versus accuracy

The goal is a fast workflow with human control and source verification. The study should not assume that AI is more accurate than a human across the whole research process.

### H. Reproducibility

Plan

- exact environment capture
- package versions
- random seeds where relevant
- reusable preprocessing code
- tests
- raw versus derived data boundaries
- repository versioning
- preregistration
- independent reproduction
- later archival release

## Current documents

- README.md
- research_question.md
- analysis_plan.md
- literature_review.md
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
- evidence extraction matrix
- bias and leakage register
- reporting standards matrix
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

Before continuing the study in a new session, I should read this file, README.md, research_question.md, analysis_plan.md, literature_review.md, methods_review.md, literature_search.md, data_provenance.md, research_log.md and ai_notes.md.

Then I should check the latest git commit and the current file tree.

No methodological decision from an earlier session should be silently dropped. If a later decision changes an earlier one, record the change in research_log.md.

## Immediate next task

Finish the methodological literature reconnaissance before writing the formal study protocol.

The protocol should be a result of that work, not a template written first and justified later.
