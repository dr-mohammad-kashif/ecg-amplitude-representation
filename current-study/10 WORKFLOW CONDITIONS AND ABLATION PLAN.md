# Workflow Conditions and Ablation Plan

Status: Draft experimental design
Version: 0.1
Month: September 2026
Study phase: Preprotocol

## 1. Purpose

The workflow conditions and planned contrasts isolate specific components of the active LLM workflow study.

The conditions operate on the same locked biomedical machine learning specification. The Reference Biomedical Analysis Protocol defines the scientific target, while the LLM Workflow Experimental Protocol defines the general rules for execution.[1,2]

The experimental manipulation is specified before primary data collection.

The study does not assume that additional workflow structure improves scientific fidelity. Improvement, no effect, resource burden, new error, and failure to complete are all admissible outcomes.

## 2. Experimental architecture

The active condition set is:

| Condition | Definition | Role |
|---|---|---|
| W0 | Minimal monolithic workflow | Secondary instructional baseline |
| W1 | Fully specified monolithic workflow | Primary comparator |
| W2 | Structured fresh-context workflow | Primary experimental condition |
| W3 | W2 plus self-audit | Secondary verification condition |
| W4 | W2 plus deterministic validation | Secondary verification condition |
| W5 | W2 plus independent LLM audit | Secondary verification condition |

The primary comparison is W1 versus W2.

W0 is retained because it provides a separate estimate of the effect of explicit workflow specification within a single context.

W3, W4, and W5 are mechanism-oriented secondary conditions. They are not folded into the primary comparison.

## 3. Common scientific substrate

Every condition receives the same scientific target.

The following are held constant:

- dataset and dataset version;
- task definitions;
- cohort and label rules;
- patient-aware split;
- waveform representation;
- preprocessing;
- model architecture;
- model training configuration;
- primary random seed;
- evaluation metrics;
- primary estimand;
- uncertainty procedure;
- interpretation boundaries;
- information available in the frozen study package;
- standardized external execution substrate;
- eligibility boundary for the consumer LLM configuration.

The only planned differences are workflow-level properties defined below.

A change to any scientific component is recorded as a protocol deviation rather than being treated as a legitimate workflow difference.

## 4. W0. Minimal monolithic

### Definition

W0 is the least structured condition.

The LLM receives the complete study package, approved data access, and standardized execution interface together with a concise task instruction.

No predefined analytical stages are imposed.

No explicit gate sequence is required.

No separate audit or validator is present.

The interaction remains in one context.

### Intended contrast

W0 provides the secondary contrast:

$$
W1 - W0
$$

This asks whether making the intended workflow explicit changes end-to-end reference-faithful completion when context architecture remains monolithic.

### What W0 does not isolate

W0 versus W2 should not be interpreted as a clean estimate of one mechanism because that comparison changes both workflow specificity and context architecture.

For that reason, W0 versus W2 is not the primary causal comparison.

## 5. W1. Fully specified monolithic

### Definition

W1 receives the same study package and execution substrate as W0 and W2, but the prompt explicitly specifies the complete intended analytical sequence.

The specified sequence is:

1. data and provenance audit;
2. cohort and label construction;
3. analysis implementation;
4. execution and evaluation;
5. interpretation and reporting.

All work remains in one context.

There is no separate stage context, self-auditor, deterministic validator, or independent LLM auditor.

### Intended role

W1 is the primary comparator because it controls for the effect of explicit instruction specificity before the workflow is reorganized into fresh contexts.

The W1 condition therefore asks whether context architecture adds value beyond a fully specified monolithic instruction.

## 6. W2. Structured fresh-context

### Definition

W2 uses the same scientific package and execution substrate as W1, but the workflow is divided into five predefined stages.

Each stage is executed in a fresh context.

Structured handoff artifacts are the only permitted mechanism for carrying stage state forward, apart from the frozen study package.

The stages are:

1. data and provenance audit;
2. cohort and label construction;
3. analysis implementation;
4. execution and evaluation;
5. interpretation and reporting.

### Intended contrast

The primary comparison is:

$$
W2 - W1
$$

The intended intervention is a change from one continuous analytical context to a structured sequence of fresh contexts with explicit handoffs.

The comparison is therefore a workflow-architecture comparison, not an estimate of any single low-level feature such as context length, prompt wording, or file format.

### Required invariants

Relative to W1, W2 must preserve:

- the scientific package;
- execution substrate;
- resource ceiling principle;
- model configuration;
- access eligibility;
- external-information restrictions;
- final evaluation criteria.

The handoff schema must be fixed before primary data collection.

## 7. Stage structure within W2

The five stages are not separate scientific analyses. They partition the same analysis into controlled workflow states.

### Stage 1. Data and provenance

Output must contain enough evidence to establish data identity, required files, waveform structure, technical eligibility, fold information, and provenance checks.

### Stage 2. Cohort and labels

Output must contain the prespecified task construction, label assignments, record counts, patient counts, inclusion and exclusion records, and fold membership.

### Stage 3. Implementation

Output must contain the executable implementation and a record of the model and training configuration used.

