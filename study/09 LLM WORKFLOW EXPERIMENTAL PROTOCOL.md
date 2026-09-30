# LLM Workflow Experimental Protocol

## 1. Purpose

This protocol specifies the experimental use of general purpose consumer-accessible LLM systems as analytical operators for a fixed biomedical machine learning task.

The biomedical analysis, dataset, cohort definitions, model, training procedure, evaluation metrics, primary estimand, and interpretation boundaries are defined separately in the Reference Biomedical Analysis Protocol.[1]

The experimental factor is workflow architecture.

The primary comparison is:

- W1, fully specified monolithic workflow in one context
- W2, structured fresh-context workflow with predefined stages and structured handoffs

W0 is a secondary instructional baseline. W3, W4, and W5 are secondary verification conditions.

The primary causal question is:

> Under a locked biomedical machine learning protocol, does moving from a fully specified monolithic LLM workflow to a structured fresh-context workflow change end-to-end reference-faithful completion when both operate under the same zero cost consumer access constraints?

The overarching research question and the confirmatory primary causal question are stated separately in the integrated Study Protocol.

## 2. Experimental unit

A run is one complete attempt by one eligible LLM configuration to perform the locked biomedical analysis under one prespecified workflow condition.

The primary replication strata are the eligible consumer LLM configurations established by the Consumer LLM Eligibility Specification.[2]

Model or provider is treated as a fixed replication stratum. The primary analysis does not treat the small set of eligible configurations as a random sample from a larger population of all LLMs.

The run retains the complete experimental record required to determine:

- workflow condition;
- LLM configuration and access epoch;
- supplied study package;
- prompts and prompt version;
- context structure;
- handoff artifacts;
- execution records;
- errors and repairs;
- scientific interventions;
- final analysis state;
- resource and access events.

## 3. Conditions held constant

The following remain identical across W0 through W5 unless an explicit workflow condition definition requires otherwise:

- scientific question;
- dataset version;
- diagnostic tasks;
- label definitions;
- cohort rules;
- patient-aware data split;
- waveform representation;
- preprocessing definition;
- model architecture;
- training configuration;
- primary seed;
- evaluation metrics;
- primary estimand;
- uncertainty procedure;
- interpretation boundaries;
- standardized execution substrate;
- access eligibility criteria;
- prohibition on external information retrieval.

The workflow layer is the intended experimental manipulation.

A change to the biomedical specification is a protocol deviation, not a workflow adaptation.

## 4. Study package

Every primary run receives the same frozen study package.

The package contains the scientific materials needed to perform the reference analysis, together with the approved execution interface and required data access.

The package may include:

- reference protocol;
- data and provenance specification;
- implementation requirements;
- analysis requirements;
- evaluation definitions;
- interpretation boundaries;
- execution instructions;
- machine-readable schemas required by the workflow.

The package does not expose:

- reference numerical results;
- reference predictions;
- reference-agreement criteria that have not yet been frozen;
- previous LLM trajectories;
- previous audit findings;
- results from other primary runs.

The purpose is to evaluate execution against a pre-existing specification rather than allowing the LLM to optimize toward a known numerical answer.

## 5. Information access boundaries

Primary runs operate without external information retrieval.

The following are prohibited unless they are explicitly part of the standardized study package:

- web search;
- external literature retrieval;
- external repositories;
- connected applications;
- uncontrolled file retrieval;
- provider memory containing prior study information;
- personalization that can expose prior study information;
- external agent services;
- external model calls.

A configuration that cannot provide the required information-isolation state is excluded or classified as indeterminate under the consumer eligibility specification.[2]

The old public ECG repository creates a nonzero possibility that some study information may already be known to an LLM through training or prior exposure. The experiment therefore does not claim contamination-free model knowledge. The controlled intervention is the information available during the run itself.

## 6. Standard execution environment

LLM-generated scientific code is executed through a standardized external computational substrate.

The substrate is the same logical execution interface across workflow conditions.

The LLM may generate or modify files within the permitted workspace and may request execution through the prescribed interface.

The execution environment records, where available:

- timestamp;
- command or launcher identifier;
- exit status;
- stdout;
- stderr;
- generated files;
- runtime;
- software environment;
- repository or package version.

