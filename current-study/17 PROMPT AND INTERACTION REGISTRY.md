# Prompt, Context and Interaction Registry

Status: Draft interaction-registry specification
Version: 0.1
Month: September 2026
Study phase: Preprotocol

## 1. Purpose

The interaction registry records how each eligible LLM configuration actually received, processed and returned the experimental workflow.

The registry is not a transcript dump. It is a controlled experimental record linking:

- the assigned workflow condition;
- the LLM configuration and access epoch;
- prompt versions;
- context boundaries;
- files and artifacts exposed;
- execution evidence returned to the model;
- repairs and audits;
- human actions;
- terminal state;
- fidelity and reproducibility records.

Prompt formulation and interaction structure are experimental variables in this study. Published healthcare data-analysis work has shown that changing prompt specificity can materially change statistical-analysis accuracy, while TRIPOD-LLM calls for transparent reporting of LLM identity, prompts, human oversight, evaluation procedures and reproducibility.[1,2]

The registry therefore preserves the experimental interaction as a versioned research object rather than treating the final response as the only relevant observation.

## 2. Relationship to other study documents

The registry is subordinate to the frozen scientific specification and does not redefine them.

- The consumer eligibility specification defines which LLM configurations can enter the primary population.[3]
- The LLM workflow protocol defines the permitted workflow mechanics.[4]
- The workflow conditions document defines W0 through W5 and their intended contrasts.[5]
- The resource plan defines observable interaction-resource variables.[6]
- The reproducibility plan defines computational and configuration provenance.[7]
- The data-provenance document defines source and derived data lineage and information exposure.[8]
- The failure taxonomy defines terminal states, error classes and repair records.[9]
- The statistical analysis plan defines how run outcomes are analyzed.[10]

The integrated study protocol will eventually provide the single front-facing synthesis. This registry remains the detailed operational record.

## 3. Unit of registration

The primary registry unit is the **run**.

A run is one assigned workflow attempt for one LLM configuration under one defined condition and one access epoch.

A run can contain multiple contexts and multiple interaction events.

The hierarchy is:

```text
study
  |
  +-- block
       |
       +-- LLM configuration
             |
             +-- run
                  |
                  +-- context
                       |
                       +-- interaction event
                            |
                            +-- artifact
                            +-- execution event
                            +-- audit event
                            +-- repair event
```

A run must have a unique study-level Run ID that is never reused.

## 4. Run identity

Every primary or pilot run receives a structured identifier.

The recommended logical fields are:

| Field | Purpose |
|---|---|
| Run ID | Unique study-wide identifier |
| Block ID | Randomization block for the primary W1 versus W2 comparison |
| Configuration ID | Eligible consumer LLM configuration |
| Access epoch | Versioned provider/configuration state |
| Workflow condition | W0, W1, W2, W3, W4 or W5 |
| Replication index | Prespecified within-configuration attempt number |
| Study phase | Pilot or primary |
| Prompt package version | Frozen prompt bundle version |
| Study package version | Scientific information bundle version |
| Execution environment ID | Standardized computational environment |
| Start month | Month-level run start |
| Terminal month | Month-level terminal state record |

The exact identifier syntax remains an investigator-defined implementation detail and will be frozen before primary collection.

No exact calendar day or clock time is required in the research registry. Event order is represented by sequence numbers.

## 5. Configuration identity

The LLM configuration is defined by the eligibility specification rather than by model name alone.[3]

Each run links to a configuration record containing, at minimum:

- provider;
- consumer product;
- interface;
- region;
- plan;
- displayed model name;
- model version if exposed;
- relevant tool capabilities;
- memory state;
- personalization state;
- web or retrieval state;
- connector state;
- access month;
- access epoch.

A model name without the surrounding interface and access state is not a complete experimental identifier.

## 6. Workflow condition identity

The condition field uses the locked W0-W5 definitions.

### W0

Minimal-instruction, single-context, monolithic execution.

### W1

Fully specified, single-context, monolithic execution.

### W2

Structured fresh-context execution with predefined stages and structured handoffs.

