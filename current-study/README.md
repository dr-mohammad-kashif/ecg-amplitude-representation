# Biomedical ML Workflow Fidelity

This is the active research workspace for a controlled study of general-purpose online LLMs executing a fixed biomedical machine-learning analysis.

The study asks whether changing the analyst-facing workflow changes end-to-end reference-faithful completion when the biomedical task, execution environment, access envelope and evaluation criteria are held constant.

The authoritative design is [STUDY PROTOCOL.md](STUDY%20PROTOCOL.md).

## Start here

[00 STUDY INDEX.md](00%20STUDY%20INDEX.md) maps the study and the pre-primary gates.

[01 LITERATURE REVIEW.md](01%20LITERATURE%20REVIEW.md) summarizes the broader scientific and methodological evidence.

[02 PRIOR ART AND GAP ANALYSIS.md](02%20PRIOR%20ART%20AND%20GAP%20ANALYSIS.md) records the current prior-art boundary and the remaining research gap.

[03 LITERATURE SEARCH AND EVIDENCE METHODS.md](03%20LITERATURE%20SEARCH%20AND%20EVIDENCE%20METHODS.md) records the search construction and evidence-handling rules.

[04 BIOMEDICAL LITERATURE REVIEW.md](04%20BIOMEDICAL%20LITERATURE%20REVIEW.md) and [05 MACHINE LEARNING METHODS REVIEW.md](05%20MACHINE%20LEARNING%20METHODS%20REVIEW.md) cover the biomedical and ML foundations.

[06 LLM WORKFLOW METHODS REVIEW.md](06%20LLM%20WORKFLOW%20METHODS%20REVIEW.md) covers prior work on scientific LLM workflows and process-level evaluation.

[07 CONSUMER LLM ELIGIBILITY SPECIFICATION.md](07%20CONSUMER%20LLM%20ELIGIBILITY%20SPECIFICATION.md) defines the eligible consumer-access population.

[08 REFERENCE BIOMEDICAL ANALYSIS PROTOCOL.md](08%20REFERENCE%20BIOMEDICAL%20ANALYSIS%20PROTOCOL.md) defines the fixed biomedical computational target.

[REFERENCE DATA AUDIT.md](REFERENCE%20DATA%20AUDIT.md) preserves the empirical PTB-XL data and waveform checks carried forward from the archived study.

[09 LLM WORKFLOW EXPERIMENTAL PROTOCOL.md](09%20LLM%20WORKFLOW%20EXPERIMENTAL%20PROTOCOL.md) and [10 WORKFLOW CONDITIONS AND ABLATION PLAN.md](10%20WORKFLOW%20CONDITIONS%20AND%20ABLATION%20PLAN.md) define the experimental conditions.

[11 SCIENTIFIC FIDELITY EVALUATION FRAMEWORK.md](11%20SCIENTIFIC%20FIDELITY%20EVALUATION%20FRAMEWORK.md), [12 STATISTICAL ANALYSIS PLAN.md](12%20STATISTICAL%20ANALYSIS%20PLAN.md), [13 RESOURCE ACCOUNTING AND ACCESSIBILITY ANALYSIS.md](13%20RESOURCE%20ACCOUNTING%20AND%20ACCESSIBILITY%20ANALYSIS.md), [14 REPRODUCIBILITY AND COMPUTATIONAL ENVIRONMENT.md](14%20REPRODUCIBILITY%20AND%20COMPUTATIONAL%20ENVIRONMENT.md), [15 DATA PROVENANCE AND DATA DICTIONARY.md](15%20DATA%20PROVENANCE%20AND%20DATA%20DICTIONARY.md), [16 FAILURE TAXONOMY AND ERROR AUDIT.md](16%20FAILURE%20TAXONOMY%20AND%20ERROR%20AUDIT.md), and [17 PROMPT AND INTERACTION REGISTRY.md](17%20PROMPT%20AND%20INTERACTION%20REGISTRY.md) define the evaluation and execution record.

[AI USE.md](AI%20USE.md) records the project's AI-assistance boundary and verification practice.

[PROMPT PACKAGE.md](PROMPT%20PACKAGE.md) contains the frozen W0-W5 prompt text.

[SAMPLE SIZE SIMULATION.md](SAMPLE%20SIZE%20SIMULATION.md) documents the design-support simulation.

## Current state

Primary LLM data collection has not begun.

The reference analysis has not yet completed the R0 through R6 execution gate, so the numerical reference-agreement criteria are not yet frozen.

The eligible configuration set will be established from the frozen consumer-eligibility criteria and direct access audit before primary collection.

## Archived research

The original ECG amplitude representation study is preserved in [../archive/ecg-amplitude-normalization/](../archive/ecg-amplitude-normalization/).

It remains the provenance source for the fixed biomedical task and for several implementation and data-audit components. It is not the active scientific question.
