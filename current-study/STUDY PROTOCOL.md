# Study Protocol

Status: Final protocol for pre-primary execution
Version: 1.0
Month: September 2026
Study phase: Pre-primary

## Protocol scope and companion records

This document is the authoritative integrated statement of the study design. It is intended to be understandable on its own without requiring a reader to reconstruct the study from the repository.

Detailed operational records are maintained in companion documents for reproducibility and version control. These include the reference analysis specification, workflow protocol, statistical analysis plan, resource plan, reproducibility record, provenance dictionary, failure taxonomy, interaction registry, prompt package, and sample-size simulation. They are linked by name where relevant. They are not treated as bibliographic sources and therefore are not numbered as Vancouver references.

The protocol contains the primary scientific question, objectives, design, eligibility rules, experimental conditions, endpoints, estimands, sample-size decision, execution controls, analysis framework, interpretation boundaries, and pre-primary gates. A companion document may contain greater implementation detail, but it does not silently change a protocol decision.

## 1. Study title

Workflow architecture and reference-faithful completion of biomedical machine learning analyses by zero-cost consumer-accessible general-purpose LLMs

## 2. Study rationale

General-purpose large language models are increasingly used to generate analytical code, perform statistical analyses, and support scientific workflows. Recent evaluations show that scientific workflow performance cannot be reduced to a final answer: execution failures, cohort errors, statistical mistakes, interpretation errors, and the quality of verification can differ within the same analytical trajectory.[1-4]

This study examines workflow architecture rather than asking whether a particular LLM is generally capable of data science.

The biomedical task is fixed. A PTB-XL ECG analysis is used as a controlled computational target. The LLM workflow, context structure, verification mechanism, and interaction burden are varied while the scientific information, execution substrate, resource boundary, and interpretation limits are held constant.

The use of zero-cost consumer access defines the study population and accessibility envelope. It is not itself the claimed novelty. Published work has already evaluated publicly accessible consumer LLMs, including free configurations.[4] The methodological question concerns the combination of a fixed biomedical machine learning target, controlled workflow architecture, end-to-end scientific fidelity, and an explicitly defined ordinary-user zero-cost access envelope.

TRIPOD-LLM provides the principal reporting basis for the LLM component, with additional reproducibility, software, data-provenance, and biomedical prediction-model guidance applied according to the roles defined in the companion documents.[5-9]

## 3. Research question

Under a locked biomedical machine learning analysis, does moving from a fully specified monolithic LLM workflow to a structured fresh-context workflow change end-to-end reference-faithful completion when both operate under the same zero-cost consumer access envelope?

## 4. Objectives

### 4.1 Primary objective

Estimate the difference in reference-faithful completion between W1, a fully specified monolithic workflow, and W2, a structured fresh-context workflow, among eligible zero-cost consumer LLM configurations.

### 4.2 Secondary objectives

Estimate the effects of instruction specificity by comparing W0 with W1.

Estimate the effect of self-audit by comparing W3 with W2.

Estimate the effect of deterministic validation by comparing W4 with W2.

Estimate the effect of an independent same-configuration LLM audit by comparing W5 with W2.

Characterize numerical fidelity to the locked biomedical reference analysis.

Characterize scientific failure, execution failure, resource or access failure, human scientific intervention, and recovery behaviour.

Describe observable interaction-resource use and the reproducibility of completed workflows.

The W2A and W2B information-exposure extensions remain outside the primary protocol because their information-exposure contrast requires a separate operational definition.

## 5. Scientific object

The experimental object is the analytical workflow.

The consumer LLM is treated as the analytical operator within the assigned workflow condition.

The biomedical scientific target, data definitions, cohort construction, model architecture, training configuration, evaluation metrics, statistical estimands, and interpretation boundaries are held constant across workflow conditions.

The workflow conditions may differ in:

- instruction structure;
- context continuity;
- context resets;
- handoff artifacts;
- self-audit;
- deterministic validation;
- independent auditing;
- bounded repair.

A difference in workflow outcome is therefore interpreted as a workflow-level observation within the eligible consumer configurations, not as evidence that one underlying model is intrinsically superior.

## 6. Study population

### 6.1 LLM configuration population

The primary population consists of general-purpose LLM configurations that an ordinary individual can access through a public consumer-facing online interface at zero monetary cost, with every capability required by the frozen workflow available through that zero-cost route.

Eligibility is configuration-specific.

The experimental identity includes:

- provider;
- consumer product;
- interface;
- plan;
- displayed model;
- model version where exposed;
- relevant capabilities;
- region;
- access month;
- access epoch;
- persistence and retrieval state.

