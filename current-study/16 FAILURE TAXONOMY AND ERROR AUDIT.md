# Failure Taxonomy and Error Audit

## 1. Purpose

The failure record separates scientific errors from execution problems, resource limitations and unauthorized human assistance.

The aim is to make a completed-looking LLM analysis auditable at the level of what actually happened in the fixed PTB-XL reference task. A terminal response, successful process exit or plausible numerical result is not by itself evidence that the prescribed scientific task was completed correctly.

The taxonomy is designed around the fixed reference analysis, the workflow conditions, the fidelity framework and the reproducibility requirements.[1-4]

This separation is also supported by recent evaluations of language agents for scientific and clinical data analysis. ScienceAgentBench evaluates generated programs, execution and cost rather than relying on a single final answer. FlowBench separately evaluates planning, fault recovery, interpretation and end-to-end output fidelity. A recent clinical data-analysis study identified silent cohort, formula and statistical errors that were not reliably visible from runtime success or final numerical summaries.[5-7]

## 2. Failure and outcome concepts

Four concepts are kept separate.

### Scientific failure

The workflow produced a result that violates the prescribed scientific specification or evaluation procedure.

Examples include wrong labels, leakage, wrong preprocessing, wrong model architecture, wrong statistical method or unsupported interpretation.

### Execution failure

The workflow could not execute the intended computational step correctly.

Examples include syntax errors, missing packages, failed file transfer, corrupted output, process termination or a command that does not complete.

An execution failure becomes a scientific failure only when the resulting terminal analysis also violates a scientific requirement.

### Resource or access failure

The workflow cannot continue within the stated access and resource envelope.

Examples include free-tier quota exhaustion, context-capacity limits, unavailable file handling, platform restrictions or local infrastructure failure.

Resource failure is recorded separately from scientific failure because it measures a property of the experimental environment.

### Unauthorized human scientific intervention

The human operator supplied scientific assistance outside the prespecified mechanical interface role.

Examples include changing code, selecting between competing methods, correcting labels for the LLM, interpreting an error and prescribing the solution, or suppressing an unsuccessful run.

This category is recorded even when the resulting analysis is scientifically correct.

## 3. Terminal run states

Each completed or terminated run receives one terminal state.

| Terminal state | Definition |
|---|---|
| Clean success | All primary success criteria satisfied without an error requiring an authorized repair |
| Recovered success | An error occurred, but the prespecified workflow detected and repaired it within its allowed recovery mechanism and all final success criteria were satisfied |
| Scientific failure | The terminal workflow violates a critical or unresolved scientific requirement |
| Execution failure | Required execution cannot be completed and the cause is computational or operational rather than scientific |
| Resource-limited noncompletion | The workflow cannot complete within the defined access or resource envelope |
| Unauthorized intervention | Scientific assistance outside the prescribed human role occurred |
| Indeterminate | Available evidence is insufficient for a defensible classification |

An indeterminate run is not counted as a successful primary outcome.

A run may have more than one observed failure during its interaction history, but it receives one terminal state after the complete run record is reviewed.

## 4. Primary success criteria

A run can contribute a primary reference-faithful success only when all required criteria are satisfied.

The run must:

1. use the eligible consumer LLM configuration and prescribed access state;
2. use the assigned workflow condition;
3. preserve the required dataset, cohort, label and split definitions;
4. execute the required analysis;
5. satisfy the structural fidelity gates;
6. satisfy the frozen numerical equivalence criteria;
7. satisfy the interpretation requirements;
8. provide the required reproducibility evidence;
9. remain within the defined workflow and resource rules;
10. contain no unauthorized human scientific intervention.

A run that produces the expected numerical result through an unprescribed scientific method is not a successful reproduction.

A run that begins with an error but is correctly repaired through a permitted W3, W4 or W5 mechanism can qualify as recovered success.

## 5. Scientific error hierarchy

Scientific errors are classified by whether they invalidate the prescribed analysis.

### Critical scientific error

A critical error changes the identity of the scientific experiment or invalidates the primary result.

Examples include:

- wrong dataset version;
- wrong phenotype task;
- wrong target or NORM label definition;
- substantial cohort construction error;
- patient leakage across primary folds;
- use of held-out test data for model selection;
- wrong primary waveform representation;
- materially different model architecture;
- materially different training objective or evaluation procedure;
- changing the primary estimand;
- fabricating, inventing or selectively reporting numerical results;
- interpreting a non-completed analysis as completed;
- use of information that was prohibited by the workflow condition;
- unresolved reference-agreement failure.

