# Scientific Fidelity Evaluation Framework

Status: Draft evaluation framework
Version: 0.1
Month: September 2026
Study phase: Preprotocol

## 1. Purpose

This framework defines how the active study determines whether an LLM-run biomedical analysis is scientifically faithful to the locked reference specification.

The framework is separate from the Statistical Analysis Plan. It determines what constitutes an acceptable scientific state and how deviations are classified. The Statistical Analysis Plan will determine how run-level outcomes are summarized and compared.

The framework is also separate from the reference analysis itself. The reference protocol defines what the biomedical analysis is. This framework defines how an LLM execution is judged against that specification.

The central principle is that a plausible final number is not sufficient evidence of a faithful analysis.

## 2. Evaluation object

The object being evaluated is the complete analytical workflow from supplied study package to terminal scientific state.

The evaluation considers:

1. the information the LLM received;
2. the scientific decisions it made;
3. the implementation it produced;
4. the execution evidence;
5. the statistical outputs;
6. the final interpretation;
7. the reproducibility record;
8. any repair or human intervention.

A final report is therefore only one component of the evidence.

The framework follows the eight-gate sequence established in the workflow protocol:

1. data;
2. cohort and labels;
3. analysis plan;
4. implementation;
5. execution;
6. statistical evaluation;
7. interpretation;
8. final reconciliation.

Each gate is evaluated independently before the final run status is assigned.

## 3. Fidelity dimensions

### 3.1 Data and provenance fidelity

The run must use the specified dataset version and the prescribed files.

The evaluation checks:

- dataset identity;
- version;
- required file availability;
- waveform dimensions;
- sampling structure;
- units;
- provenance evidence;
- technical exclusions;
- patient identifiers where required;
- fold assignment.

A run does not pass this dimension merely because it can read some data. It must demonstrate that the data correspond to the specified analysis target.

### 3.2 Cohort and label fidelity

The run must construct the prespecified HYP versus NORM and MI versus NORM tasks using the locked label rules.

The evaluation checks:

- target definitions;
- NORM definition;
- likelihood threshold;
- target-plus-NORM handling;
- exclusion rule;
- sensitivity label definition when applicable;
- record counts;
- patient counts;
- fold-specific membership.

A change to the label rule is a scientific deviation even if the resulting cohort is numerically similar.

### 3.3 Analysis-plan fidelity

The run must preserve the scientific specification independently of how the LLM organizes its work.

The evaluation checks:

- raw and normalized representation definitions;
- preprocessing;
- model architecture;
- training configuration;
- seed;
- evaluation dataset;
- metrics;
- bootstrap procedure;
- primary estimand;
- sensitivity analyses;
- interpretation boundaries.

The LLM may choose implementation details that are not fixed by the protocol only when those details do not alter the scientific meaning of the locked analysis.

### 3.4 Implementation fidelity

The generated implementation must instantiate the required analysis.

The evaluation checks:

- input shape and ordering;
- preprocessing implementation;
- model layers and parameters;
- loss;
- optimizer;
- training settings;
- checkpoint rule;
- prediction generation;
- metric definitions;
- bootstrap implementation.

Structural properties are evaluated directly where possible.

Equivalent code organization is permitted when it implements the same specification.

### 3.5 Execution fidelity

The implementation must actually run to the required terminal state.

The evaluation checks:

- successful data loading;
- model fitting;
- validation;
- checkpoint generation;
- held-out prediction generation;
- metric calculation;
- bootstrap execution;
- calibration output where required;
- execution logs;
- generated artifacts;
- absence of unexplained execution gaps.

A report describing an analysis that was never executed does not pass execution fidelity.

### 3.6 Statistical fidelity

The statistical outputs must correspond to the locked evaluation procedure.

The evaluation checks:

- held-out test data use;
- AUROC calculation;
- average precision calculation;
- Brier score;
- prevalence;
- calibration;
- patient-level bootstrap;
- number of bootstrap resamples;
- one-class bootstrap handling;
- primary cross-task estimand;
- confidence interval calculation.