Provider documentation current to the study preparation period shows that several mainstream products offer some combination of free consumer access, file handling, analysis or coding capabilities, but the presence of a nominal free plan is not sufficient for inclusion. OpenAI documents data analysis and file uploads on its Free tier with separate limits.[10,11] Google documents file upload and analysis in Gemini Apps without a Google AI plan, with rolling usage limits and lower limits than paid tiers.[12] Anthropic documents a $0 Free plan and current availability of code execution and file creation for Free users.[13,14] Mistral documents a Free plan with limited coding sessions and other capabilities, while its current documentation identifies some code-interpreter functionality as paid, so complete-workflow feasibility requires direct configuration testing.[15,16]

These provider records support candidate screening only. The primary configuration set is established by the direct access audit defined below.

### 6.2 Minimum configuration requirement

At least three eligible LLM configurations are required for the confirmatory primary W1 versus W2 comparison.

If fewer than three configurations satisfy all mandatory eligibility and primary-run feasibility requirements, the confirmatory primary comparison is not conducted. Available runs may be retained as descriptive feasibility evidence.

The final eligible set is not selected on the basis of observed analytical performance.

### 6.3 Excluded systems

The primary population excludes:

- API-only access;
- paid subscriptions;
- paid agents or paid orchestration products;
- institutional, enterprise, university, student, or researcher entitlements;
- promotional or trial access;
- local model deployments;
- downloaded open-weight models used locally;
- small language models selected for local execution;
- domain-specific biomedical models;
- configurations in which an essential primary capability requires payment.

## 7. Biomedical reference analysis

The fixed biomedical target is the PTB-XL v1.0.3 analysis defined in the [Reference Biomedical Analysis Protocol](08%20REFERENCE%20BIOMEDICAL%20ANALYSIS%20PROTOCOL.md).

The reference task contains:

- HYP versus NORM;
- MI versus NORM;
- PTB-XL records100 waveforms;
- 12 leads by 1,000 samples at 100 Hz;
- raw and record-wise global z-score representations;
- patient-aware folds 1 through 8 for training, 9 for validation, and 10 for testing;
- a compact direct-waveform 1D CNN;
- fixed training configuration;
- AUROC, average precision, Brier score, and calibration outputs;
- the primary cross-task representation-effect contrast;
- patient-level paired bootstrap uncertainty;
- prespecified sensitivity analyses.

The reference analysis is a scientific testbed, not clinical ground truth.

The reference study does not establish clinical utility, clinical benefit, causal biological information loss, prospective deployment performance, or general performance across other ECG datasets.

## 8. Reference execution gate

Primary LLM collection cannot begin until the reference analysis passes the following sequence.

### R0. Protocol implementation check

The executable reference implementation is reviewed against the written biomedical protocol.

### R1. Locked reference execution

The original reference implementation is executed under the documented environment.

### R2. Reference repeat

The original implementation is executed again under the same locked configuration to characterize repeatability.

### R3. Independent reimplementation

A second implementation is written from the scientific specification without receiving the original reference source code or numerical outputs in advance.

### R4. Independent comparison

R1, R2, and R3 are compared structurally and numerically.

### R5. Equivalence envelope

For each numerical outcome subject to reference comparison, the empirical reference variability is calculated from the maximum pairwise absolute discrepancy among compliant R1-R3 executions.

No arbitrary numerical tolerance is introduced.

### R6. Criterion freeze

The resulting numerical equivalence criteria are frozen in the primary study record before any primary LLM outcome is observed.

The primary reference estimate remains the result of the locked original reference implementation from R1. R2 and R3 establish the empirical variability envelope.

If any reference execution fails a critical structural requirement, the equivalence envelope is not frozen until the reference implementation is corrected and the reference comparison is repeated.

## 9. Information-exposure boundary

All workflow conditions receive the same scientific information.

The LLM does not receive the reference answer key.

### 9.1 Information exposed to all primary conditions

The frozen study package contains:

- scientific question;
- reference biomedical protocol;
- data dictionary;
- dataset access and file-structure information;
- allowed software environment;
- execution interface instructions;
- workflow-independent output schema;
- interpretation boundaries;
- required evaluation definitions.

The fixed model architecture and training configuration are therefore known to the LLM. The experimental question is whether it can execute the specified analysis, not whether it can infer an unspecified model.

### 9.2 Information withheld from primary conditions

The study package does not contain:

- reference source code;
- reference numerical results;
- reference bootstrap outputs;
- reference calibration outputs;
- reference final report;
- hidden deterministic validator implementation;
- previous LLM trajectories;
- previous workflow failures;
- post hoc corrections from other runs;
- outputs from another experimental condition.