A terminal critical error prevents primary success unless the error is corrected through the explicitly permitted workflow mechanism before the terminal state is reached.

### Major scientific error

A major error affects an important analytical component but does not necessarily redefine the entire study.

Examples include:

- wrong bootstrap unit;
- incorrect paired-resampling implementation;
- incorrect metric definition;
- wrong checkpoint rule;
- incorrect training parameter;
- materially incorrect calibration calculation;
- failure to execute a required primary sensitivity analysis when that sensitivity analysis is part of the terminal condition;
- incorrect implementation of the primary numerical contrast;
- unrecorded change to a required execution setting.

A major error is not downgraded because the final numbers look plausible.

### Minor scientific error

A minor error does not materially change the prescribed computation or interpretation.

Examples include:

- nonessential metadata omission;
- naming inconsistency that does not alter provenance;
- a presentation defect that does not change the reported computation;
- missing nonessential documentation where the underlying evidence remains available.

Minor errors remain in the run record.

## 6. Data and cohort error classes

Data fidelity is evaluated before downstream numerical comparison.[1,3,8]

### D1. Dataset identity error

The wrong dataset, release, version or waveform collection is used.

### D2. Source-file error

A required metadata or waveform file is missing, substituted, misread or taken from an unapproved source.

### D3. Waveform schema error

Lead count, sample count, sampling frequency, signal structure or unit handling differs from the reference definition.

### D4. Cohort construction error

Records are incorrectly included, excluded or assigned to the wrong phenotype task.

### D5. Label derivation error

The SCP mapping, target likelihood, NORM likelihood, threshold rule or target-plus-NORM handling is implemented incorrectly.

### D6. Split error

Patient-aware fold assignments are not preserved or the held-out test population is altered.

### D7. Identifier contamination

Patient or ECG identifiers, record order or another identifier-derived feature is used as a model predictor.

### D8. Missingness or coding error

A missing value, unknown source value or provider-specific coding convention is silently reinterpreted.

The data dictionary and provenance record define the expected source and derived fields.[8]

## 7. Method and computational error classes

### M1. Representation error

The raw or normalized representation does not match the prescribed waveform construction.

Examples include unrequested resampling, filtering, denoising, clipping, augmentation or a different normalization scope.

### M2. Preprocessing error

A preprocessing operation is added, removed or ordered differently from the reference definition.

### M3. Architecture error

The model differs from the locked architecture in a material way.

Changing the model merely because it is expected to perform better is not permitted.

### M4. Training error

The optimizer, loss, learning rate, weight decay, batch size, stopping rule, checkpoint rule, seed or class-weighting configuration differs from the prescribed condition without authorization.

### M5. Evaluation error

The wrong prediction set, metric implementation, calibration procedure, task contrast or uncertainty procedure is used.

### M6. Statistical error

The statistical analysis does not implement the frozen SAP.

Examples include incorrect patient-level resampling, incorrect bootstrap pairing, incorrect rejection of one-class bootstrap replicates, incorrect confidence-interval construction or use of an unprespecified inferential procedure.

### M7. Interpretation error

The numerical analysis is acceptable, but the final scientific statement is not.

Examples include unsupported causal language, treating NORM as equivalent to healthy status, claiming clinical utility, ignoring uncertainty, reversing the direction of an effect, or presenting an exploratory finding as prespecified.

## 8. Leakage and information-exposure errors

Information exposure is a separate audit dimension because the same underlying error can arise through different mechanisms.

The following exposures are critical unless explicitly permitted by the assigned workflow condition:

- reference numerical results;
- reference source code when the condition requires independent generation;
- hidden validation code;
- previous LLM trajectories;
- post hoc corrections from another run;
- test-set performance used to guide development;
- prohibited web or retrieval access;
- prohibited memory or personalization state;
- connected applications or external sources;
- information transferred from another experimental condition.

The data-provenance record identifies which source and derived objects were exposed to each workflow.[8]

The consumer-eligibility and workflow documents define which access and persistence states are admissible.[9,10]

## 9. Execution failure classes

Execution failures are recorded even when the scientific design is otherwise correct.