The execution substrate may use ordinary existing hardware and freely available software. It must not introduce a paid cloud service, paid software package, paid agent, API billing relationship, or other paid dependency into the qualifying consumer workflow.[2]

The purpose of this separation is to prevent differences between provider-specific code execution systems from becoming an uncontrolled component of the workflow comparison.

## 7. Human role

The human operator is a mechanical interface.

Permitted actions include:

- creating the prescribed consumer conversation;
- supplying the frozen study package;
- entering the frozen prompt;
- transferring generated files to the prescribed workspace;
- launching the prescribed execution command;
- returning permitted execution evidence;
- creating the next prescribed context;
- transferring the predefined handoff artifact;
- recording run metadata and access events.

The human operator may not:

- modify scientific code generated by the LLM;
- change labels or cohorts;
- change preprocessing;
- change model architecture or hyperparameters;
- select among competing scientific implementations;
- tell the LLM that a result is incorrect;
- suggest a scientific correction;
- choose a favorable result;
- suppress an unsuccessful run;
- silently retry outside the prespecified workflow;
- introduce external scientific information.

Any unauthorized scientific intervention is recorded as a distinct failure class and the run is not silently repaired.

## 8. Context and persistence rules

A context is the complete interaction state available to the LLM within one designated consumer conversation.

A fresh context means a newly initiated conversation or equivalent provider context in which prior conversation history is not available.

Primary runs require, where technically possible:

- memory disabled;
- personalization disabled;
- connected applications disabled;
- external retrieval disabled;
- web search disabled;
- new context for every W2 stage;
- no prior study artifacts accessible outside the prescribed handoff.

W1 and W0 intentionally remain within one context.

W3, W4, and W5 introduce additional fresh contexts only where their condition definitions require audit or repair separation.

The access record must capture any provider limitation that prevents a complete persistence-control state.

## 9. Resource envelope

All workflow conditions operate under the same study-wide resource principle.

Each run has a common ceiling of 32 LLM response turns. The ceiling is fixed before primary collection and applies equally to W0 through W5.

The budget applies to the complete run rather than granting a larger total allowance to more structured conditions.

Observable resource variables include:

- user turns;
- assistant turns;
- context resets;
- file uploads;
- execution attempts;
- audit attempts;
- repair attempts;
- elapsed wall-clock time;
- free-tier limit encounters;
- quota-induced interruptions;
- resource-limited noncompletion;
- human mechanical time;
- human scientific intervention count.

Provider-side token or compute values are recorded only when the consumer interface exposes them reliably.

Resource use is an outcome, not an explanatory label for scientific failure.

## 10. W0. Minimal monolithic workflow

W0 is the secondary instructional baseline.

The LLM receives the complete study package, data access, and standardized execution interface together with one concise task instruction.

The workflow does not impose predefined analytical stages, explicit gate prompts, self-audit, deterministic validation, or independent review.

All reasoning and interaction occur within one context.

The model may respond to execution errors and continue within the same 32-response interaction envelope.

W0 isolates the effect of adding explicit workflow specification when compared with W1.

## 11. W1. Fully specified monolithic workflow

W1 is the primary monolithic comparator.

The LLM receives the same study package, data access, execution environment, information restrictions, and resource envelope as W0 and W2.

The initial instruction explicitly specifies the intended workflow sequence:

1. audit data and provenance;
2. construct the prespecified cohorts and labels;
3. implement the locked analysis;
4. execute the analysis;
5. calculate the prespecified metrics;
6. check the outputs;
7. produce the final scientific report.

The model remains responsible for the complete analysis in one context.

There is no separate stage context, independent auditor, or deterministic validator in W1.

The purpose of W1 is to provide a strong monolithic baseline that controls for explicit instruction specificity when W1 is compared with W2.

## 12. W2. Structured fresh-context workflow

W2 is the primary experimental workflow.

The complete analysis is divided into five predefined stages.

Each stage is conducted in a fresh context and receives only the study package plus the handoff artifacts prescribed for that stage.

The stage sequence is fixed:

1. data and provenance audit;
2. cohort and label construction;
3. analysis implementation;
4. execution and evaluation;
5. interpretation and reporting.

A stage cannot be skipped silently.