The pre-execution cohort counts retained in the archived ECG study are not exposed as an answer key. The LLM must derive cohort membership and counts from the prescribed data and label rules.

### 9.3 External information controls

Primary runs are closed-book.

The LLM does not have:

- web search;
- external retrieval;
- external connectors;
- connected applications;
- uncontrolled remote browsing;
- prior study memory;
- personalization state;
- previous study artifacts.

A configuration that cannot provide the required information isolation is excluded from the primary comparison or is separately defined before any pooling.

The public availability of the archived ECG repository creates a residual possibility that aspects of the task or earlier scientific work may have been encountered during model training. The study does not claim contamination-free evaluation. The control is that experimental conditions are matched, external browsing is disabled, the reference answer key is withheld, and newly created primary prompts, validators, manifests, and numerical results are not published before primary collection is complete.

## 10. Standardized execution environment

All workflow conditions use the same logical computational substrate described in the [Reproducibility and Computational Environment](14%20REPRODUCIBILITY%20AND%20COMPUTATIONAL%20ENVIRONMENT.md).

The substrate provides a controlled workspace for:

- study package;
- data;
- environment;
- generated run artifacts;
- outputs.

The human operator transfers LLM-generated artifacts into the designated run area and launches the prescribed execution command.

The execution process records:

- exit status;
- stdout;
- stderr;
- generated files;
- runtime;
- environment identifier;
- repository or study-package version.

Provider-specific code-execution environments are not used as a hidden second execution substrate for the primary comparison.

Provider-side inference hardware and hidden token-level computation are not inferred when the consumer interface does not expose them.

## 11. Human operator boundary

The human operator is a mechanical interface between the consumer LLM and the standardized execution substrate described in the [Reproducibility and Computational Environment](14%20REPRODUCIBILITY%20AND%20COMPUTATIONAL%20ENVIRONMENT.md) and [Data Provenance and Data Dictionary](15%20DATA%20PROVENANCE%20AND%20DATA%20DICTIONARY.md).

Permitted actions include:

- opening the designated consumer context;
- entering a frozen prompt;
- uploading prescribed files;
- transferring generated artifacts;
- launching the prescribed command;
- returning permitted execution evidence;
- opening the next prescribed context;
- recording operational metadata.

Scientific assistance is prohibited.

Examples of prohibited scientific intervention include:

- modifying generated code;
- changing parameters;
- changing cohort definitions;
- correcting labels;
- selecting among competing implementations;
- telling the LLM what methodological error it made;
- prescribing an unplanned correction;
- selecting a favourable result.

A scientific intervention produces an intervention-assisted run and prevents classification as an autonomous primary success.

## 12. Workflow conditions

### W0. Minimal monolithic

W0 is a secondary instructional baseline.

The system receives one minimal initial instruction to execute the analysis specified in the study package.

The run remains within one context.

No explicit workflow stages, external audit, deterministic validator, or independent reviewer is supplied.

Ordinary execution feedback within the same context remains permitted.

### W1. Fully specified monolithic

W1 is the primary monolithic condition.

The complete workflow is explicitly specified in the initial prompt.

The analysis remains in one context.

No external verifier is supplied.

The scientific information, execution substrate, access envelope, and interaction ceiling are identical to W2.

### W2. Structured fresh context

W2 is the primary staged condition.

The workflow consists of five predefined stages:

1. data and provenance audit;
2. cohort and label construction;
3. analysis implementation;
4. execution and evaluation;
5. interpretation and reporting.

Each stage uses a fresh consumer context.

A structured handoff artifact is the only state transfer between stages.

The new context does not receive the preceding conversational history.

### W3. W2 plus self-audit

W3 follows W2 and adds one explicit self-audit context.

The audit examines the completed workflow against the locked scientific specification.

One bounded repair cycle is permitted.

The initial error remains recorded even when the repair succeeds.

### W4. W2 plus deterministic validation

W4 follows W2 and applies read-only deterministic validators to machine-checkable properties.

A validation finding may trigger one bounded repair cycle, followed by re-execution or revalidation as appropriate.

The validator does not expose the reference numerical answer key.

### W5. W2 plus independent LLM audit

W5 follows W2 and adds an independently initiated audit context using the same prespecified LLM configuration as the executor.

The auditor receives only the artifacts and evidence permitted by the W5 condition.

One audit cycle and one bounded repair cycle are permitted.

The auditor is independent in context and trajectory, not a different model population.

## 13. Interaction and resource ceiling