### E1. Environment failure

Missing dependency, incompatible library, unavailable runtime or other environment problem.

### E2. File or transfer failure

Required file cannot be uploaded, copied, read or returned correctly.

### E3. Command failure

The prescribed command cannot execute because of a syntax, path, permission or process problem.

### E4. Runtime failure

The analysis process terminates unexpectedly, times out or exceeds the permitted execution boundary.

### E5. Output-integrity failure

Expected outputs are missing, truncated, corrupted or cannot be linked to the execution that produced them.

### E6. Evidence-capture failure

The scientific computation may have completed, but the required provenance evidence was not preserved.

A completed analysis with inadequate provenance is not automatically a successful primary run because reproducibility evidence is part of the endpoint definition.

## 10. Resource and access failure classes

Resource failures are logged using the observable interaction measures established in the resource plan.[11]

### R1. Quota or rate-limit failure

The consumer service prevents further interaction within the permitted access envelope.

### R2. Context-capacity failure

The workflow cannot continue because the available context capacity is insufficient for the assigned condition.

### R3. File-capability failure

Required file upload, download or artifact exchange is unavailable under the eligible free configuration.

### R4. Feature-access failure

A capability required by the assigned condition is unavailable in the eligible configuration.

### R5. Local infrastructure failure

The standardized execution environment becomes unavailable because of the investigator's computational infrastructure.

### R6. Access-epoch change

A provider-side change materially alters the experimental configuration during an active run.

A resource-limited noncompletion is not reclassified as a scientific failure merely because the primary endpoint was not reached. The two statements are recorded separately.

## 11. Human intervention classes

Human actions are classified as mechanical or scientific.

### H1. Mechanical action

Allowed actions include:

- opening the designated consumer context;
- entering a frozen prompt;
- uploading prescribed files;
- copying generated artifacts;
- launching the prescribed execution command;
- returning permitted execution evidence;
- opening the next prescribed context;
- recording operational information.

### H2. Scientific intervention

Examples include:

- modifying generated code;
- changing a model parameter;
- changing a label rule;
- changing the cohort;
- selecting the preferred implementation;
- diagnosing the scientific problem for the LLM;
- supplying an unprescribed methodological correction;
- selecting a favorable result;
- deciding to rerun only after observing an unfavorable result.

Any H2 event is recorded as unauthorized scientific intervention unless that repair was explicitly part of the assigned workflow condition.

## 12. Context and state errors

The staged conditions depend on controlled context transitions.

### C1. Context loss

Required information is omitted or corrupted during a handoff between stages.

### C2. Context contamination

A stage receives information that the condition does not permit.

### C3. State persistence

Memory, personalization, retrieval, connected applications or another persistent state carries information from a prior run or context when that state should be absent.

### C4. Wrong-context execution

A file, result or instruction from another condition, run or stage is used.

### C5. Handoff identity error

A generated artifact cannot be confidently linked to the stage and run that produced it.

These failures are distinct from ordinary code errors because they concern the workflow architecture itself.

## 13. Repair and recovery audit

Every error that triggers a repair mechanism is recorded as an event.

The repair record should state:

| Field | Required information |
|---|---|
| Error ID | Unique failure identifier |
| Detection stage | Stage or condition where error was detected |
| Error class | Taxonomy code |
| Severity | Critical, major or minor where applicable |
| Detection source | LLM, deterministic validator, independent auditor or execution system |
| Initial evidence | Artifact or log supporting the finding |
| Repair permitted | Yes or no under the assigned condition |
| Repair action | Exact authorized response |
| Re-execution required | Yes or no |
| Repaired artifact | Version or integrity identifier |
| New error introduced | Yes or no |
| Final status | Recovered or unresolved |

The study does not treat successful repair as equivalent to error-free execution.

A clean success and a recovered success therefore remain separate terminal states.

## 14. False completion

False completion is a distinct failure class.

It occurs when the workflow presents an analysis as complete even though required evidence shows that one or more essential components were not completed, were not run, or were not valid.

Examples include:

- claiming that the model was trained when the training process did not complete;
- reporting numerical metrics without evidence of the corresponding evaluation execution;
- describing a sensitivity analysis that was not actually run;
- reporting a successful repair without re-executing the affected step;
- presenting a plausible numerical value when its provenance cannot be established;
- reporting a complete interpretation despite an unresolved critical protocol violation.