The next stage receives the structured evidence produced by the preceding stage rather than the preceding conversational history.

### Stage 1. Data and provenance audit

The LLM establishes:

- required files;
- dataset identity and version;
- data structure;
- waveform availability;
- sampling information;
- technical eligibility;
- patient and fold information;
- provenance checks.

The stage produces a structured audit artifact.

### Stage 2. Cohort and label construction

Using the study package and Stage 1 evidence, the LLM constructs:

- task cohorts;
- label assignments;
- inclusion and exclusion records;
- record counts;
- patient counts;
- fold membership.

The stage produces a cohort and label manifest.

### Stage 3. Analysis implementation

The LLM receives the locked scientific specification and preceding structured evidence.

It constructs the executable analysis without changing the reference scientific specification.

The stage produces source code and an implementation manifest.

### Stage 4. Execution and evaluation

The stage executes the analysis through the standardized substrate and calculates the prespecified evaluation outputs.

It records:

- execution status;
- generated predictions;
- primary and secondary metrics;
- bootstrap outputs;
- calibration outputs;
- technical failures;
- execution logs.

The stage produces a results package.

### Stage 5. Interpretation and reporting

The LLM receives the prescribed scientific evidence from earlier stages.

It prepares the final report while respecting the predefined interpretation boundaries.

The final report must distinguish:

- protocol fidelity;
- numerical result;
- uncertainty;
- execution limitations;
- resource or access limitations;
- unsupported conclusions.

## 13. W3. W2 with self-audit

W3 follows W2 through the complete five-stage workflow.

After Stage 5, a separate fresh context performs a structured self-audit against the locked protocol.

The self-audit receives the required final artifacts and protocol information, but not a hidden reference answer.

The audit evaluates at least:

- data and cohort fidelity;
- label fidelity;
- analysis specification fidelity;
- implementation fidelity;
- execution completeness;
- statistical fidelity;
- interpretation fidelity.

The audit records:

- finding;
- severity;
- evidence;
- affected artifact or gate;
- correction requirement.

A maximum of one repair cycle is permitted.

The repair context receives the audit findings and the relevant artifacts and may correct only the identified issues.

After one repair cycle, the final state is terminal for that run.

An unresolved failure remains a failure. Further discretionary repair is not permitted.

## 14. W4. W2 with deterministic validation

W4 follows W2 and adds machine-checkable validation.

The validator is read-only with respect to the generated scientific artifacts.

Its checks may include:

- required files present;
- required columns and shapes;
- cohort counts consistent with manifests;
- patient-disjoint fold structure;
- model architecture parameters;
- preprocessing specification;
- expected metric fields;
- bootstrap configuration;
- absence of forbidden external information;
- execution completion;
- reproducibility manifest completeness.

The validator does not decide whether a scientific method is clinically appropriate beyond the machine-checkable properties explicitly specified in advance.

Validation failures are returned as structured findings.

One bounded repair cycle is permitted.

After repair, the validator is run again.

A post-repair validation failure is terminal for the run.

The validator specification must be frozen before primary collection and must not contain checks derived from primary LLM outcomes.

## 15. W5. W2 with independent LLM audit

W5 follows W2 through completion and then introduces an independent fresh LLM audit context.

The auditor receives:

- the locked scientific protocol;
- the relevant final artifacts;
- the required execution evidence;
- the audit rubric.

The auditor does not receive:

- the executor's conversation;
- the executor's hidden reasoning;
- the executor's self-assessment;
- prior audit conclusions.

The auditor acts as an evaluator rather than a second executor.

For primary W5 runs, the auditor uses the same eligible LLM configuration as the executor so that workflow architecture is not confounded with model identity.

The auditor reports findings using the same structured finding and severity schema used for W3.

One bounded repair cycle is permitted.

The repair is conducted in a fresh context using the audit evidence.

No further repair is permitted after that cycle.

## 16. Gate architecture

Every complete run is evaluated across the same scientific gate sequence:

1. Data gate
2. Cohort and label gate
3. Analysis plan gate
4. Implementation gate
5. Execution gate
6. Statistical evaluation gate
7. Interpretation gate
8. Final reconciliation

Each gate records:

- required evidence;
- required condition;
- status as PASS, FAIL, or UNCERTAIN;
- relevant deviation;
- next permitted state.

A later gate cannot erase a failure at an earlier gate.

A correct numerical result does not automatically pass a failed scientific gate.

## 17. Primary endpoint

The primary endpoint is reference-faithful completion.

A run is classified as successful only when all critical conditions are satisfied:

1. no critical protocol violation;
2. required analysis executes to completion;
3. primary numerical outputs satisfy the frozen reference-agreement criteria;
4. the interpretation passes the prespecified interpretation audit;
5. the final state contains the required reproducibility evidence;
6. no unauthorized human scientific intervention occurred.

The endpoint is binary at the run level.

The detailed failure taxonomy is retained separately so that two failures with different mechanisms are not collapsed into the same scientific explanation.

## 18. Secondary outcomes

Secondary outcomes include:

- numerical error in the primary biomedical estimand;
- task-specific numerical errors;
- protocol violation severity;
- execution failure;
- resource or access failure;
- unauthorized human scientific intervention;
- wall-clock time;
- interaction count;
- context-reset count;
- execution attempts;
- audit attempts;
- repair attempts;
- repair success;
- new error after repair;
- interpretation fidelity;
- reproducibility across repeated runs.

No composite numerical score is used as a substitute for these separate outcomes.

## 19. Failure classes

A failed run must receive one or more applicable failure classes.

### Scientific or protocol failure

The LLM changes or misimplements a required scientific component.

Examples include wrong cohort, wrong label rule, wrong preprocessing, wrong model, wrong metric, wrong statistical procedure, or unsupported interpretation.

### Execution failure

The scientific specification is not completed because the generated implementation cannot execute or produces an incomplete execution state.

### Resource or access failure

The run terminates because of consumer usage limits, context limits, quota restrictions, unavailable capabilities, or another qualifying access constraint.

### Unauthorized human scientific intervention

The human modifies, selects, corrects, or suppresses scientific content outside the permitted mechanical interface.

These classes are recorded separately even when they contribute to the same noncompletion endpoint.

## 20. Protocol deviations

A primary run must not be silently altered.

Deviations include:

- unplanned prompt modification;
- use of prohibited external information;
- context reuse where a fresh context is required;
- unrecorded repair;
- human scientific intervention;
- alteration of the locked study package;
- execution outside the standardized interface;
- undocumented provider configuration change.

Each deviation record includes:

- run identifier;
- workflow condition;
- deviation type;
- description;
- timing;
- immediate consequence;
- whether the run remains eligible for the primary endpoint.

A deviation that changes the scientific object or workflow manipulation is not retrospectively reclassified as normal execution.

## 21. Access epochs

Consumer LLM systems can change during the study.

Each run therefore records the access epoch defined by:

- provider;
- consumer product;
- plan;
- displayed model;
- model version when visible;
- region;
- access date;
- enabled capabilities;
- relevant context limits;
- usage limits;
- persistence settings.

A change that materially alters model identity, tool availability, context capacity, or another feature relevant to the experiment defines a new access epoch unless equivalence is justified before pooling.

The study reports provider and model identity with the access epoch rather than treating a provider name as a timeless experimental condition.[3]

## 22. Reproducibility of workflow identity

Every primary run receives a unique run identifier.

The run record links:

- model configuration record;
- access epoch;
- workflow condition;
- prompt version;
- study package version;
- handoff schema version;
- validator version when applicable;
- execution environment version;
- repository commit;
- timestamps;
- context identifiers where available;
- generated artifacts;
- deviations;
- resource events;
- final gate states.

A run cannot be considered reproducible from the final report alone.

The complete workflow trajectory and relevant intermediate artifacts are part of the evidence record, consistent with recent evaluations that emphasize executable evidence and process-level assessment rather than final text alone.[4-8]

## 23. Primary comparison

The primary contrast is W2 versus W1.

The intended interpretation is the difference in reference-faithful completion under:

- the same biomedical specification;
- the same eligible LLM configuration;
- the same free-access envelope;
- the same standardized execution substrate;
- the same information restrictions;
- the same total permitted interaction principle.

The workflow intervention is:

> monolithic execution versus structured fresh-context execution.