The primary workflow uses one common interaction ceiling.

A run may contain at most **32 LLM response turns** across all contexts associated with that run.

A model response counts as one LLM response event regardless of its length.

The ceiling applies equally to W1 and W2 and is retained for W0 and W3-W5 unless a secondary condition requires a documented condition-specific extension.

The ceiling is an investigator-defined operational boundary. It is intended to permit ordinary code generation, execution feedback, stage handoffs, verification, and bounded recovery without allowing indefinite interaction.

A run that reaches the ceiling before satisfying the primary terminal requirements is recorded as noncompletion.

The study does not purchase additional interaction capacity after a free-tier limit is encountered.

Observable resource outcomes include:

- LLM response turns;
- human turns;
- context transitions;
- file transfers;
- execution attempts;
- audit attempts;
- repair attempts;
- elapsed wall-clock time;
- free-tier limit events;
- quota interruptions;
- human mechanical time;
- human scientific intervention.

Resource burden is reported separately from scientific correctness.

## 14. Prompt and interaction control

Prompt text is a frozen experimental artifact.

Before primary collection:

1. canonical prompts for W0-W5 are finalized;
2. each prompt receives a version identifier;
3. the prompt package is integrity-identified;
4. the study package version is frozen;
5. the prompt version actually sent in each run is recorded.

Pilot prompt versions are never relabeled as primary versions.

A change to a primary prompt after collection begins constitutes a protocol amendment or deviation and does not silently replace the earlier prompt version.

The prompt, context, handoff and interaction records follow the registry defined in the [Prompt, Context and Interaction Registry](17%20PROMPT%20AND%20INTERACTION%20REGISTRY.md).

## 15. Randomization and blocking

The primary W1 versus W2 comparison uses randomized scheduling blocks within each eligible LLM configuration.

Each primary block contains:

- one W1 attempt;
- one W2 attempt.

The order of W1 and W2 is randomized before either run begins.

The block is a scheduling unit, not a paired biomedical observation.

The randomization is intended to reduce short-range confounding from provider state, browser state, quota state and other temporal operational changes.

Randomization is not stratified on outcome because outcomes are not known at assignment.

## 16. Primary sample size

The primary allocation is:

> **25 randomized W1/W2 blocks per eligible LLM configuration.**

The decision was based on the completed sample-size simulation in [SAMPLE SIZE SIMULATION.md](SAMPLE%20SIZE%20SIMULATION.md).

The simulation used three configurations as the minimum eligible set, W1 completion probabilities of 0.35, 0.50, and 0.65, a 25 percentage-point W2 minus W1 planning effect, configuration-specific effect heterogeneity of plus or minus 0.05, and within-block dependence of 0 and 0.25.

With 20 blocks per configuration, minimum simulated power across the alternative grid was 0.713.

With 25 blocks per configuration, minimum simulated power was 0.820, while the maximum simulated type I error across the evaluated null grid was 0.040.

The planning effect and scenario grid are investigator-defined. They are not predictions of the observed LLM effect.

If fewer than three configurations qualify for the primary experiment, the confirmatory primary comparison does not proceed.

The minimum primary allocation under three qualifying configurations is therefore 150 W1/W2 runs.

## 17. Secondary run allocation

Secondary conditions are allocated a fixed descriptive budget of **6 blocks per configuration**.

The W0 versus W1 contrast uses six blocks per configuration.

W3, W4, and W5 each use six blocks per configuration with W2 as their comparison condition.

These secondary allocations are not presented as powered confirmatory samples. They provide a fixed replication budget for workflow-specific failure and recovery analyses.

A secondary contrast is not promoted to confirmatory status on the basis of its observed result.

## 18. Primary endpoint

The primary endpoint is a binary run-level indicator of reference-faithful completion.

A primary run receives a value of 1 only when all of the following are satisfied:

1. eligible configuration and access state;
2. correct workflow condition;
3. correct dataset and data lineage;
4. correct cohort and labels;
5. correct patient-aware split;
6. correct representation and model;
7. correct training and evaluation procedures;
8. required analysis reaches terminal execution;
9. primary numerical fidelity gate passes;
10. interpretation gate passes;
11. required reproducibility evidence is present;
12. no unauthorized human scientific intervention occurred.

A run that reaches a free-tier quota, context limit, file limit, execution limit, or other resource barrier before satisfying these criteria receives 0 for the primary endpoint.

The immediate failure mechanism remains separately classified.

## 19. Reference numerical fidelity

The primary numerical fidelity gate concerns the primary cross-task AUROC representation-effect contrast.