False completion is particularly important because a successful conversational response can conceal an incomplete computational workflow. Recent scientific-agent and clinical data-analysis evaluations have reported cases in which plausible outputs failed to reveal underlying execution or methodological problems.[5-7]

## 15. Reproducibility failure

A run can be scientifically correct but insufficiently reproducible.

A reproducibility failure includes:

- missing environment specification;
- untracked source changes;
- missing prompt or context information;
- inability to identify the model or access epoch;
- missing input or output provenance;
- missing execution logs;
- inability to identify which artifact generated the reported result;
- inability to reconstruct the computational state.

This classification does not automatically imply that the underlying scientific calculation was wrong.

It means the evidence needed to inspect or reproduce it is inadequate.[2-4]

## 16. Interpretation audit

The final scientific report is audited separately from the numerical outputs.

At minimum, verify:

- the task is named correctly;
- the representation comparison is described correctly;
- the primary estimand is reported correctly;
- uncertainty is reported;
- the direction of the numerical contrast is correct;
- the distinction between NORM and healthy is maintained;
- no causal effect is claimed;
- no clinical utility or patient benefit is claimed;
- exploratory findings are identified as exploratory;
- protocol deviations and unresolved failures are disclosed;
- numerical claims trace to the preserved execution outputs.

A report that contains correct numbers but an incorrect scientific conclusion is an interpretation failure.

## 17. Audit order

The audit should proceed from upstream inputs to downstream interpretation.

1. Configuration and access eligibility
2. Information exposure and context state
3. Dataset and source-file identity
4. Cohort and label construction
5. Patient-aware split
6. Representation and preprocessing
7. Model architecture and training
8. Execution integrity
9. Evaluation and statistical analysis
10. Numerical reference comparison
11. Interpretation
12. Reproducibility evidence

This ordering reduces the risk of spending interpretive effort on a result that has already failed an upstream scientific requirement.

An upstream critical failure does not disappear because downstream numerical outputs happen to agree with the reference.

## 18. Evidence hierarchy for adjudication

When classifying a failure, the strongest available evidence is preferred.

The hierarchy is:

1. deterministic validator output;
2. execution log and machine-generated artifact;
3. preserved input or output manifest;
4. source file or generated code inspection;
5. preserved LLM interaction record;
6. final LLM narrative.

A final narrative assertion cannot override contradictory execution evidence.

If two evidence sources conflict, the run is not classified as a clean success until the discrepancy is resolved.

## 19. Relationship to the scientific fidelity framework

The failure taxonomy supplies error codes for the fidelity domains already defined in the study.[1]

| Fidelity domain | Primary failure families |
|---|---|
| Data fidelity | D1-D8 |
| Protocol and method fidelity | M1-M4 |
| Statistical fidelity | M5-M6 |
| Numerical fidelity | Evaluation and reference-agreement failures |
| Interpretive fidelity | M7 and interpretation audit failures |
| Reproducibility | Evidence-capture and reproducibility failures |
| Workflow integrity | C1-C5 |
| Resource/accessibility | R1-R6 |
| Human oversight | H1-H2 |

The taxonomy is therefore an audit vocabulary, not an additional composite score.

No single numerical “error score” is created.

## 20. Relationship to workflow conditions

The taxonomy must be interpreted in light of the assigned workflow condition.

For W1, a problem that can be corrected within the allowed monolithic interaction remains part of the run's error history.

For W2, stage handoff errors are recorded separately because fresh-context staging is part of the condition.

For W3, self-audit detection and repair are outcomes of interest.

For W4, deterministic validator detection and repair are outcomes of interest.

For W5, independent audit detection and repair are outcomes of interest.

The existence of a repair mechanism does not make the initial error disappear from the record.

This distinction allows the study to ask not only whether a workflow eventually succeeds, but also whether it detects and corrects specific failure classes.

## 21. Adjudication rules

A run should be classified conservatively.

The following rules apply:

- unresolved critical scientific errors prevent primary success;
- unresolved major errors prevent primary success when they affect a required primary component;
- resource-limited noncompletion is not recoded as a scientific error solely because the endpoint was not reached;
- unauthorized scientific intervention prevents classification as autonomous primary success;
- insufficient evidence prevents a clean-success classification;
- a permitted repair can convert an initial failure into recovered success only when the repair itself is documented and the affected analysis is successfully re-executed;
- a numerical match does not override a protocol failure;
- protocol fidelity does not override failed numerical agreement where numerical agreement is required;
- a plausible final report does not override missing execution evidence.

