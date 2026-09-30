# Prompt Package

Version 1.0, 30 September 2026.

## 1. Purpose

This package contains the canonical prompt text for workflow conditions W0 through W5.

The scientific target, information-exposure boundary, execution environment, human role, interaction ceiling, repair rules, and terminal states are defined in the integrated Study Protocol and companion documents.[1-4]

The package fixes the wording used for primary collection. Pilot wording is not reused under a primary version.

Prompt formulation is treated as part of the experimental configuration because prior healthcare data-analysis work has shown that changes in prompt specification can alter analytical performance.[5] TRIPOD-LLM also requires transparent reporting of prompting and evaluation settings.[6]

## 2. Common operational rules

The following rules apply to every prompt.

The LLM must:

- use only the supplied study package and permitted execution evidence;
- use the standardized execution environment;
- follow the locked biomedical protocol;
- preserve required artifacts and provenance;
- distinguish completed computation from proposed computation;
- report failures and unresolved issues;
- avoid inventing numerical outputs;
- avoid external web search, retrieval, connected applications, or other uncontrolled information sources.

The prompts do not authorize scientific intervention by the human operator.

The human may perform only the mechanical actions defined in the Study Protocol.[2]

The maximum interaction envelope is 32 LLM response turns per run for every workflow condition W0 through W5.

## 3. W0 prompt

### W0-INITIAL-1.0

~~~text
Perform the complete analysis specified in the supplied study package.

Use the designated execution environment and preserve the required analysis artifacts, execution evidence, and final report.

Use only the supplied study materials and permitted execution evidence. Do not use external web search, retrieval, connected applications, or prior study information.

Do not invent results. If the analysis cannot be completed or a required component is unresolved, state that explicitly and preserve the relevant evidence.

Proceed within the permitted interaction and resource envelope.
~~~

W0 intentionally does not enumerate an analytical workflow in the initial instruction. The scientific information remains available in the study package.

## 4. W1 prompt

### W1-INITIAL-1.0

~~~text
Perform the complete biomedical machine learning analysis specified in the supplied study package.

Conduct the work in this single consumer LLM context using the following sequence:

1. audit the dataset, source files, waveform structure, technical eligibility, and patient-aware fold information;
2. construct the HYP and MI cohorts using the prescribed label definitions and preserve a cohort and exclusion manifest;
3. implement the exact waveform representations, model architecture, training configuration, evaluation metrics, bootstrap procedures, and sensitivity analyses specified in the study package;
4. execute the analysis in the standardized execution environment and preserve generated code, configuration, execution logs, predictions, metrics, bootstrap outputs, and other required artifacts;
5. evaluate the results against the locked protocol and prepare the final scientific report with the required interpretation boundaries.

Use only the supplied study materials and permitted execution evidence. Do not use external web search, retrieval, connected applications, or prior study information.

Do not change the scientific specification. Do not introduce unrequested preprocessing, model changes, labels, statistical procedures, or exploratory analyses into the primary workflow.

Do not invent numerical results. Distinguish completed computation from planned or proposed computation.

If an execution error occurs, correct it only within the permitted run and preserve the error and repair history.

Complete the analysis within the permitted interaction and resource envelope.
~~~

## 5. W2 Stage 1 prompt

### W2-STAGE1-1.0

~~~text
You are responsible for Stage 1 of the assigned biomedical analysis workflow: data and provenance audit.

Using only the supplied study package and accessible study data, establish:

- dataset identity and version;
- required source files;
- waveform file structure;
- sampling frequency and dimensions;
- technical eligibility checks;
- patient-aware fold information;
- source fields required for downstream label construction;
- any unresolved data-access or integrity problems.

Create the required structured data-audit artifact and provenance record.

Do not construct the final model, select labels beyond the prescribed audit, or interpret biomedical performance.

Do not use external web search, retrieval, connected applications, or prior conversational history.

State unresolved issues explicitly.

Return the completed Stage 1 artifact and a concise handoff record for Stage 2.
~~~

## 6. W2 Stage 2 prompt

### W2-STAGE2-1.0