### W3

W2 plus one self-audit cycle and one bounded repair cycle.

### W4

W2 plus deterministic read-only validation, one bounded repair cycle and revalidation.

### W5

W2 plus one independently initiated same-model audit and one bounded repair cycle.

The condition changes workflow architecture rather than the underlying biomedical scientific target.[4,5]

## 7. Prompt versioning

Prompts must be immutable once a version enters primary collection.

Each prompt has:

- Prompt ID;
- condition;
- stage or event type;
- version;
- text;
- study package dependency;
- intended recipient context;
- permitted inputs;
- permitted outputs;
- change status;
- freeze status.

The registry must distinguish:

1. the canonical prompt text;
2. the prompt version actually sent;
3. the resulting LLM response.

A response cannot retroactively change the prompt record.

Prompt versions used only during pilot development must remain identifiable as pilot versions and must not be silently relabeled as primary versions.

## 8. Prompt classes

The registry distinguishes the following prompt classes.

| Class | Use |
|---|---|
| W0 initial instruction | Minimal monolithic workflow |
| W1 initial instruction | Fully specified monolithic workflow |
| W2 stage instruction | One predefined stage |
| W3 audit instruction | Self-audit |
| W4 validation instruction | Deterministic-validation response or permitted repair request |
| W5 audit instruction | Independent audit |
| Repair instruction | Bounded repair allowed by the assigned condition |
| Terminal reporting instruction | Final interpretation/report stage where specified |

The exact canonical wording will be frozen in the integrated protocol and prompt package.

This document deliberately does not invent final prompt text before the prompt-freeze stage.

## 9. Study-package version

The scientific information supplied to the LLM must have its own version.

The package version identifies the exact set of permitted study materials at the point of use.

The registry records:

- study package version;
- file manifest;
- file integrity identifiers where used;
- information classified as exposed;
- information classified as withheld;
- package change status.

The package must not contain hidden reference numerical results, reference source code or prior experimental trajectories when those are prohibited by the assigned workflow condition.[4,8]

## 10. Context registry

Every distinct LLM context receives a Context ID linked to a Run ID.

For each context, record:

| Field | Required information |
|---|---|
| Context ID | Unique identifier |
| Run ID | Parent run |
| Sequence | Context order within run |
| Condition | Assigned workflow |
| Stage | W2-W5 stage where applicable |
| Fresh context | Yes or no |
| Prior context link | Prior context if a permitted handoff exists |
| Prompt version | Initial instruction for the context |
| Files received | Input artifact identifiers |
| Handoff received | Handoff artifact identifier |
| State controls | Memory, personalization, retrieval and connector state |
| Terminal role | Whether the context produced an audit, repair or report |

A W2-W5 fresh context must not inherit conversational history merely because it is the same browser session or provider account.

Freshness is an experimental property and must be recorded as part of the context state.

## 11. Handoff registry

A context transition must occur through an explicit handoff artifact rather than an unrecorded conversational summary.

The handoff record should identify:

- source Context ID;
- destination Context ID;
- handoff version;
- files transferred;
- status;
- completed checks;
- unresolved issues;
- permitted next actions;
- artifact integrity identifiers.

The handoff may contain derived scientific evidence but must not contain information prohibited by the assigned condition.

For W2, the handoff is the mechanism through which fresh-context staging is made operational.

For W3-W5, audit or validator information is additionally recorded according to the assigned condition.

The exact handoff schema remains an investigator-defined implementation choice and will be frozen with the workflow package.

## 12. Interaction-event registry

Within a run, interaction events are recorded in sequence.

Recommended event types are:

- prompt sent;
- response received;
- artifact generated;
- artifact uploaded;
- artifact transferred;
- execution requested;
- execution result returned;
- audit requested;
- audit finding received;
- repair requested;
- repair artifact received;
- terminal report received;
- resource limitation observed;
- human intervention observed.

Each event should record:

| Field | Required information |
|---|---|
| Event ID | Unique identifier |
| Run ID | Parent run |
| Context ID | Context in which event occurred |
| Sequence number | Order within run |
| Event type | Controlled event class |
| Actor | LLM, execution system, validator or human |
| Input artifact links | Relevant inputs |
| Output artifact links | Relevant outputs |
| Prompt link | Prompt version where applicable |
| Intervention class | Mechanical, scientific or none |
| Error link | Failure ID where applicable |
| Resource link | Resource event where applicable |
| Notes | Concise factual record |

Sequence numbers are used instead of exact timestamps in the research registry.

## 13. Artifact registry

Generated files and exchanged artifacts require their own provenance record.

Artifact fields include:

- Artifact ID;
- Run ID;
- Context ID;
- stage;
- filename;
- artifact type;
- producing event;
- source prompt version where relevant;
- parent artifact;
- integrity identifier where practical;
- exposure status;
- execution status;
- final disposition.

Artifact types include:

- source code;
- configuration file;
- cohort manifest;
- label manifest;
- split manifest;
- implementation manifest;
- execution output;
- metric table;
- bootstrap output;
- calibration output;
- report;
- audit report;
- repair artifact;
- handoff artifact.

An artifact that is revised during an authorized repair receives a new Artifact ID or immutable version rather than replacing the earlier artifact in the registry.

## 14. Information-exposure registry

The registry must make it possible to reconstruct what the LLM could actually see.

For each run and context, classify information as:

### Exposed

Permitted scientific package, dataset information, generated intermediate artifact or execution evidence that the assigned condition is allowed to receive.

### Withheld

Reference source code, reference numerical results, prior trajectories or other information that is deliberately unavailable.

### Prohibited exposure

Information that should not have reached the LLM under the assigned condition.

Examples include:

- prior run output;
- another condition's repair;
- held-out reference result;
- hidden validator implementation;
- external web material;
- uncontrolled retrieval;
- persistent memory content from an earlier run.

The occurrence of prohibited exposure is recorded as a workflow or information-exposure failure even if the final numerical result is correct.[8,9]

## 15. Human-action registry

Human actions are recorded separately from LLM interaction events.

The action type is:

### Mechanical

Examples:

- opening the required context;
- entering a frozen prompt;
- uploading a prescribed file;
- copying a generated artifact;
- running the prescribed command;
- returning execution evidence;
- recording operational information.

### Scientific

Examples:

- changing scientific code;
- changing parameters;
- correcting a label;
- selecting among model implementations;
- diagnosing the scientific error for the LLM;
- prescribing an unplanned methodological repair;
- choosing whether to retain a result because it looks favorable.

Scientific human intervention prevents classification as an autonomous primary success under the current endpoint definition.[4,9]

## 16. Execution and evidence linkage

The interaction registry does not duplicate the computational execution log.

Instead, each execution event links to:

- execution record;
- environment ID;
- repository commit;
- command;
- exit status;
- stdout;
- stderr;
- output manifest;
- execution artifact identifiers.

This allows the evaluator to distinguish an LLM statement about what happened from the machine-generated evidence of what happened.[7,9]

## 17. Audit and repair registry

Every W3, W4 or W5 audit event receives a structured record.

| Field | Required information |
|---|---|
| Audit ID | Unique identifier |
| Run ID | Parent run |
| Audit type | Self, deterministic or independent LLM |
| Auditor configuration | Model/configuration identity |
| Source context | Context being audited |
| Audit context | Context performing the audit |
| Evidence available | Artifact identifiers |
| Findings | Error codes from the failure taxonomy |
| Severity | Critical, major or minor where applicable |
| Repair permitted | Yes or no |
| Repair request | Recorded instruction |
| Repair artifact | Artifact identifier |
| Re-execution | Required or not |
| Revalidation result | Pass or fail |
| Final audit status | Resolved or unresolved |

A W5 auditor is linked to the same prespecified LLM configuration as the executor in the primary comparison.

The independent relationship concerns the audit context and trajectory, not a change in model population.

## 18. Resource linkage

Interaction records link to the resource registry rather than duplicating all resource measurements.

The linked resource record should allow reconstruction of:

- LLM turns;
- context transitions;
- file transfers;
- execution attempts;
- audit attempts;
- repair attempts;
- elapsed operational time when measured;
- free-tier limit events;
- quota interruptions;
- terminal resource-limited noncompletion.[6]

The primary resource construct remains observable interaction resource use. Hidden server-side token or compute usage is not inferred when the provider does not expose it.

## 19. Terminal run record

At the end of every run, the registry records:

| Field | Required information |
|---|---|
| Terminal state | Clean success, recovered success, scientific failure, execution failure, resource-limited noncompletion, unauthorized intervention or indeterminate |
| Primary success | Yes or no |
| Fidelity status | Passing or specified failure state |
| Numerical equivalence status | Passing, failing or not applicable |
| Interpretation status | Passing or failing |
| Reproducibility evidence | Complete or incomplete |
| Scientific intervention | Yes or no |
| Failure IDs | Linked taxonomy codes |
| Final artifact | Final report or terminal artifact |
| Terminal month | Month-level terminal record |

The terminal state is determined after the full run record is reviewed. A conversationally plausible final response cannot override contradictory execution or audit evidence.[9]

## 20. Pilot and primary separation

Pilot and primary runs must be distinguishable at the registry level.

### Pilot runs

Pilot runs may be used to:

- debug file transfer;
- test context transitions;
- test validators;
- identify access failures;
- identify ambiguous prompt wording;
- revise the workflow package.

Pilot results do not enter the primary analysis.

Any pilot-derived change to a prompt, handoff, validator, resource ceiling or workflow condition receives a new version and is frozen before primary collection.

### Primary runs

Primary runs use the frozen prompt and workflow package.

Observed primary results cannot trigger silent prompt revision, workflow redesign or eligibility changes.

A needed change becomes a protocol change and must be handled through the change-control process.

## 21. Randomization and block linkage

The primary W1 versus W2 comparison uses randomized scheduling within blocks for each eligible LLM configuration.

The registry must therefore record:

- Block ID;
- configuration ID;
- assigned condition;
- replication index;
- randomization assignment;
- condition execution order.

The W1 and W2 assignments within a block are treated as scheduling units rather than paired biomedical observations.

The randomization mechanism and final replication count are frozen in the statistical plan after the sample-size simulation is complete.[10]

## 22. Access-epoch linkage

Every run must link to one access epoch.

The registry records the access epoch rather than assuming that a model name remains constant over the study.

A material change in model identity, relevant tool capability, context capacity, free-tier limits, memory or retrieval can create a new epoch under the reproducibility and eligibility rules.[3,7]

Runs from distinct epochs are not silently pooled.

The epoch record includes the access month and the evidence source used to establish the configuration.

## 23. Reproducibility linkage

The interaction registry links each run to:

- environment ID;
- repository commit;
- study package version;
- prompt package version;
- configuration ID;
- access epoch;
- artifact manifest;
- execution records;
- terminal state.[7]

A future investigator should be able to reconstruct the workflow trajectory without relying on an informal description in the manuscript.

The registry itself does not claim that a consumer interface is permanently reproducible. It preserves the configuration actually observed.

## 24. Transcript handling

Full transcripts are retained as underlying evidence when permitted and necessary for audit.

The registry does not replace those transcripts.

Instead, it provides structured links into them through Run ID, Context ID, Event ID and Prompt ID.

The structured registry should therefore remain compact enough to analyze across many runs.

The transcript is the detailed conversational evidence.

The registry is the experimental index.

These roles should not be merged.

## 25. Version control and change management

A prompt, study package, handoff schema, validator, or workflow condition that has entered primary collection is immutable.

A change creates a new version and must record:

- affected object;
- previous version;
- new version;
- reason;
- evidence basis;
- whether any primary outcome had already been observed;
- affected runs;
- pooling or exclusion decision.

The historical version remains identifiable.

This preserves the real research trajectory rather than rewriting earlier experimental conditions to match the eventual final design.

## 26. Registry quality checks

Before primary collection, the registry implementation must demonstrate that it can:

1. assign unique Run IDs;
2. link runs to configuration and access epoch;
3. distinguish pilot from primary;
4. preserve prompt versions;
5. represent multiple fresh contexts;
6. link handoff artifacts;
7. record information exposure;
8. classify human actions;
9. link executions and artifacts;
10. record audit and repair events;
11. record resource events;
12. record a terminal state;
13. prevent silent replacement of prior versions;
14. produce a complete run-level provenance record.

These are implementation checks for the registry itself.

They do not constitute primary experiment results.

## 27. Data retention and release boundaries

The interaction archive may contain provider-generated content, potentially sensitive operational information, or material that cannot be redistributed under provider terms.

The release package should therefore distinguish:

- material that can be published;
- material that can be archived privately;
- derived metadata suitable for public release;
- content that requires redaction;
- provider-restricted material.

The study should preserve enough structured metadata to allow audit even when a full transcript cannot be publicly released.

## 28. Evidence basis

TRIPOD-LLM emphasizes transparent reporting of LLM identity, prompting, human oversight, outputs, evaluation procedures and reproducibility, providing the main reporting basis for the interaction registry.[2]

Ruta et al. evaluated multiple prompt-specificity conditions in healthcare statistical analysis and observed substantial differences in accuracy across levels of prompt detail. Their study also preserved the actual prompts used, supporting the treatment of prompt version as a meaningful experimental record.[1]

ScienceAgentBench argues for evaluating individual tasks within scientific workflows and assessing generated programs and their execution rather than making broad end-to-end capability claims from final outputs alone.[11]

The exact registry fields, identifier structure, event classes, month-level temporal representation, exposure categories, versioning rules and transcript-retention policy are investigator-defined components of this study.

No primary experiment results are included.

## References

1. Ruta MR, Gaidici T, Irwin C, Lifshitz J. ChatGPT for Univariate Statistics: Validation of AI-Assisted Data Analysis in Healthcare Research. J Med Internet Res. 2025;27:e63550. doi:10.2196/63550.
2. Gallifant J, Afshar M, Ameen S, et al. The TRIPOD-LLM reporting guideline for studies using large language models. Nat Med. 2025;31(1):60-69. doi:10.1038/s41591-024-03425-5.
3. Consumer LLM Eligibility Specification. current-study/07 CONSUMER LLM ELIGIBILITY SPECIFICATION.md. Study repository; 2026.
4. LLM Workflow Experimental Protocol. current-study/09 LLM WORKFLOW EXPERIMENTAL PROTOCOL.md. Study repository; 2026.
5. Workflow Conditions and Ablation Plan. current-study/10 WORKFLOW CONDITIONS AND ABLATION PLAN.md. Study repository; 2026.
6. Resource Accounting and Accessibility Analysis. current-study/13 RESOURCE ACCOUNTING AND ACCESSIBILITY ANALYSIS.md. Study repository; 2026.
7. Reproducibility and Computational Environment. current-study/14 REPRODUCIBILITY AND COMPUTATIONAL ENVIRONMENT.md. Study repository; 2026.
8. Data Provenance and Data Dictionary. current-study/15 DATA PROVENANCE AND DATA DICTIONARY.md. Study repository; 2026.
9. Failure Taxonomy and Error Audit. current-study/16 FAILURE TAXONOMY AND ERROR AUDIT.md. Study repository; 2026.
10. Statistical Analysis Plan. current-study/12 STATISTICAL ANALYSIS PLAN.md. Study repository; 2026.
11. Chen Z, Chen S, Ning Y, et al. ScienceAgentBench: Toward Rigorous Assessment of Language Agents for Data-Driven Scientific Discovery. International Conference on Learning Representations; 2025.

## Evidence status

Published evidence supports treating prompt specification, model identity, interaction structure, human oversight and execution as reportable experimental features in LLM data-analysis studies.[1,2,11]

The exact registry schema, run identifiers, event vocabulary, month-level temporal convention and version-control rules are investigator-defined operational choices designed to make those evidence requirements executable in this study.

No primary execution results are included.