### Stage 4. Execution and evaluation

Output must contain execution status, predictions, prespecified metrics, bootstrap outputs, calibration outputs, and execution evidence.

### Stage 5. Interpretation and reporting

Output must contain the final scientific interpretation with the predefined limits on what the experiment can establish.

A failed stage does not disappear because a later stage produces a plausible result.

## 8. W3. Self-audit ablation

### Definition

W3 adds one self-audit mechanism to W2.

The completed W2 state is evaluated in a fresh context by the same LLM configuration that performed the run.

The self-audit is read-only with respect to the scientific artifacts until a finding has been issued.

### Audit domains

The audit checks:

- data fidelity;
- cohort and label fidelity;
- analysis-plan fidelity;
- implementation fidelity;
- execution completeness;
- statistical fidelity;
- interpretation fidelity.

### Repair rule

A maximum of one repair cycle is permitted.

The repair context receives the audit findings and affected artifacts.

The repaired state is terminal after that cycle.

### Intended contrast

$$
W3 - W2
$$

This comparison asks whether explicit self-audit and one bounded recovery cycle alter completion or error outcomes beyond the structured fresh-context workflow itself.

It does not establish that self-reflection is intrinsically beneficial in other tasks.

## 9. W4. Deterministic validation ablation

### Definition

W4 adds a predetermined machine-checking layer to W2.

The validator is read-only and checks only properties specified before primary collection.

Potential checks include:

- required files;
- schema and dimensional integrity;
- cohort manifest consistency;
- patient-aware fold structure;
- model configuration;
- preprocessing definition;
- required metrics;
- bootstrap configuration;
- execution completion;
- required reproducibility fields.

### Repair rule

One bounded repair cycle is allowed after a validator failure.

The validator is then rerun.

A post-repair failure is terminal.

### Intended contrast

$$
W4 - W2
$$

This compares deterministic validation with the same structured workflow without that validation layer.

The contrast is designed to separate machine-checkable validation from general workflow staging.

## 10. W5. Independent audit ablation

### Definition

W5 adds an independent audit context to W2.

The auditor receives the protocol and final evidence artifacts but not the executor conversation or prior self-assessment.

The auditor uses the same eligible LLM configuration as the executor in primary runs.

### Repair rule

One audit cycle and one bounded repair cycle are permitted.

After the repair cycle the run is terminal.

### Intended contrast

$$
W5 - W2
$$

This asks whether an independently initiated evaluation context changes failure detection, recovery, or reference-faithful completion relative to W2.

The comparison is not a test of one model versus another because executor and auditor identity are held constant within primary W5 runs.

## 11. Comparison matrix

| Contrast | Added or changed component | Main question | Primary or secondary |
|---|---|---|---|
| W1 vs W0 | Explicit workflow specification within one context | Does explicit specification change completion? | Secondary |
| W2 vs W1 | Structured stages and fresh contexts with handoffs | Does workflow architecture change completion beyond monolithic specification? | Primary |
| W3 vs W2 | Same-model self-audit plus one repair | What changes when the executor evaluates and repairs its own work? | Secondary |
| W4 vs W2 | Deterministic validation plus one repair and revalidation | What changes when machine-checkable validation is added? | Secondary |
| W5 vs W2 | Independent same-model audit plus one repair | What changes when evaluation is separated from execution? | Secondary |

No contrast is interpreted as evidence that an individual mechanism is universally optimal.

## 12. Interaction and resource fairness

The complete run has a fixed ceiling of 32 LLM response turns across contexts. The same ceiling applies to W0 through W5.

The fairness rule is already fixed.

A workflow condition does not receive a larger total interaction allowance merely because it has more stages or verification mechanisms.

The total permitted interaction envelope must be defined at the complete-run level.

Within that envelope, conditions may allocate interactions differently according to their prespecified architecture.

Observable resource outcomes include:

- user turns;
- assistant turns;
- context resets;
- execution attempts;
- audit turns;
- repair turns;
- elapsed wall-clock time;
- free-tier limit encounters;
- resource-limited termination;
- human mechanical time;
- human scientific intervention.

The primary W1 and W2 allocation is fixed at 25 randomized blocks per eligible configuration. Secondary conditions use the fixed descriptive budget defined in the integrated Study Protocol.

## 13. Human intervention fairness

The human role is identical across conditions except for the mechanically required context transitions and artifact transfers defined by the condition.

The human may not provide scientific guidance to one condition that is withheld from another.

Examples of prohibited intervention include:

- correcting generated code;
- identifying the correct label construction;
- suggesting the right model architecture;
- selecting a preferred result;
- telling the LLM where an error occurred;
- supplying external literature during a run.

A scientific intervention is recorded as an outcome and deviation.

## 14. Information exposure and deferred W2A/W2B experiment

An earlier design considered a secondary comparison between whole-data exposure and chunked data exposure.

The concept is not included in the current primary ablation set.

The unresolved problem is defining equivalent information exposure across different context and file-access patterns without simultaneously changing:

- memory burden;
- retrieval burden;
- tool interaction;
- context length;
- artifact structure;
- execution behavior.