~~~text
You are responsible for Stage 2 of the assigned biomedical analysis workflow: cohort and label construction.

Use the supplied study package, the Stage 1 handoff artifact, and the permitted source data.

Construct the HYP versus NORM and MI versus NORM cohorts exactly according to the prescribed diagnostic likelihood rules.

Produce:

- target and NORM likelihood derivations;
- task-specific binary labels;
- technical eligibility status;
- inclusion and exclusion reasons;
- patient-aware split assignments;
- cohort and label manifests;
- explicit unresolved issues.

Do not alter the label rule because of class balance, model performance, or implementation difficulty.

Do not use reference numerical results or a hidden answer key.

Do not use external web search, retrieval, connected applications, or prior conversational history.

Return the completed Stage 2 artifacts and a structured handoff for Stage 3.
~~~

## 7. W2 Stage 3 prompt

### W2-STAGE3-1.0

~~~text
You are responsible for Stage 3 of the assigned biomedical analysis workflow: analysis implementation.

Use only the locked scientific specification, the approved Stage 1 and Stage 2 handoff artifacts, and the permitted execution environment.

Implement:

- the prescribed raw and normalized waveform representations;
- the fixed direct-waveform model architecture;
- the locked training configuration;
- the required evaluation metrics;
- the primary cross-task estimand;
- the patient-level reference bootstrap procedures;
- the prespecified sensitivity analyses.

Create the implementation manifest and all executable analysis artifacts required for Stage 4.

Do not change the scientific specification.

Do not use external web search, retrieval, connected applications, reference source code, reference numerical results, or previous LLM trajectories.

Preserve unresolved implementation issues rather than silently resolving them by changing the protocol.

Return the completed implementation artifacts and a structured handoff for Stage 4.
~~~

## 8. W2 Stage 4 prompt

### W2-STAGE4-1.0

~~~text
You are responsible for Stage 4 of the assigned biomedical analysis workflow: execution and evaluation.

Use the locked protocol, validated handoff artifacts, implementation files, and standardized execution environment.

Execute the prescribed analysis.

Capture and preserve:

- execution status;
- stdout and stderr;
- generated files;
- test predictions;
- AUROC;
- average precision;
- Brier score;
- calibration outputs;
- representation-specific effects;
- the primary cross-task contrast;
- bootstrap outputs;
- sensitivity-analysis outputs where completed.

Verify that the recorded outputs correspond to the code and execution that actually ran.

Do not invent or estimate missing numerical outputs.

Do not use external web search, retrieval, connected applications, reference numerical results, or previous LLM trajectories.

If an execution or implementation problem occurs, correct it only within the permitted run, preserve the initial failure, and re-execute the affected step.

Return the complete Stage 4 evidence package and a structured handoff for Stage 5.
~~~

## 9. W2 Stage 5 prompt

### W2-STAGE5-1.0

~~~text
You are responsible for Stage 5 of the assigned biomedical analysis workflow: interpretation and scientific reporting.

Use the locked protocol, the permitted Stage 1 through Stage 4 handoff artifacts, execution evidence, and computed results.

Prepare the final report.

The report must:

- state the task and representation comparison accurately;
- report the primary biomedical estimand and its uncertainty;
- distinguish AUROC, average precision, Brier score, and calibration;
- identify protocol deviations and unresolved failures;
- distinguish completed computation from unsupported claims;
- avoid causal or clinical-utility claims not established by the study;
- use NORM-labelled rather than healthy when describing the control phenotype;
- preserve the study's interpretation boundaries.

Do not change the analysis after observing the results.

Do not introduce unprespecified scientific claims.

Do not use external web search, retrieval, connected applications, reference numerical results, or prior LLM trajectories.

Return the final scientific report and terminal workflow status.
~~~

## 10. W3 self-audit prompt

### W3-AUDIT-1.0

~~~text
Act as the self-audit stage for the completed W2 workflow.

Treat the completed analysis as untrusted until checked against the locked study package and the preserved execution evidence.

Audit:

- dataset and provenance;
- cohort and labels;
- patient-aware split;
- waveform representation;
- model architecture;
- training configuration;
- evaluation and statistical procedures;
- primary estimand;
- numerical outputs;
- execution provenance;
- interpretation;
- reproducibility evidence.

Use the failure taxonomy codes where applicable.

Do not use a hidden reference answer key.

Do not use external web search, retrieval, connected applications, or prior study information.

For each finding, identify the evidence supporting it.

If a correctable issue remains, one bounded repair cycle is permitted. Repair only the identified issue, re-execute affected steps, and record the original error, repair, and post-repair status.

Do not convert an unresolved issue into a claim of success.

Return the audit record and terminal status.
~~~

## 11. W4 validation response prompt

### W4-VALIDATION-1.0

~~~text
Review the deterministic validation findings supplied for the completed W2 workflow.

Treat each reported finding as an observed validation failure that must be addressed without changing the locked scientific specification.

For each finding:

1. identify the affected artifact or analysis step;
2. determine whether the finding is valid from the supplied evidence;
3. correct the implementation only as permitted by the protocol;
4. re-execute the affected component when required;
5. re-run the applicable deterministic validation checks;
6. preserve the original failure and the repair history.

Do not use reference numerical results as a target.

Do not introduce a different scientific method because it appears preferable.

If the validation evidence is insufficient to resolve the issue, leave the issue unresolved and report it explicitly.

One bounded repair cycle is permitted.
~~~

## 12. W5 independent audit prompt

### W5-AUDIT-1.0

~~~text
Act as an independent audit context for the completed W2 workflow.

You did not perform the original analysis. Treat all prior outputs as untrusted evidence to be checked against the locked study package.

Audit the completed analysis for:

- data and cohort fidelity;
- label and split correctness;
- representation and preprocessing;
- model and training fidelity;
- statistical implementation;
- numerical provenance;
- execution evidence;
- interpretation;
- reproducibility evidence.

Use the failure taxonomy and identify the evidence supporting every finding.

Do not use a reference answer key.

Do not use external web search, retrieval, connected applications, or prior LLM trajectories outside the artifacts explicitly supplied to the audit condition.

If a repair is permitted, issue one bounded repair request. The affected analysis must then be re-executed and the repair status recorded.

Do not suppress an error because the final numerical result appears plausible.

Return the independent audit record and terminal status.
~~~

## 13. Repair instruction

### REPAIR-1.0

~~~text
Address only the finding identified in the supplied audit or validation record.

Do not change the locked scientific specification.

Make the smallest correction necessary to resolve the documented issue.

Preserve the original artifact and create a new versioned artifact for the repair.

Re-execute every affected analysis step.

Return:

- the corrected artifact;
- the execution evidence;
- the revalidation evidence where applicable;
- a concise statement of whether the finding is resolved.

Do not introduce unrelated changes.
~~~

## 14. Freeze and change control


Any change to prompt text requires:

- a new prompt version;
- a documented reason;
- identification of affected workflow conditions;
- confirmation of whether primary outcomes have already been observed;
- replacement or amendment of the primary study package only before primary collection unless a formal protocol amendment is approved.

The original prompt version remains archived.

## References

1. Study Protocol. study/STUDY PROTOCOL.md. Study repository.
2. LLM Workflow Experimental Protocol. study/09 LLM WORKFLOW EXPERIMENTAL PROTOCOL.md. Study repository.
3. Workflow Conditions and Ablation Plan. study/10 WORKFLOW CONDITIONS AND ABLATION PLAN.md. Study repository.
4. Prompt, Context and Interaction Registry. study/17 PROMPT AND INTERACTION REGISTRY.md. Study repository.
5. Ruta MR, Gaidici T, Irwin C, Lifshitz J. ChatGPT for Univariate Statistics: Validation of AI-Assisted Data Analysis in Healthcare Research. J Med Internet Res. 2025;27:e63550. doi:10.2196/63550.
6. Gallifant J, Afshar M, Ameen S, et al. The TRIPOD-LLM reporting guideline for studies using large language models. Nat Med. 2025;31(1):60-69. doi:10.1038/s41591-024-03425-5.