W0 is used for the secondary comparison W1 versus W0.

W3, W4, and W5 provide mechanistic comparisons against W2 and are not part of the primary causal claim.

## 24. Model-level replication

For each eligible consumer configuration, W1 and W2 are evaluated within the same configuration.

The primary workflow contrast is therefore formed within model or provider stratum before aggregation across eligible configurations.

The aggregation procedure and uncertainty model are specified in the Statistical Analysis Plan and are not changed by observed model-specific results.

A provider with no feasible primary run under a qualifying free configuration is recorded as an access or feasibility failure rather than silently replaced by a paid model.

## 25. Pilot and primary separation

Pilot runs may be used to:

- test file transfer;
- verify the execution substrate;
- identify missing operational fields;
- test whether the workflow can be executed as specified;
- identify provider capability failures;
- debug logging.

Pilot runs are not part of the primary dataset.

A pilot discovery that changes a scientific endpoint, workflow definition, validator rule, eligibility criterion, or other prespecified analysis element must be documented as a protocol change before primary collection.

Primary prompts, schemas, validators, resource ceilings, and run accounting are frozen before the first primary run.

## 26. Stopping and terminal states

A workflow run reaches a terminal state when:

- the required final evidence has been produced;
- a defined terminal failure occurs;
- the permitted repair allocation is exhausted;
- the consumer configuration becomes unusable under the qualifying access envelope;
- the run encounters an explicitly prespecified safety or infrastructure termination condition.

After terminal state, no discretionary scientific repair is allowed.

A failed primary run remains part of the dataset and is not replaced solely because its failure is inconvenient.

## 27. Interpretation boundaries

The study does not measure whether one LLM provider is generally better than another.

It does not establish that structured workflows are universally superior to monolithic workflows.

It evaluates a specific workflow intervention on a fixed biomedical machine learning task under a specific consumer-access population.

The study does not treat the zero cost access boundary as a claim of scientific superiority. It is an explicit resource and population boundary defined to make the experiment reproducible.[2]

The study also does not treat the reference analysis as clinical ground truth.

## 28. Evidence basis

The workflow design draws on several established methodological observations.

Scientific-agent evaluations have increasingly assessed executable task completion, code validity, and reproducibility rather than relying only on narrative answers.[4-6]

Recent biomedical LLM studies demonstrate that apparently appropriate analysis plans can coexist with implementation errors, supporting separate evaluation of planning, execution, and scientific correctness.[7]

Recent agentic biomedical work also motivates explicit staging, reflection, validation, and independent auditing as distinct process mechanisms rather than treating them as one undifferentiated capability.[8]

The specific W0-W5 architecture, gate sequence, resource envelope, and endpoint are investigator-defined choices for isolating the workflow question in this study.

## References

1. Reference Biomedical Analysis Protocol. study/08 REFERENCE BIOMEDICAL ANALYSIS PROTOCOL.md. Study repository.

2. Consumer LLM Eligibility Specification. study/07 CONSUMER LLM ELIGIBILITY SPECIFICATION.md. Study repository.

3. Gallifant J, et al. The TRIPOD-LLM reporting guideline for studies using large language models. Nat Med. 2025;31(1):60-69. doi:10.1038/s41591-024-03425-5.

4. Chen X, et al. ScienceAgentBench: Toward Rigorous Assessment of Language Agents for Data-Driven Scientific Discovery. ICLR. 2025.

5. Starace M, et al. PaperBench: Evaluating AI's Ability to Replicate AI Research. Proc Mach Learn Res. 2025;267:56843-56873.

6. Zhang Y, et al. DataSciBench: Benchmarking Large Language Models for Data Science Tasks. Findings of the Association for Computational Linguistics. 2026:3685-3728. doi:10.18653/v1/2026.findings-acl.181.

7. Wu et al. Performance, Failures, and Oversight of a Large Language Model Agent for Clinical Data Analysis: Evaluation Study. J Med Internet Res. 2026;28:e99597. doi:10.2196/99597.

8. Bu et al. Empowering AI data scientists using a multi-agent LLM framework with self-evolving capabilities for autonomous, tool-aware biomedical data analyses. Nat Biomed Eng. 2026. doi:10.1038/s41551-026-01634-6.