A numerically plausible statistic calculated using the wrong procedure remains a statistical fidelity failure.

### 3.7 Numerical fidelity

Numerical fidelity concerns agreement with the independently established reference analysis.

The comparison has two components.

The first is structural. Required numerical outputs must be generated from the correct inputs, model, evaluation set, and procedure.

The second is numerical. The resulting values must fall within the reference-equivalence criteria established before primary LLM collection.

No final numerical tolerance is specified in this framework before the reference-equivalence work is complete.

Numerical fidelity is therefore not evaluated using an arbitrary threshold such as a fixed AUROC difference selected in advance for convenience.

### 3.8 Interpretive fidelity

The final report must accurately describe what the analysis shows and does not show.

The evaluation checks whether the report:

- states the primary contrast correctly;
- distinguishes direction from magnitude;
- reports uncertainty;
- separates protocol fidelity from numerical agreement;
- avoids unsupported clinical conclusions;
- respects the study's noncausal interpretation boundary;
- distinguishes execution failure from scientific evidence;
- identifies important unresolved limitations.

A numerically correct analysis can therefore fail interpretive fidelity.

### 3.9 Reproducibility and traceability fidelity

The run must leave enough evidence to reconstruct what happened.

The evaluation checks:

- run identifier;
- workflow condition;
- LLM configuration;
- access epoch;
- prompt version;
- study package version;
- handoff version where applicable;
- execution environment;
- repository commit;
- relevant generated artifacts;
- deviations;
- resource and access events;
- terminal state.

The final report alone is not considered a complete reproducibility record.

## 4. Gate adjudication

Each gate receives one of three statuses.

### PASS

The required evidence is present and the gate conditions are satisfied.

### FAIL

There is sufficient evidence that a required condition was violated or that the necessary evidence is absent in a way that prevents the gate from being considered complete.

### UNCERTAIN

The available evidence is insufficient to establish either PASS or FAIL.

UNCERTAIN is retained as its own state. It is not converted into PASS because a result appears plausible, and it is not automatically treated as FAIL when the evidence is genuinely incomplete.

## 5. Critical, major and minor findings

Findings are assigned severity according to their effect on the scientific object.

### Critical

A critical finding changes or invalidates the primary scientific object or prevents valid adjudication of the primary endpoint.

Examples include:

- wrong dataset;
- wrong diagnostic task;
- wrong label rule;
- patient leakage;
- materially different model architecture;
- wrong primary estimand;
- use of forbidden reference results to guide the analysis;
- unauthorized scientific human repair;
- fabricated execution evidence.

A critical finding prevents reference-faithful completion.

### Major

A major finding does not necessarily invalidate the entire run, but it materially affects a secondary outcome, a gate, or the scientific interpretation.

Examples include:

- incorrect secondary metric;
- incomplete bootstrap artifact;
- missing required execution evidence for a secondary component;
- interpretation that overstates a secondary finding;
- reproducibility information too incomplete for independent reconstruction.

Major findings are retained in the run record even when the primary endpoint remains adjudicable.

### Minor

A minor finding concerns a limited documentation, formatting, or noncritical traceability defect that does not alter the scientific analysis.

Examples include:

- an incomplete descriptive field;
- a noncritical naming inconsistency;
- a missing convenience artifact that can be reconstructed without changing the analysis.

The detailed failure taxonomy will expand these categories and define the evidence expected for each failure class.

## 6. Primary completion adjudication

The primary endpoint is reference-faithful completion.

A run is eligible for a successful primary endpoint only if:

1. all critical gates PASS;
2. the required analysis reaches terminal execution;
3. the primary numerical outputs satisfy the frozen reference-equivalence criteria;
4. the final interpretation passes the interpretation gate;
5. the required reproducibility evidence is present;
6. no unauthorized human scientific intervention occurred.

A major or minor finding does not automatically negate the primary endpoint. Its effect depends on whether it affects one of the required primary conditions above.