Until these properties can be operationally matched, W2A and W2B remain deferred.

A future W2A/W2B experiment may be added only after an explicit information-exposure specification and feasibility analysis.

It will not be retrofitted into the primary analysis after results are observed.

## 15. Prohibited condition combinations before protocol freeze

The following combinations are not added to the primary experiment without a new design decision:

- W1 plus self-audit;
- W1 plus deterministic validator;
- W1 plus independent audit;
- W3 plus deterministic validator;
- W4 plus independent audit;
- unrestricted combinations of audit and validation layers;
- cross-model W5 auditing.

Such combinations are scientifically possible, but adding them would increase the factorial structure and alter the interpretation of the existing contrasts.

They remain exploratory design space rather than undocumented primary conditions.

## 16. Failure interpretation across conditions

The same endpoint can arise through different mechanisms.

For example:

- W1 may fail because the monolithic context loses an intermediate state;
- W2 may fail because a handoff omits required information;
- W3 may detect a problem but fail to repair it;
- W4 may detect a machine-checkable error without detecting a scientific interpretation error;
- W5 may detect an error that the executor did not identify.

These are not interchangeable failures.

The run record therefore preserves the gate state, failure class, evidence, repair history, and terminal reason.

The study does not award a condition a single composite score to conceal these distinctions.

## 17. What each ablation can support

### W1 versus W0

Can support a statement about the effect of explicit workflow specification within a monolithic context, under the study's fixed target and resource boundary.

### W2 versus W1

Can support a statement about the effect of moving from fully specified monolithic execution to structured fresh-context execution under the study's fixed target and resource boundary.

This is the primary experimental contrast.

### W3 versus W2

Can support a statement about the incremental effect of the defined self-audit and bounded repair mechanism.

### W4 versus W2

Can support a statement about the incremental effect of the defined deterministic validation and bounded repair mechanism.

### W5 versus W2

Can support a statement about the incremental effect of the defined independent same-model audit and bounded repair mechanism.

None of these contrasts establishes a general ranking of LLM workflow architectures across unrelated tasks.

## 18. Relation to prior research designs

The condition structure incorporates recurring mechanisms observed in the prior methodological literature:

- explicit task specification in scientific LLM evaluation;
- process-level and executable evaluation rather than final narrative scoring;
- fresh-context and independent auditing concepts;
- bounded recovery rather than unrestricted repair;
- explicit failure dimensions;
- separate treatment of planning, execution, and verification.[3-8]

The exact condition definitions in this study remain investigator-defined.

The study does not present staging, self-audit, deterministic validation, or independent auditing as new mechanisms.

## 19. Protocol-freeze requirements

Before the first primary run, the following must be frozen:

1. exact W0 through W5 prompts;
2. study package version;
3. W2 stage instructions;
4. handoff schema;
5. W3 audit rubric;
6. W4 deterministic validator specification;
7. W5 audit rubric;
8. repair instructions;
9. terminal-state rules;
10. interaction budget;
11. run metadata fields;
12. deviation taxonomy;
13. definition of eligible access configurations;
14. information-isolation settings;
15. final primary endpoint and numerical equivalence criteria.

Pilot runs may identify operational defects before this freeze.

Pilot observations may not be used to redefine a primary endpoint or condition in a way that is selected according to primary outcomes.

## References

1. Reference Biomedical Analysis Protocol. current-study/08 REFERENCE BIOMEDICAL ANALYSIS PROTOCOL.md. Study repository; 2026.

2. LLM Workflow Experimental Protocol. current-study/09 LLM WORKFLOW EXPERIMENTAL PROTOCOL.md. Study repository; 2026.

3. Chen X, et al. ScienceAgentBench: Toward Rigorous Assessment of Language Agents for Data-Driven Scientific Discovery. ICLR. 2025.

4. Starace M, et al. PaperBench: Evaluating AI's Ability to Replicate AI Research. Proc Mach Learn Res. 2025;267:56843-56873.

5. Zhang Y, et al. DataSciBench: Benchmarking Large Language Models for Data Science Tasks. Findings of the Association for Computational Linguistics. 2026:3685-3728. doi:10.18653/v1/2026.findings-acl.181.

6. Wu et al. Performance, Failures, and Oversight of a Large Language Model Agent for Clinical Data Analysis: Evaluation Study. J Med Internet Res. 2026;28:e99597. doi:10.2196/99597.

7. Ma et al. LongHorizon-Harness: Advancing Long-Horizon Agents for Real-World Tasks. arXiv. 2026. arXiv:2608.01964.

8. Kurjan A, Cribbs AP. FlowBench: separating planning, fault recovery and interpretation in agentic bioinformatics. bioRxiv. 2026. doi:10.64898/2026.06.12.731844.

## Evidence status

The cited literature supports the use of executable task evaluation, process-level assessment, explicit verification mechanisms, and separation of execution from auditing. It does not establish the exact W0 through W5 architecture used here.

The condition definitions, ablation contrasts, bounded repair rules, deferred W2A/W2B design, and protocol-freeze requirements are investigator-defined choices for this study.

No primary experimental results are included.