For task t:

$$
\Delta_t =
AUROC_{normalized,t}
-
AUROC_{raw,t}
$$

The primary biomedical estimand is:

$$
\Delta_{HYP-MI}
=
\Delta_{HYP}
-
\Delta_{MI}.
$$

For an LLM run, the primary numerical error is:

$$
E_{\Delta}
=
\left|
\widehat{\Delta}_{HYP-MI}^{LLM}
-
\Delta_{HYP-MI}^{ref}
\right|.
$$

The primary reference value is the R1 locked reference execution.

The numerical equivalence criterion is the empirical reference envelope established at R5.

A numerically evaluable LLM run passes the primary numerical gate when:

$$
E_{\Delta}
\le
T_{\Delta}
$$

where $T_{\Delta}$ is the maximum pairwise absolute discrepancy observed among the compliant R1-R3 reference executions for the same estimand.

No arbitrary fixed numerical tolerance is introduced.

Secondary numerical discrepancies for AUROC, average precision, Brier score and calibration are reported continuously and are not converted into an aggregate numerical fidelity score.

## 20. Fidelity evaluation

Scientific fidelity is evaluated using the domains defined in the Scientific Fidelity Evaluation Framework.[8]

The critical audit sequence is:

1. configuration and access;
2. information exposure;
3. dataset identity and waveform structure;
4. cohort and label construction;
5. patient-aware split;
6. preprocessing and representation;
7. model architecture and training;
8. execution;
9. evaluation and statistical analysis;
10. numerical reference comparison;
11. interpretation;
12. reproducibility evidence.

Failure severity follows the Failure Taxonomy and Error Audit.

Clean success and recovered success remain distinct.

A numerical match cannot override a protocol violation.

Protocol fidelity cannot override failed primary numerical equivalence.

A plausible final narrative cannot override missing execution evidence.

## 21. Statistical analysis

### 21.1 Primary estimand

Let $m$ index eligible LLM configurations and $w$ index W1 or W2.

Let:

$$
p_{m,w}
=
P(Y=1\mid m,w)
$$

where $Y=1$ is reference-faithful completion.

For configuration m:

$$
\theta_m
=
p_{m,W2}
-
p_{m,W1}.
$$

The primary estimand is the equally weighted contrast:

$$
\theta
=
\frac{1}{M}
\sum_{m=1}^{M}
\theta_m.
$$

This estimand describes the prespecified eligible configuration set.

It is not a population-level effect across all current or future LLMs.

### 21.2 Primary estimator

For configuration m with $B_m$ completed randomized blocks:

$$
\hat{\theta}_m
=
\frac{1}{B_m}
\sum_{b=1}^{B_m}
\left(
Y_{m,b,W2}
-
Y_{m,b,W1}
\right).
$$

The overall estimator is:

$$
\hat{\theta}
=
\frac{1}{M}
\sum_{m=1}^{M}
\hat{\theta}_m.
$$

Each configuration therefore has equal weight.

### 21.3 Primary inferential test

The primary hypothesis test uses a two-sided stratified randomization test based on the randomized W1/W2 assignment within blocks.

Within each block, the W1 and W2 labels are randomly swapped or retained while the observed outcomes remain fixed.

The primary test statistic is $\hat{\theta}$.

The analysis uses 100,000 randomization draws with a fixed random-number seed of 314159.

The two-sided p-value uses the plus-one correction:

$$
p
=
\frac{
1+
\#\{
|T^*|\ge|T_{obs}|
\}
}{
100001
}.
$$

The primary alpha level is 0.05.

The randomization test is conditional on the prespecified eligible configuration set and does not support broader population inference.

### 21.4 Primary confidence interval

The primary 95 percent confidence interval is obtained by a stratified block bootstrap with 10,000 resamples.

Blocks are resampled with replacement within each eligible LLM configuration.

The equally weighted across-configuration estimator is recomputed for each bootstrap sample.

LLM configurations are not resampled because they are fixed experimental strata.

The bootstrap uses fixed random-number seed 271828.

The study reports the point estimate, 95 percent interval, and primary randomization-test p-value.

### 21.5 Missing and noncompleted runs

No statistical imputation is performed for the binary primary endpoint.

An initiated primary run is coded:

- 1 for reference-faithful completion;
- 0 for any terminal noncompletion.

Noncompletion includes:

- scientific or protocol failure;
- execution failure;
- resource or access failure;
- unauthorized scientific intervention;
- unresolved reproducibility failure.

A pre-initiation infrastructure failure that prevents the initial prompt from being delivered is recorded separately as a scheduled infrastructure failure and is included as noncompletion in sensitivity analysis rather than being treated as an LLM outcome.