This avoids turning every documentation defect into a scientific failure while preventing a good-looking final number from concealing a critical methodological error.

## 7. Structural, numerical and interpretive layers

The framework preserves three distinct forms of agreement.

### Structural agreement

The LLM follows the same scientific specification.

This includes data, labels, representation, model, training, split, metrics, statistical procedure, and interpretation rules.

### Numerical agreement

The resulting primary outputs fall within the frozen reference-equivalence criteria.

The criteria will be established from compliant reference executions rather than from LLM outcomes.

### Interpretive agreement

The final account of the result is scientifically consistent with the executed analysis and its uncertainty.

The three layers are not collapsed into a single score.

There is no single composite fidelity score.

## 8. Reference result is not clinical truth

The reference analysis is the numerical and computational standard for this experiment.

It is not an adjudicated biological truth and it does not establish which implementation is clinically correct outside the study protocol.

A run can be faithful to the reference specification while the reference analysis itself remains an investigator-defined computational experiment.

This distinction is particularly important for interpretation of the PTB XL phenotype labels and for avoiding the use of numerical agreement as a substitute for clinical validation.

## 9. Evidence required at each gate

| Gate | Minimum evidence |
|---|---|
| Data | Dataset identity, version, required files, waveform and provenance checks |
| Cohort and labels | Label rule, cohort manifest, record and patient counts |
| Analysis plan | Locked scientific specification and applied representation |
| Implementation | Source code, configuration record, architecture and preprocessing evidence |
| Execution | Run logs, predictions, generated outputs, execution status |
| Statistical evaluation | Metric outputs, bootstrap outputs, primary estimand calculation |
| Interpretation | Final report linked to executed evidence and uncertainty |
| Final reconciliation | Complete gate record, deviations, terminal state, reproducibility record |

The exact machine-readable form of these artifacts is specified in the later prompt and run registry work.

## 10. Evidence hierarchy

When evidence conflicts, the study uses the following hierarchy:

1. frozen protocol requirements;
2. dataset and cohort artifacts;
3. executable implementation;
4. execution outputs;
5. statistical outputs;
6. final narrative interpretation.

A narrative claim does not override contradictory execution evidence.

A numerical output does not override evidence that the wrong cohort or model was used.

An execution error does not establish that the scientific specification itself was wrong.

## 11. Repair adjudication

Repair is part of the workflow condition only when the condition explicitly permits it.

For W3, W4 and W5, at most one bounded repair cycle is allowed.

The adjudication record must distinguish:

- initial state;
- detected finding;
- repair action;
- post-repair state;
- whether the original failure was resolved;
- whether a new error appeared;
- terminal outcome.

A repair does not erase the initial failure.

This allows the study to measure detection and recovery rather than recording only the final state.

## 12. Human intervention adjudication

The human operator is permitted to perform mechanical actions defined in the workflow protocol.

Any action that changes scientific content, scientific code, parameters, labels, model choice, interpretation, or selection among competing results is a scientific intervention.

Such an intervention is recorded separately from model-generated failure.

A run that requires unplanned scientific human intervention cannot be silently reported as autonomous completion.

## 13. Resource and access events

Resource failures are evaluated separately from scientific failures.

Examples include:

- free-tier quota exhaustion;
- context limit;
- unavailable file capability;
- provider-side interruption;
- access epoch change;
- terminal resource limitation.

A resource failure can prevent primary completion, but it is not reclassified as a scientific error simply because the primary endpoint was not achieved.

The final analysis therefore records both:

1. whether the run completed faithfully;
2. why it did or did not complete.

## 14. Cross-condition fairness

The same fidelity criteria apply to W0 through W5.

The evaluation rubric, primary scientific specification, reference criteria, and interpretation boundaries do not change according to workflow condition.

Only the workflow features defined in the experimental protocol may vary.

The auditor in W5 is not given a different scientific standard from the executor.

The W3 self-audit and W4 deterministic validator are not permitted to introduce post hoc success criteria.

## 15. Repeat-run reproducibility

