# Resource Accounting and Accessibility Analysis

Status: Draft analysis plan
Version: 0.1
Month: September 2026
Study phase: Preprotocol

## 1. Purpose

This plan defines how accessibility and resource use will be recorded during the LLM workflow experiment.

The study population is restricted to general purpose LLM configurations available to an ordinary user through a qualifying zero cost consumer route. The eligibility boundary is defined separately in [07 CONSUMER LLM ELIGIBILITY SPECIFICATION.md](07%20CONSUMER%20LLM%20ELIGIBILITY%20SPECIFICATION.md).[1]

Resource accounting therefore has two related but distinct functions.

First, it establishes whether a configuration actually satisfies the study's zero cost accessibility boundary.

Second, it measures the observable burden required to complete the fixed biomedical analysis under each workflow condition.

The study does not combine scientific fidelity and resource use into a single score.

## 2. Resource accounting principle

The primary monetary requirement is fixed by eligibility:

$$
\text{qualifying consumer access cost} = \$0
$$

A paid upgrade, paid API, paid agent service, institutional allocation, promotional credit, or other excluded payment route cannot be counted as part of a qualifying primary run.

The fact that every eligible configuration has zero monetary cost does not imply that the workflows have equal resource burden.

The study therefore records observable differences in:

- interaction burden;
- context management;
- execution effort;
- elapsed time;
- human mechanical effort;
- human scientific intervention;
- free-tier limits;
- failed or interrupted attempts;
- local computing requirements.

The resource analysis describes these dimensions separately rather than reducing them to a cost-efficiency score.

## 3. Resource domains

### 3.1 LLM interaction burden

Record the number of observable LLM interactions required for each run.

Where the consumer interface makes the distinction observable, record:

- user turns;
- assistant turns;
- audit turns;
- repair turns;
- other explicitly initiated LLM interactions.

A provider-specific token count is not assumed to be available.

Token use is recorded only when the consumer interface exposes it reliably and without introducing a different access route.

Server-side inference cost is not estimated from token counts unless the study has a documented basis for doing so.

### 3.2 Context transitions

Record the number of new contexts initiated during a run.

This includes:

- designated W2 stage contexts;
- W3 self-audit context;
- W4 repair context where required;
- W5 independent audit context;
- W5 repair context where required.

W1 and W0 normally remain within one context.

A context transition is recorded even when no scientific correction occurs because context management itself is part of the workflow architecture.

### 3.3 File and artifact transfers

Record observable file operations associated with the LLM workflow, including:

- files supplied to the LLM;
- generated files transferred into the execution workspace;
- execution outputs returned to the LLM;
- structured handoff artifacts;
- audit artifacts;
- repaired artifacts.

The count does not imply that all providers expose identical file metadata.

The purpose is to record observable workflow burden rather than infer hidden provider infrastructure.

### 3.4 Execution attempts

Record every prescribed execution attempt and its terminal state.

For each attempt, record:

- attempt number;
- workflow condition;
- execution status;
- whether the attempt followed the frozen workflow;
- whether the failure was scientific, execution-related, or access-related;
- whether another execution attempt was permitted.

An execution retry is not treated as free if it consumes interaction or time resources.

### 3.5 Wall-clock time

Wall-clock time is a secondary process outcome.

The run record should capture:

- run start month;
- run terminal month;
- elapsed wall-clock duration when it can be measured consistently;
- time spent waiting on provider responses when observable;
- time spent on execution;
- time spent on prescribed audit or repair steps.

Because the study uses month-level research records, the public research record does not retain day-level timestamps.

Where elapsed duration is measured during a run, the measurement method is recorded rather than reconstructing exact calendar timestamps from memory.

### 3.6 Human mechanical time

Human effort is divided into mechanical and scientific components.

Mechanical effort includes:

- opening the prescribed consumer interface;
- uploading the supplied study package;
- transferring artifacts;
- launching the standardized execution command;
- creating the next prescribed context;
- copying structured handoff evidence;
- recording run metadata.

This effort is permitted by the workflow protocol and is an accessibility outcome.

### 3.7 Human scientific intervention

Scientific intervention is not treated as ordinary workflow burden.

Examples include:

- changing generated code;
- changing labels or cohorts;
- selecting a scientific implementation;
- correcting a methodological decision;
- supplying external scientific information;
- choosing among competing results.

A scientific intervention is recorded as a protocol event and a primary endpoint failure where applicable.

The intervention burden is reported separately from mechanical user time.

### 3.8 Local compute and storage

The standardized execution substrate may use ordinary available computing hardware and freely available software.

Where measurable, record:

- CPU model or available processor class;
- GPU presence and model when relevant;
- RAM available;
- storage used by the run;
- execution time;
- peak memory where practical;
- software environment.

The experiment does not require specialized paid infrastructure.

Provider-side GPU allocation and inference hardware are not treated as measurable resources unless the consumer service explicitly exposes them.

## 4. Accessibility dimensions

Accessibility is broader than monetary cost.

The run record should preserve:

- ordinary consumer account requirement;
- payment instrument requirement;
- regional availability;
- required interface;
- required capabilities;
- context constraints;
- file limits;
- execution availability;
- free-tier quota;
- persistence and memory controls;
- external retrieval controls;
- need for repeated manual context transitions;
- need for local computing resources;
- whether the complete workflow can be completed without payment.

The exact eligibility criteria are defined in the consumer eligibility specification.[1]

## 5. Free-tier resource envelope

Free-tier limits are treated as part of the experimental environment rather than as technical obstacles to bypass.

Relevant limits may include:

- message quotas;
- rolling usage windows;
- file limits;
- context limits;
- execution limits;
- rate limits;
- temporary service restrictions;
- storage limits.

The study does not permit upgrading a qualifying run to a paid tier to finish an experiment.

A run that reaches a free-tier limit is recorded as a resource or access event.

If the limit causes terminal noncompletion, the run remains in the primary binary endpoint as a noncompletion while its failure mechanism is classified separately.

This distinction follows the experimental design in which the zero cost envelope itself is part of the study population.[1,2]

## 6. Resource envelope across workflow conditions

The workflow protocol requires the same study-wide resource principle across W0 through W5.[2]

The final numerical interaction ceiling is not yet frozen.

Once established, it will apply to the complete run rather than granting a larger total budget to conditions with more workflow components.

The resource allocation may differ within that common ceiling because W3 through W5 deliberately contain audit or repair stages.

For example, a structured workflow may consume more contexts while a monolithic workflow may consume fewer contexts but more continuous interaction.

The observed burden is therefore a result rather than a prespecified reason to prefer one condition.

## 7. Accessibility feasibility

Primary-run feasibility is distinct from the existence of a free feature.

A configuration is not considered operationally qualifying merely because it can:

- accept a file;
- generate code;
- execute a small example;
- provide a free chat interface.

The complete frozen workflow must be capable of execution within the qualifying free configuration after the final workflow and interaction budget are frozen.[1]

The feasibility assessment therefore occurs in two stages:

1. capability eligibility;
2. complete primary-run feasibility.

A candidate that passes the first but fails the second does not enter the primary model pool.

## 8. Resource failure classification

Resource events receive a separate classification from scientific and execution failures.

### Access capability failure

A required free capability is unavailable.

### Quota failure

A free-tier quota or usage ceiling prevents continuation.

### Context capacity failure

The prescribed context cannot accommodate the required stage state within the qualifying configuration.

### File or artifact limit failure

The required file or artifact cannot be supplied or retrieved within the free configuration.

### Service interruption

The provider becomes unavailable or interrupts the qualifying consumer service.

### Local infrastructure failure

The standardized execution substrate fails independently of the LLM's scientific output.

Each event is linked to the affected run and workflow stage.

A resource failure is not relabeled as a scientific failure merely because it reduces the completion rate.

## 9. Resource and scientific outcomes remain separate

The study reports two related questions.

The first is:

> Did the workflow produce a reference-faithful biomedical analysis?

The second is:

> What observable resource and accessibility burden accompanied that outcome?

A workflow may therefore have:

- high scientific fidelity with high interaction burden;
- low scientific fidelity with low interaction burden;
- successful completion with substantial context management;
- noncompletion because of a free-tier limit despite scientifically appropriate intermediate work.

These outcomes remain distinct.

The study does not define a quantity such as:

$$
\frac{\text{scientific fidelity}}{\text{resource cost}}
$$

as a primary or composite endpoint.

The underlying dimensions will be reported separately.

## 10. Human burden and accessibility

Human time is particularly relevant because an ordinary-user workflow may transfer effort from the model to the user.

The study therefore records:

- mechanical context management;
- file handling;
- execution launching;
- artifact transfer;
- waiting and monitoring where measurable;
- scientific interventions.

Scientific intervention is never counted as successful autonomous completion.

A completed run after prohibited scientific intervention is recorded as intervention-assisted completion in the process record and as a failure of the primary autonomous endpoint where the intervention affected the scientific trajectory.

## 11. Retry and recovery burden

Retries are counted separately for:

- execution;
- audit;
- repair;
- provider-access recovery;
- infrastructure recovery.

A retry is counted even when it eventually succeeds.

For W3, W4, and W5, the permitted repair cycle is part of the predefined workflow architecture.[2]

The record therefore preserves:

- initial failure;
- detection;
- repair attempt;
- post-repair result;
- additional resource burden;
- whether a new error was introduced.

The purpose is to measure recovery rather than hide the cost of reaching the final state.

## 12. Run-level resource record

Each primary run should eventually produce a resource record containing:

| Field | Description |
|---|---|
| Run ID | Unique study identifier |
| Condition | W0 through W5 |
| Configuration ID | Eligible LLM configuration |
| Access epoch | Configuration state |
| Start month | Month in which the run began |
| Terminal month | Month in which the run reached terminal state |
| LLM turns | Observable user and assistant interactions |
| Context resets | Number of fresh contexts |
| File transfers | Observable supplied and returned artifacts |
| Execution attempts | Count of prescribed execution calls |
| Audit attempts | Count of audit contexts |
| Repair attempts | Count of repair cycles |
| Wall-clock duration | Elapsed duration when measured consistently |
| Human mechanical time | Recorded mechanical effort |
| Scientific intervention | Count and description if any |
| Free-tier events | Quota, context, file, or service limitations |
| Local CPU/RAM/GPU | Available execution resources where relevant |
| Local storage | Storage used where measurable |
| Terminal resource state | Resource-related completion status |
| Notes | Operational observations |

The final schema is implemented after the prompt and run registry are frozen.

## 13. Aggregation and reporting

Resource variables are summarized by workflow condition and eligible LLM configuration.

Continuous variables will generally be summarized using median and interquartile range because resource distributions are expected to be skewed.

Counts and proportions will be used for discrete resource events.

Where useful, report the relationship between resource variables and reference-faithful completion descriptively.

This does not change the primary statistical estimand.

No post hoc resource measure will be promoted to a primary endpoint because it appears to distinguish workflow conditions.

## 14. Provider and configuration changes

A resource record is tied to the exact consumer configuration and access epoch.

A provider change that affects:

- model identity;
- context capacity;
- free usage limits;
- file handling;
- code execution;
- memory or persistence;
- external retrieval;
- another primary workflow capability

creates a new access epoch unless equivalence is justified before pooling.

The access epoch rule is defined in the consumer eligibility specification and is relevant to resource interpretation because an observed burden change may otherwise reflect provider drift rather than workflow architecture.[1]

## 15. Zero cost does not imply zero burden

The study's zero monetary cost criterion is deliberately narrow.

It does not claim that the workflow is burden-free.

A qualifying user may still incur:

- substantial interaction time;
- repeated context creation;
- local computing requirements;
- file management;
- waiting for usage windows;
- failed attempts;
- audit and repair effort.

This is why the accessibility analysis is a separate component of the study rather than a statement that free access is equivalent to unrestricted access.

## 16. What the resource analysis can support

The resource analysis can support statements about the observed accessibility and operational burden of the prespecified workflow conditions under the eligible consumer configurations.

It can report whether:

- one workflow used more interactions;
- one workflow required more context transitions;
- one workflow consumed more human mechanical time;
- free-tier limits caused noncompletion;
- audit and repair increased operational burden;
- local execution requirements were materially different;
- resource failures differed by configuration or workflow.

It cannot establish the infrastructure cost incurred by the providers.

It cannot infer hidden token consumption or provider GPU usage when those measurements are not exposed.

It cannot establish that one workflow is universally more affordable for all users or future consumer configurations.

## 17. Reporting requirements

The final report should present resource and accessibility results alongside scientific outcomes rather than hiding them in an appendix.

At minimum, report:

- eligible configuration count;
- access epochs represented;
- qualifying free capabilities;
- primary-run feasibility;
- resource-limited noncompletion;
- interaction burden;
- context resets;
- execution attempts;
- repair attempts;
- wall-clock duration where measured;
- human mechanical time where measured;
- scientific intervention count;
- relevant local compute requirements.

The denominator and measurement basis must be explicit for every reported quantity.

## 18. Evidence basis and study-specific decisions

The consumer-access boundary, access epoch concept, free-tier feasibility rule, and standardized workflow resource envelope are defined in the eligibility and workflow protocols.[1,2]

Reporting guidance for LLM studies supports recording model identity, configuration, evaluation setting, prompting, oversight, and relevant temporal context.[3]

FAIR and research-software reproducibility principles support preserving the provenance and computational information needed to interpret and reproduce resource-related observations.[4,5]

The exact resource variables, classifications, aggregation choices, and separation of scientific and resource outcomes are investigator-defined components of this study.

## References

1. Consumer LLM Eligibility Specification. current-study/07 CONSUMER LLM ELIGIBILITY SPECIFICATION.md. Study repository; 2026.

2. LLM Workflow Experimental Protocol. current-study/09 LLM WORKFLOW EXPERIMENTAL PROTOCOL.md. Study repository; 2026.

3. Gallifant J, et al. The TRIPOD-LLM reporting guideline for studies using large language models. Nat Med. 2025;31(1):60-69. doi:10.1038/s41591-024-03425-5.

4. Wilkinson MD, Dumontier M, Aalbersberg I, Appleton G, Axton B, et al. The FAIR Guiding Principles for scientific data management and stewardship. Sci Data. 2016;3:160018. doi:10.1038/sdata.2016.18.

5. Barker M, Chue Hong NP, Katz DS, Lamprecht A-L, Martinez-Ortiz C, Psomopoulos F, et al. Introducing the FAIR Principles for research software. Sci Data. 2022;9:622. doi:10.1038/s41597-022-01710-x.

## Evidence status

The current resource framework is consistent with the study-wide consumer eligibility and workflow specifications.

The specific resource variables, month-level public records, failure classifications, aggregation summaries, and separation of monetary eligibility from operational burden are investigator-defined study components.

No primary resource measurements are included.