### 21.6 Secondary contrasts

The following are prespecified secondary workflow contrasts:

- W0 versus W1;
- W3 versus W2;
- W4 versus W2;
- W5 versus W2.

Secondary contrasts are reported with effect estimates and confidence intervals when sufficiently evaluable.

Secondary p-values are not used as confirmatory evidence.

### 21.7 Secondary numerical outcome

For numerically evaluable runs:

$$
E_{\Delta}
=
\left|
\widehat{\Delta}_{HYP-MI}^{LLM}
-
\Delta_{HYP-MI}^{ref}
\right|.
$$

Report:

- median;
- interquartile range;
- prespecified quantiles;
- proportion of primary runs that are numerically evaluable.

No numerical error is imputed for a non-evaluable run.

No composite 0 to 100 numerical fidelity score is created.

### 21.8 Biomedical reference uncertainty

The reference analysis uses the patient-level paired percentile bootstrap with 5,000 resamples specified in the [Reference Biomedical Analysis Protocol](08%20REFERENCE%20BIOMEDICAL%20ANALYSIS%20PROTOCOL.md).

The same patient resampling structure is used for HYP and MI.

A one-class bootstrap draw for a task is rejected and resampled.

The reference bootstrap is a property of the biomedical analysis and is distinct from the block bootstrap used for the LLM workflow primary endpoint.

### 21.9 Multiplicity

The W1 versus W2 binary completion comparison is the only confirmatory hypothesis test.

The remaining workflow contrasts and numerical metrics are secondary.

No unplanned secondary analysis can be promoted to confirmatory status.

## 22. Secondary outcomes

Secondary outcomes include:

- numerical error in the primary biomedical estimand;
- task-specific AUROC error;
- average precision error;
- Brier score error;
- calibration discrepancy;
- protocol violation severity;
- critical, major and minor failure counts;
- resource and access failures;
- execution failures;
- unauthorized interventions;
- time to completion;
- interaction burden;
- repair attempts;
- repair success;
- post-repair regression;
- reproducibility evidence completeness;
- configuration-specific workflow effects.

Resource outcomes are summarized with distributional statistics appropriate to their measurement scale.

## 23. Pilot versus primary collection

Pilot runs are allowed before primary collection.

Pilot runs may be used to:

- test access eligibility;
- verify file transfer;
- verify the standardized execution substrate;
- verify prompt interpretation;
- test handoff artifacts;
- verify deterministic validators;
- identify workflow failures;
- determine whether the 32-turn ceiling is feasible.

Pilot runs are excluded from all primary and secondary outcome analyses.

Pilot findings may result in a protocol amendment before primary collection.

After primary collection begins:

- prompts are frozen;
- workflow conditions are frozen;
- sample size is frozen;
- eligibility criteria are frozen;
- the primary endpoint is frozen;
- the primary analysis is frozen.

Observed primary outcomes cannot be used to retune these components.

## 24. LLM access audit

Before primary collection, each candidate configuration is checked against the full eligibility specification.[3]

The audit records:

- provider;
- product;
- interface;
- region;
- access month;
- plan;
- displayed model;
- version where visible;
- payment requirement;
- institutional or researcher entitlement;
- trial or promotion status;
- file handling;
- code generation;
- permitted execution route;
- context capacity;
- usage limits;
- memory state;
- personalization state;
- retrieval and web state;
- connector state;
- primary-run feasibility.

The final primary set is frozen before any primary result is inspected.

An access epoch is created for a material change in:

- model identity;
- model family;
- tool capability;
- context capacity;
- free-tier limits;
- persistence;
- retrieval;
- file handling;
- execution capability.

Runs from distinct epochs are not silently pooled.

## 25. Reproducibility and provenance

Each run is linked to:

- configuration ID;
- access epoch;
- workflow condition;
- prompt version;
- study package version;
- context IDs;
- handoff artifacts;
- generated artifact IDs;
- execution records;
- environment ID;
- repository commit;
- failure IDs;
- resource records;
- terminal state.

The reproducibility record follows the computational-environment plan.

The data-provenance record follows the [Data Provenance and Data Dictionary](15%20DATA%20PROVENANCE%20AND%20DATA%20DICTIONARY.md).

The interaction registry records prompt, context and event history in the [Prompt, Context and Interaction Registry](17%20PROMPT%20AND%20INTERACTION%20REGISTRY.md).

## 26. Failure and recovery

The [Failure Taxonomy and Error Audit](16%20FAILURE%20TAXONOMY%20AND%20ERROR%20AUDIT.md) defines:

- terminal run states;
- critical, major and minor errors;
- data and cohort errors;
- method errors;
- statistical errors;
- execution errors;
- resource failures;
- human scientific intervention;
- context and state failures;
- false completion;
- reproducibility failures.

A W3, W4 or W5 repair does not erase the initiating error.

The study distinguishes:

- clean success;
- recovered success;
- scientific failure;
- execution failure;
- resource-limited noncompletion;
- unauthorized intervention;
- indeterminate outcome.

## 27. Interpretation boundaries

The study does not establish:

- clinical utility;
- clinical superiority;
- patient benefit;
- causal biological information loss;
- prospective deployment performance;
- general performance across other biomedical datasets;
- general LLM capability beyond the fixed task.

The reference biomedical analysis is not a clinical decision-support evaluation.

The LLM workflow is not evaluated in patient care.

A change in an ECG classification metric is not described as proof of clinical information loss.

A statistically significant workflow difference is interpreted only within the prespecified consumer configuration population and access envelope.

## 28. Reporting framework

The final study report will use TRIPOD-LLM as the primary LLM reporting framework.[5]

The biomedical prediction component will be reported with relevant TRIPOD+AI principles, with MINIMAR used as a supporting completeness framework.[6,7]

FAIR and FAIR4RS principles will guide research-object and software stewardship.[8,9]

PRISMA-S is relevant to the literature-search documentation layer rather than to the study as a systematic review.

STROBE and RECORD provide transferable principles for transparent secondary-data description but do not govern the full computational experiment.

DECIDE-AI, CONSORT-AI, and SPIRIT-AI are not governing frameworks because the study is not a live clinical evaluation or clinical trial.

The study will not claim blanket compliance with every reporting framework. Applicability remains modular and documented.

## 29. Data access and ethics

The study uses a publicly available secondary research dataset and does not recruit participants or collect new clinical data.

Raw PTB-XL files are not redistributed in the repository.

Dataset access, provenance, licensing and version-specific file structure follow the provider documentation and the Data Provenance and Data Dictionary.

Any release of generated artifacts is reviewed for licensing, privacy, provider terms, and redistribution restrictions.

## 30. Protocol changes

Before primary collection, substantive protocol amendments are recorded with:

- month;
- affected section;
- reason;
- evidence or investigator rationale;
- status before primary outcome observation.

After primary collection begins, any change to a primary endpoint, primary estimand, sample size, eligibility criterion, workflow definition, or primary statistical procedure is treated as a protocol deviation or amendment and is not silently incorporated into the original primary analysis.

Historical versions remain identifiable.

## 31. Pre-primary execution gates

The protocol is final with respect to study design.

Primary collection remains blocked until the following empirical gates pass:

### Gate A. Reference execution

R0 through R6 are complete and the numerical equivalence envelope is frozen.

### Gate B. Consumer access

At least three configurations pass the full eligibility audit and primary-run feasibility check.

### Gate C. Prompt freeze

[Prompt Package v1.0](PROMPT%20PACKAGE.md) is frozen and integrity-identified.

### Gate D. Workflow pilot

The 32-response interaction ceiling, handoff mechanism, standardized execution substrate, validators, and recording system pass feasibility testing.

### Gate E. Primary package freeze

The reference-blind LLM study package is frozen, including all permitted files and withheld information.

### Gate F. Registry validation

The Prompt, Context and Interaction Registry passes its own implementation checks.

No primary outcome can be used to determine any of Gates A-F.

## 32. Principal analysis package

The final study package consists of the following companion records:

- [Reference Biomedical Analysis Protocol](08%20REFERENCE%20BIOMEDICAL%20ANALYSIS%20PROTOCOL.md)
- LLM Workflow Experimental Protocol
- Workflow Conditions and Ablation Plan
- Scientific Fidelity Evaluation Framework
- Statistical Analysis Plan
- Resource Accounting and Accessibility Analysis
- [Reproducibility and Computational Environment](14%20REPRODUCIBILITY%20AND%20COMPUTATIONAL%20ENVIRONMENT.md)
- [Data Provenance and Data Dictionary](15%20DATA%20PROVENANCE%20AND%20DATA%20DICTIONARY.md)
- [Failure Taxonomy and Error Audit](16%20FAILURE%20TAXONOMY%20AND%20ERROR%20AUDIT.md)
- [Prompt, Context and Interaction Registry](17%20PROMPT%20AND%20INTERACTION%20REGISTRY.md)
- [SAMPLE SIZE SIMULATION.md](SAMPLE%20SIZE%20SIMULATION.md)
- [PROMPT PACKAGE.md](PROMPT%20PACKAGE.md)
- final reference implementation and environment records
- primary run manifests and execution logs