Repeated runs of the same condition and eligible LLM configuration are evaluated using the same gate and fidelity framework.

The framework therefore captures both:

- whether a run succeeds;
- whether the workflow behaves consistently across repeated runs.

Repeated-run reproducibility is not used to alter the primary definition of reference-faithful completion after data collection begins.

## 16. Relation to existing methodological guidance

The framework adopts several principles that recur in current reporting and evaluation guidance.

TRIPOD plus AI emphasizes transparent reporting of the data, model development, evaluation, performance, and validation procedures for clinical prediction models.[1]

TRIPOD-LLM extends reporting expectations to LLM identity, prompting, evaluation setting, outputs, oversight, and configuration details.[2]

PROBAST plus AI supports structured assessment of quality, risk of bias, and applicability for prediction models using artificial intelligence methods.[3]

Recent scientific-agent benchmarks such as ScienceAgentBench, PaperBench, and DataSciBench evaluate executable task completion and intermediate or programmatic evidence rather than relying only on final narrative output.[4-6]

The clinical data analysis evaluation by Wu and colleagues further supports separating analytical planning from implementation and execution because an apparently appropriate plan did not ensure a correct implemented analysis.[7]

These sources motivate the framework. They do not validate the exact gate definitions or severity categories used here. Those are investigator-defined components of the study.

## 17. Planned adjudication record

For each primary run, the fidelity record will eventually contain:

| Field | Description |
|---|---|
| Run ID | Unique run identifier |
| Condition | W0 through W5 |
| Model configuration | Eligible consumer configuration and access epoch |
| Gate status | PASS, FAIL, or UNCERTAIN for each gate |
| Critical findings | Findings that affect primary completion |
| Major findings | Findings that materially affect secondary outcomes or interpretation |
| Minor findings | Limited noncritical defects |
| Numerical status | Primary reference-equivalence status |
| Interpretation status | Interpretation gate status |
| Intervention status | Human scientific intervention status |
| Resource status | Access or resource event status |
| Repair history | Detection, repair and post-repair state |
| Terminal state | Final run classification |

This record will be implemented only after the numerical reference criteria, run schema, and prompt/interaction schema have been frozen.

## References

1. Collins GS, Moons KGM, Dhiman P, Riley RD, Beam AL, Van Calster B, et al. TRIPOD+AI statement: updated guidance for reporting clinical prediction models that use regression or machine learning methods. BMJ. 2024;385:e078378. doi:10.1136/bmj-2023-078378.

2. Gallifant J, et al. The TRIPOD-LLM reporting guideline for studies using large language models. Nat Med. 2025;31(1):60-69. doi:10.1038/s41591-024-03425-5.

3. Moons KGM, Damen JAA, Kaul T, et al. PROBAST+AI: an updated quality, risk of bias, and applicability assessment tool for prediction models using regression or artificial intelligence methods. BMJ. 2025;388:e082505. doi:10.1136/bmj-2024-082505.

4. Chen X, et al. ScienceAgentBench: Toward Rigorous Assessment of Language Agents for Data-Driven Scientific Discovery. ICLR. 2025.

5. Starace M, et al. PaperBench: Evaluating AI's Ability to Replicate AI Research. Proc Mach Learn Res. 2025;267:56843-56873.

6. Zhang Y, et al. DataSciBench: Benchmarking Large Language Models for Data Science Tasks. Findings of the Association for Computational Linguistics. 2026:3685-3728. doi:10.18653/v1/2026.findings-acl.181.

7. Wu et al. Performance, Failures, and Oversight of a Large Language Model Agent for Clinical Data Analysis: Evaluation Study. J Med Internet Res. 2026;28:e99597. doi:10.2196/99597.

## Evidence status

The external literature supports process-aware, execution-based and configuration-specific evaluation of machine learning and LLM analytical systems.

The fidelity dimensions, gate adjudication rules, severity categories, primary completion rule, and repair accounting are investigator-defined components of this study.

No primary experimental results are included.
