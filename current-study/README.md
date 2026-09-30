# Biomedical ML Workflow Fidelity in Free Consumer General-Purpose LLMs

This is the active research workspace for a controlled study of completely free consumer-facing general-purpose online LLM configurations executing a fixed biomedical machine-learning analysis.

The study asks whether changing the analyst-facing workflow changes end-to-end reference-faithful completion when the biomedical task, execution environment, zero-cost consumer access envelope and evaluation criteria are held constant.

The authoritative design is [STUDY PROTOCOL.md](STUDY%20PROTOCOL.md).

## Start here

**Study design**  
[STUDY PROTOCOL.md](STUDY%20PROTOCOL.md) is the authoritative integrated protocol.

**Research question and prior art**  
[01 LITERATURE REVIEW.md](01%20LITERATURE%20REVIEW.md) gives the scientific background.  
[02 PRIOR ART AND GAP ANALYSIS.md](02%20PRIOR%20ART%20AND%20GAP%20ANALYSIS.md) defines the current gap and its boundaries.  
[03 LITERATURE SEARCH AND EVIDENCE METHODS.md](03%20LITERATURE%20SEARCH%20AND%20EVIDENCE%20METHODS.md) records how the evidence boundary was built.

**Biomedical target**  
[04 BIOMEDICAL LITERATURE REVIEW.md](04%20BIOMEDICAL%20LITERATURE%20REVIEW.md) and [05 MACHINE LEARNING METHODS REVIEW.md](05%20MACHINE%20LEARNING%20METHODS%20REVIEW.md) establish the biomedical and ML basis.  
[08 REFERENCE BIOMEDICAL ANALYSIS PROTOCOL.md](08%20REFERENCE%20BIOMEDICAL%20ANALYSIS%20PROTOCOL.md) defines the fixed computational target.  
[REFERENCE DATA AUDIT.md](REFERENCE%20DATA%20AUDIT.md) preserves the empirical PTB-XL metadata and waveform checks carried forward from the archived study.

**LLM workflow experiment**  
[06 LLM WORKFLOW METHODS REVIEW.md](06%20LLM%20WORKFLOW%20METHODS%20REVIEW.md) covers prior methodological evidence.  
[07 CONSUMER LLM ELIGIBILITY SPECIFICATION.md](07%20CONSUMER%20LLM%20ELIGIBILITY%20SPECIFICATION.md) defines the access population.  
[09 LLM WORKFLOW EXPERIMENTAL PROTOCOL.md](09%20LLM%20WORKFLOW%20EXPERIMENTAL%20PROTOCOL.md) and [10 WORKFLOW CONDITIONS AND ABLATION PLAN.md](10%20WORKFLOW%20CONDITIONS%20AND%20ABLATION%20PLAN.md) define the conditions.  
[PROMPT PACKAGE.md](PROMPT%20PACKAGE.md) contains the frozen W0-W5 prompt text.

**Evaluation and execution records**  
[11 SCIENTIFIC FIDELITY EVALUATION FRAMEWORK.md](11%20SCIENTIFIC%20FIDELITY%20EVALUATION%20FRAMEWORK.md) defines scientific adjudication.  
[12 STATISTICAL ANALYSIS PLAN.md](12%20STATISTICAL%20ANALYSIS%20PLAN.md) defines the primary analysis.  
[13 RESOURCE ACCOUNTING AND ACCESSIBILITY ANALYSIS.md](13%20RESOURCE%20ACCOUNTING%20AND%20ACCESSIBILITY%20ANALYSIS.md), [14 REPRODUCIBILITY AND COMPUTATIONAL ENVIRONMENT.md](14%20REPRODUCIBILITY%20AND%20COMPUTATIONAL%20ENVIRONMENT.md), [15 DATA PROVENANCE AND DATA DICTIONARY.md](15%20DATA%20PROVENANCE%20AND%20DATA%20DICTIONARY.md), [16 FAILURE TAXONOMY AND ERROR AUDIT.md](16%20FAILURE%20TAXONOMY%20AND%20ERROR%20AUDIT.md), and [17 PROMPT AND INTERACTION REGISTRY.md](17%20PROMPT%20AND%20INTERACTION%20REGISTRY.md) define supporting controls.

**Research transparency**  
[AI USE.md](AI%20USE.md) records the project's AI-assistance boundary and verification practice.  
[SAMPLE SIZE SIMULATION.md](SAMPLE%20SIZE%20SIMULATION.md) documents the design-support simulation.

## Current state

Primary LLM data collection has not begun.

The reference analysis has not yet completed the R0 through R6 execution gate, so the numerical reference-agreement criteria are not yet frozen.

The eligible configuration set will be established from the frozen consumer-eligibility criteria and direct access audit before primary collection.

## Archived research

The original ECG amplitude representation study is preserved in [../archive/ecg-amplitude-normalization/](../archive/ecg-amplitude-normalization/).

It remains the provenance source for the fixed biomedical task and for several implementation and data-audit components. It is not the active scientific question.