The integrated protocol serves as the front-facing synthesis. The companion documents retain the detailed operational definitions.

## 33. Evidence classification

The study distinguishes four evidence classes.

### Evidence fact

Directly supported by a peer-reviewed source, formal reporting standard, official dataset documentation, or current official provider documentation.

### Evidence-supported inference

A design conclusion derived by combining multiple relevant sources.

### Investigator-defined choice

A deliberate protocol decision made to isolate the scientific question when the literature does not prescribe one unique solution.

### Computed result

A result generated by executed code or simulation.

No investigator-defined choice is presented as if it were already established by the literature.

No computed result is written into the protocol as a study outcome.

## References

1. Chen Z, Chen S, Ning Y, Zhang Q, Wang B, Yu B, et al. ScienceAgentBench: Toward Rigorous Assessment of Language Agents for Data-Driven Scientific Discovery. Int Conf Learn Represent. 2025.
2. Kurjan A, Cribbs AP. FlowBench: separating planning, fault recovery and interpretation in agentic bioinformatics. bioRxiv. 2026. doi:10.64898/2026.06.12.731844.
3. Wu Y, Fu DJ, Zhou Y, Wagner SK, Keane PA. Performance, Failures, and Oversight of a Large Language Model Agent for Clinical Data Analysis: Evaluation Study. J Med Internet Res. 2026;28:e99597. doi:10.2196/99597.
4. Ruta MR, Gaidici T, Irwin C, Lifshitz J. ChatGPT for Univariate Statistics: Validation of AI-Assisted Data Analysis in Healthcare Research. J Med Internet Res. 2025;27:e63550. doi:10.2196/63550.
5. Gallifant J, Afshar M, Ameen S, et al. The TRIPOD-LLM reporting guideline for studies using large language models. Nat Med. 2025;31(1):60-69. doi:10.1038/s41591-024-03425-5.
6. Collins GS, Moons KGM, Dhiman P, et al. TRIPOD+AI statement: updated guidance for reporting clinical prediction models that use regression or machine learning methods. BMJ. 2024;385:e078378. doi:10.1136/bmj-2023-078378.
7. Hernandez-Boussard T, Bozkurt S, Ioannidis JPA, Shah NH. MINIMAR (MINimum Information for Medical AI Reporting): Developing reporting standards for artificial intelligence in health care. J Am Med Inform Assoc. 2020;27(12):2011-2015. doi:10.1093/jamia/ocaa088.
8. Wilkinson MD, Dumontier M, Aalbersberg IJJ, et al. The FAIR Guiding Principles for scientific data management and stewardship. Sci Data. 2016;3:160018. doi:10.1038/sdata.2016.18.
9. Barker M, Chue Hong NP, Katz DS, et al. Introducing the FAIR Principles for research software. Sci Data. 2022;9:622. doi:10.1038/s41597-022-01710-x.
10. OpenAI. ChatGPT Free Tier FAQ. Official help documentation. Accessed September 2026.
11. OpenAI. Data analysis with ChatGPT. Official help documentation. Accessed September 2026.
12. Google. Upload and analyse files in Gemini Apps. Official help documentation. Accessed September 2026.
13. Anthropic. Choose a Claude plan. Official help documentation. Accessed September 2026.
14. Anthropic. Create and edit files with Claude. Official help documentation. Accessed September 2026.
15. Mistral AI. Pricing. Official product documentation. Accessed September 2026.
16. Mistral AI. Code Interpreter. Official documentation. Accessed September 2026.

## Evidence status

The workflow decomposition, process-level evaluation, and attention to silent analytical failure are supported by recent scientific and clinical LLM workflow evaluations.[1-4]

TRIPOD-LLM supports configuration-specific reporting, prompt transparency, human oversight, quality-control documentation, and reproducibility.[5]

The PTB-XL scientific target and its fixed biomedical analysis specification are retained from the archived and current reference protocol.

The standardized computational provenance, data lineage, resource measurement, failure taxonomy, and interaction registry are defined in the companion study documents.

The primary sample-size allocation is a computed result from the study's investigator-defined simulation scenarios and is documented in the [SAMPLE SIZE SIMULATION.md](SAMPLE%20SIZE%20SIMULATION.md).

The exact W0-W5 prompt wording, eligible configuration list, reference numerical envelope, and primary execution logs are execution-stage artifacts and are not represented as completed study results in this protocol.