The final handling of ambiguous cases and any requirement for independent second adjudication will be frozen in the integrated study protocol before primary collection.

## 22. Historical development evidence

The archived ECG research phase provides concrete examples of why this taxonomy is needed.

During development of the earlier study, the repository history included changes to the primary label rule, transition from simpler models to a direct-waveform CNN, and a later correction of an implementation or test-fixture inconsistency after archival relocation. Those events are historical development records and are not outcomes of the current LLM study.

They nonetheless demonstrate the practical distinction between:

- a scientific specification changing;
- an implementation not matching the specification;
- a test fixture not matching the implementation;
- a later audit detecting the discrepancy.

The active study therefore treats versioned specifications, deterministic tests and preserved correction history as part of the error-audit design rather than assuming that a polished final repository is self-validating.[12,13]

## 23. Evidence basis

The distinction between task-level correctness, execution behaviour and end-to-end completion is consistent with ScienceAgentBench, which evaluates generated scientific programs through execution and multiple task-level metrics rather than relying only on final prose.[5]

FlowBench supports separating planning, fault recovery, interpretation and end-to-end fidelity because these capabilities can fail independently, and reports cases where repair mechanisms do not necessarily improve structural quality.[6]

Recent clinical data-analysis evaluation similarly demonstrates silent cohort, formula and statistical errors, including cases where outputs appeared plausible despite underlying methodological problems, supporting explicit audits of cohort logic, statistical implementation and narrative concordance.[7]

TRIPOD-LLM provides the reporting basis for preserving model identity, prompting, human oversight, outputs and quality-control information for LLM evaluations.[2]

The exact taxonomy codes, severity boundaries, terminal states, audit order and adjudication rules are investigator-defined components of the present study.

No primary experiment results are included.

## References

1. Scientific Fidelity Evaluation Framework. current-study/11 SCIENTIFIC FIDELITY EVALUATION FRAMEWORK.md. Study repository; 2026.
2. Gallifant J, Afshar M, Ameen S, et al. The TRIPOD-LLM reporting guideline for studies using large language models. Nat Med. 2025;31(1):60-69. doi:10.1038/s41591-024-03425-5.
3. Reproducibility and Computational Environment. current-study/14 REPRODUCIBILITY AND COMPUTATIONAL ENVIRONMENT.md. Study repository; 2026.
4. LLM Workflow Experimental Protocol. current-study/09 LLM WORKFLOW EXPERIMENTAL PROTOCOL.md. Study repository; 2026.
5. Chen Z, Chen S, Ning Y, et al. ScienceAgentBench: Toward Rigorous Assessment of Language Agents for Data-Driven Scientific Discovery. International Conference on Learning Representations; 2025.
6. Kurjan A, Cribbs AP. FlowBench: separating planning, fault recovery and interpretation in agentic bioinformatics. bioRxiv. 2026. doi:10.64898/2026.06.12.731844.
7. Wu Y, Fu DJ, Zhou Y, et al. Performance, Failures, and Oversight of a Large Language Model Agent for Clinical Data Analysis: Evaluation Study. J Med Internet Res. 2026;28:e99597. doi:10.2196/99597.
8. Data Provenance and Data Dictionary. current-study/15 DATA PROVENANCE AND DATA DICTIONARY.md. Study repository; 2026.
9. Consumer LLM Eligibility Specification. current-study/07 CONSUMER LLM ELIGIBILITY SPECIFICATION.md. Study repository; 2026.
10. Workflow Conditions and Ablation Plan. current-study/10 WORKFLOW CONDITIONS AND ABLATION PLAN.md. Study repository; 2026.
11. Resource Accounting and Accessibility Analysis. current-study/13 RESOURCE ACCOUNTING AND ACCESSIBILITY ANALYSIS.md. Study repository; 2026.
12. Study Protocol. archive/ecg-amplitude-normalization/01 STUDY PROTOCOL.md. Study repository archive; 2026.
13. Research Log. archive/ecg-amplitude-normalization/13 RESEARCH LOG.md. Study repository archive; 2026.
