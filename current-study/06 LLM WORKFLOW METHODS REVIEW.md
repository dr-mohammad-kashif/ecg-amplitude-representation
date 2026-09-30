# LLM Workflow Methods Review

## Scope

This review examines methodological evidence relevant to the use of general purpose large language models for scientific and biomedical data analysis.

The focus is the workflow around the model rather than model capability alone. The review covers prompting, code generation, tool use, context structure, staged execution, fresh contexts, self-reflection, deterministic validation, independent auditing, bounded repair, agent harnesses, process-level evaluation, human oversight, and reproducibility.

The active study uses this literature to define the methodological background for its workflow conditions. The exact W0 to W5 architecture remains an investigator-defined experimental design and is not presented as a structure established by any single prior study.

## 1. LLMs as scientific data-analysis operators

General purpose LLMs can already perform substantial parts of a scientific data-analysis workflow.

ScienceAgentBench evaluated 102 scientific data-analysis tasks derived from 44 peer-reviewed publications across four disciplines. Tasks were converted into self-contained Python program targets and assessed using generated programs, execution results, and cost. The benchmark compared direct prompting with OpenHands and self-debugging frameworks and found that performance remained limited on end-to-end scientific programming tasks.[1]

DataSciBench extends this approach to challenging data-science tasks with complex evaluation criteria. Its Intention-Function-Code framework connects the intended operation, generated code, and executable outcome, allowing programmatic assessment rather than judging the final text alone.[2]

PaperBench moves from individual scientific analysis tasks to replication of published machine learning research. It evaluates 20 ICML 2024 papers using 8,316 individually gradable subtasks and hierarchical rubrics developed with the original paper authors.[3]

RECLAIM provides a recent resource-bounded research-reproduction benchmark. It fixes the target result and success criterion before execution, imposes GPU-hour budgets, and evaluates reproduction of claims from 100 NeurIPS 2025 papers. A separate language model grades logs and outputs rather than relying only on an agent's own report.[4]

These studies establish that executable scientific work, process evidence, resource accounting, and reference-based evaluation are already important objects of LLM research.

They also constrain the active study's framing. The scientific contribution cannot simply be that a general purpose LLM can write and execute biomedical analysis code.

## 2. Prompt specificity and analytical specification

Prompt construction can materially affect scientific data-analysis performance.

Ruta and colleagues evaluated ChatGPT on data processing, descriptive statistics, and inferential statistical tasks using multiple levels of prompt specificity. The inferential experiments compared basic, intermediate, and advanced prompts against expected results generated with conventional statistical software. Accuracy increased substantially as analytical specificity increased in that experimental setting.[5]

The same study conducted trials in new GPT-4 windows with memory disabled and recommended repeated trials, explicit prompts, verification, and transparency around the prompts used.[5]

This provides direct precedent for testing analytical specification separately from other workflow mechanisms.

The active design therefore retains a distinction between W0 and W1.

W0 is a minimal monolithic instruction with the complete scientific package supplied externally to the prompt.

W1 is a fully specified monolithic instruction that makes the analytical sequence explicit while keeping the interaction within one continuous context.

This comparison is investigator-defined. It isolates the effect of explicit workflow specification while attempting not to confound the experiment with withholding scientific information.

Prompt specificity should therefore not be treated as a trivial presentation detail. It is part of the experimental input and must be versioned.

## 3. Continuous context versus staged execution

Long multistep tasks introduce a second problem that is different from prompt specificity.

A continuous context can accumulate intermediate assumptions, execution failures, outdated state, and incorrect self-assessments. LongHorizon-Harness explicitly treats task-state management as a separate problem from task execution. Its Manage-Execute-Audit architecture maintains state outside the executor's context, uses fresh-context executors, and employs a read-only auditor to verify environment state before progress continues.[6]

Wu and colleagues provide a close clinical-data precedent from a different direction. Their 2026 clinical data-analysis evaluation separated five stages of a workflow, varied interaction modes and analytical specification, and repeated each configuration three times. They compared execution outputs with validated reference values and compared narrative reports with execution logs. The study found that a correct statistical analysis plan did not guarantee correct code execution, and that execution errors could persist across repetitions.[7]

These studies support the methodological value of separating analytical stages and preserving explicit state, while not establishing that staged execution will always outperform a continuous context.

That distinction is important for the active experiment.

The purpose of W2 is to test whether structured stage boundaries and fresh contexts change reference-faithful completion when the underlying scientific task is fixed.

## 4. Structured handoffs and state representation

A fresh context is useful only if the scientific state required by the next stage can be transferred accurately.

The active design therefore uses structured handoff artifacts rather than carrying raw conversation history from one stage to the next.

The intended flow is:

1. data and provenance audit;
2. cohort and label construction;
3. analysis implementation;
4. execution and evaluation;
5. interpretation and reporting.

Each stage receives the locked protocol and only the artifacts specified for that stage.

This resembles the explicit state-management approach in LongHorizon-Harness, where verified task state is maintained outside the executor context.[6] HealthFlow similarly maintains structured task context, execution traces, evaluator feedback, planning state, and governed experience memory rather than relying on an undifferentiated conversation history.[8]

The exact handoff schema is investigator-defined.

The reason for using a structured handoff is experimental rather than aesthetic. If a fresh-context condition simply receives an unbounded copy of the preceding conversation, context isolation is not meaningfully different from a continuous workflow.

The handoff artifact must therefore preserve the evidence required for the next stage while exposing less conversational state than the continuous baseline.

## 5. Workflow architecture and agent harness effects

Recent biomedical agent literature shows that the system surrounding the language model can materially affect performance.

BioMedAgent uses a self-evolving multi-agent architecture that chains biomedical tools into executable workflows and evaluates the system on 327 biomedical data-analysis tasks.[9]

BiomniBench makes this point directly at the process level. Its benchmark evaluates full agent trajectories against task-specific rubrics rather than judging only the final answer. The reported comparison across multiple agent harnesses found that harness choice could shift scores by more than the gap between successive model generations.[10]

HealthFlow uses an executor, planner, evaluator, reflector, governed memory, and external tools, and performs progressive ablation of these components. Its reported results show that different additions contribute differently across benchmark settings rather than functioning as a single undifferentiated increase in capability.[8]

Agentomics provides a biomedical ML example with strict validation checkpoints, repeated runs, containerized execution, and protection against test-set leakage and metric hallucination. It was evaluated across 20 biomedical datasets and reports three replicates per dataset.[11]

These studies establish that workflow scaffolding is itself an experimental variable in contemporary scientific-agent systems.

The active study therefore treats the workflow architecture as the primary experimental factor instead of interpreting the model or provider as the sole determinant of performance.

## 6. Self-reflection and self-audit

Self-reflection has a substantial prior literature.

Reflexion introduced a framework in which language agents use verbal feedback and reflective memory to change later decisions without updating model weights.[12] Self-Debugging similarly demonstrated that language models can inspect their own generated programs and use execution-related feedback to repair errors.[13] More recent empirical work has examined self-reflection directly and has reported performance improvements in some problem-solving settings.[14]

These studies close any claim that self-audit or self-reflection is itself a new mechanism.

The methodological question is more specific.

Does an explicit adversarial audit, performed after a staged biomedical ML workflow has completed, recover errors that remain in the completed artifacts?

The active W3 condition is designed to address this question.

W3 follows W2 through completion, then creates one fresh audit context containing the locked protocol, complete analytical artifacts, execution evidence, code, and results. It does not receive the executor's conversational history or its own earlier self-assessment.

The auditor classifies predefined audit items as PASS, FAIL, or UNCERTAIN.

One bounded repair cycle is permitted.

This structure is investigator-defined. It is informed by the prior reflection literature and by process-aware agent evaluation, but it is not copied from any single published system.

## 7. Deterministic validation

LLM self-assessment is not the same as deterministic validation.

A language-model auditor can reason about an implementation, but its evaluation is itself probabilistic. Deterministic validators can instead check properties that have an unambiguous machine-readable criterion.

CLEAR-Med is a recent clinical-data example. Its Invocation Agent generates executable SQL and retains the executed query and resulting data. Deterministic checks and a separately invoked validation agent then determine whether the result is accepted, repaired once, or rejected.[15]

Agentomics also uses explicit validation checkpoints during biomedical ML development, with execution artifacts and defined interfaces retained between stages.[11]

The active W4 condition isolates deterministic validation from self-audit.

W4 follows W2, then runs a read-only validator suite against machine-checkable properties of the analysis. Candidate checks include dataset structure, cohort membership, patient overlap, label construction, waveform dimensions, preprocessing parameters, model architecture, training configuration, metric implementation, bootstrap configuration, and expected output structure.

The validator returns PASS, FAIL, or NOT CHECKABLE.

It does not repair the analysis.

A predefined failure can trigger one bounded repair context, followed by revalidation.

The validator and repair rules are investigator-defined. Their scientific justification is that machine-checkable properties should be evaluated with deterministic rules where possible rather than delegating every verification task back to a language model.

## 8. Independent auditing

Independent auditing addresses a different failure mode from self-audit.

A model that generated an analysis may carry forward its own assumptions when asked to inspect that same analysis. A fresh auditor can be separated from the executor's reasoning history and given only the locked protocol and observable evidence.

LongHorizon-Harness explicitly uses a read-only auditor operating after fresh-context execution to verify environment state.[6]

CLEAR-Med likewise separates invocation and validation roles and uses a separately invoked validation agent in addition to deterministic checks.[15]

The active W5 condition uses the same LLM configuration for execution and auditing so that the primary comparison does not simultaneously change model identity and workflow role.

The auditor sees the final artifacts and protocol but not the executor's conversational history or self-assessment.

It classifies findings, records the evidence supporting each finding, and can trigger one bounded repair.

The role separation is investigator-defined. The underlying principle has clear precedent.

## 9. Why bounded repair is necessary

Unbounded self-correction creates a methodological problem.

A workflow allowed to continue indefinitely can use additional interactions, additional executions, or repeated re-analysis until it obtains an apparently acceptable result. This makes the condition difficult to compare with a workflow having a fixed resource envelope.

HealthFlow uses bounded within-task repair as part of its evaluator-guided control loop.[8] CLEAR-Med permits one bounded repair or abstention after validation.[15]

FlowBench provides an important counterpoint. It separates planning, fault recovery, biological interpretation, and end-to-end output fidelity rather than assuming that a single overall capability score is sufficient. Its analysis reports that workflow additions do not necessarily improve every dimension and that some validator-driven retry settings can worsen structural quality.[16]

The active design therefore limits W3, W4, and W5 to one audit or validation cycle and at most one repair cycle.

This does not imply that one repair is universally optimal. It is an investigator-defined resource and comparability constraint.

The important property is that the bound is fixed before primary runs.

## 10. Process-level evaluation is preferable to final-answer scoring

A recurring theme in scientific-agent research is that final answers can conceal how an analysis was obtained.

BiomniBench explicitly argues that outcome-only evaluation can give credit for a correct answer produced by an incorrect process or can penalize scientifically valid alternatives when only one reference answer is expected.[10]

ScienceAgentBench similarly evaluates generated programs, execution results, and cost rather than accepting natural-language answers alone.[1]

RECLAIM grades runs using logs and outputs, while PaperBench decomposes reproduction into gradable subtasks.[3,4]

This evidence supports the active study's decision to retain the full analytical trace as data.

A completed run must therefore preserve, where applicable:

- prompts and prompt versions;
- context boundaries;
- files exposed to the model;
- generated code;
- structured handoff artifacts;
- execution logs;
- validator outputs;
- audit findings;
- repair actions;
- final results;
- final interpretation;
- human interventions;
- resource and access failures.

The trace is not merely supplementary documentation. It is required to classify why a run succeeded or failed.

## 11. Scientific fidelity cannot be reduced to numerical performance

The recent clinical-data study by Wu and colleagues provides a direct example. Statistical analysis plans could be correct while implementation still contained errors, and narrative reports could sometimes appear satisfactory despite execution problems.[7]

BiomniBench similarly separates process dimensions such as method selection and interpretation from the final answer.[10]

The active study therefore distinguishes:

- data fidelity;
- cohort and label fidelity;
- representation fidelity;
- implementation fidelity;
- execution fidelity;
- statistical fidelity;
- numerical fidelity;
- interpretive fidelity;
- reproducibility;
- human intervention;
- resource and access failure;
- recovery behavior.

These dimensions are not combined into a single composite score.

A numerically close result can still represent an incorrect workflow.

Conversely, a scientifically faithful analysis can show a small numerical discrepancy because the reference implementation itself has finite computational variability.

The later fidelity framework will define the operational scoring and failure taxonomy.

## 12. Human oversight

TRIPOD-LLM treats transparency, human oversight, model configuration, prompting, evaluation settings, and reproducibility as essential reporting areas for LLM research in healthcare.[17]

The workflow literature also shows that a model can produce plausible but scientifically incorrect code or interpretation.[7]

The active study therefore treats human intervention as an explicit experimental variable rather than an invisible rescue mechanism.

Routine mechanical actions may be allowed within the eventual execution protocol, but scientific interventions must be recorded separately.

Examples of scientific intervention include changing a cohort definition, correcting a label rule, changing the statistical estimator, changing the model architecture, overriding an audit finding, or deciding that a failed run should be accepted.

An unrecorded scientific repair would convert an LLM failure into an apparent success and would compromise the comparison.

The exact human-intervention rules will be frozen in the LLM workflow experimental protocol.

## 13. LLM reproducibility and model identity

LLM systems are not static scientific instruments.

TRIPOD-LLM requires reporting model names and versions, relevant prompt engineering, evaluation settings, and whether the model was frozen or remained dynamic during data collection.[17]

The active study therefore treats each included consumer system as a configuration defined by more than a vendor name.

At minimum, a configuration record must identify:

- provider;
- interface;
- presented model identity;
- access tier;
- relevant capabilities;
- region;
- access date;
- configuration or settings that affect behavior;
- memory and personalization state;
- external tools or retrieval state;
- observed usage limits.

The same configuration must be used across workflow conditions within a replication stratum whenever technically possible.

Changes in provider behavior or presented model identity are handled as access-epoch changes rather than silently pooled with older runs.

## 14. Consumer interface versus agent framework

Many scientific-agent papers use specialized frameworks, API calls, local models, external tools, research harnesses, or paid infrastructure.

Those systems are relevant as workflow prior art but are not interchangeable with an ordinary consumer LLM interface.

The active study has a stricter access population.

An eligible system must be a general purpose LLM available through a public zero-cost consumer interface, and every capability essential to the prespecified workflow must be available within that consumer configuration.

A free underlying model used through a paid agent product does not qualify.

This is an investigator-defined population boundary.

The literature reviewed here therefore needs to distinguish three different objects.

1. The underlying language model
2. The consumer interface through which an ordinary user accesses it
3. The surrounding agent or research harness used to orchestrate the model

Conflating these objects would make provider comparisons difficult to interpret and would undermine the study's resource-access question.

## 15. Resource constraints are part of the workflow

A workflow with more contexts, validators, audits, and repair cycles can consume more interactions and more human time even when it improves scientific fidelity.

The active study therefore treats resource use as an outcome rather than as something to optimize away after the fact.

Candidate observable quantities include:

- LLM turns;
- context resets;
- audit turns;
- repair turns;
- execution attempts;
- wall-clock time;
- human mechanical time;
- human scientific interventions;
- access-limit failures;
- resource-limit termination.

Server-side token or compute consumption should be reported only when it is directly observable or reliably exposed by the interface.

The use of a zero-cost consumer interface therefore does not imply zero computational resource use. It defines monetary accessibility, while the study separately records observable resource burden.

ScienceAgentBench explicitly includes cost among its evaluation dimensions, and RECLAIM imposes GPU-hour budgets.[1,4] These studies provide precedent for resource-aware scientific-agent evaluation, although the active study uses a different resource envelope because it focuses on ordinary consumer access.

## 16. Contamination, memory, and hidden context

A consumer LLM interface may expose more information than the explicit study package.

Potential sources include persistent conversation memory, personalization, connectors, retrieval, browsing, uploaded files from earlier sessions, and hidden workspace state.

These features can create information exposure that differs between runs even when the visible prompt is identical.

The active protocol therefore intends to disable memory and personalization and to control retrieval, browsing, connectors, and other external information sources for the primary experiment wherever the interface permits this.

When an essential capability cannot be disabled or its state cannot be verified, that configuration must be excluded from the primary comparison or analyzed as a distinct configuration stratum.

This requirement follows from the experimental question rather than from a claim that external information is inherently undesirable.

The objective is to keep the information available to the workflow stable across conditions.

## 17. What the literature establishes and what remains open

The current evidence establishes that:

1. LLMs can perform executable scientific data-analysis tasks.[1,2]
2. Research reproduction can be evaluated with executable targets, reference criteria, and resource budgets.[3,4]
3. Prompt specificity can materially change analytical accuracy.[5]
4. Fresh contexts and externalized task state have been used to control long-horizon agent execution.[6]
5. Biomedical agents already use planners, evaluators, reflection, memory, tools, and validation.[8,9,10,11]
6. Self-reflection and self-debugging are established mechanisms.[12-14]
7. Deterministic checking and independent validation are established workflow components.[15]
8. Workflow components can have heterogeneous effects and may introduce new failure modes.[16]
9. LLM study reporting should document model identity, prompting, evaluation settings, oversight, and reproducibility information.[17]

The following remain investigator-defined:

1. W0 to W5 as the specific experimental condition set.
2. W1 versus W2 as the primary workflow comparison.
3. The five-stage W2 decomposition.
4. The exact structured handoff schema.
5. One audit cycle and at most one repair cycle for W3 to W5.
6. The deterministic validator suite used in W4.
7. Same-model auditing in W5.
8. The strict ordinary-user zero-cost consumer eligibility boundary.
9. The resource accounting variables available in the consumer interfaces.
10. The separation of workflow effects from model identity through fixed configuration strata.

These decisions are carried into the workflow experimental protocol rather than treated as already validated by the literature.

## References

1. Chen Z, Chen S, Ning Y, Zhang Q, Wang B, Yu B, et al. ScienceAgentBench: Toward rigorous assessment of language agents for data-driven scientific discovery. In: International Conference on Learning Representations; 2025.

2. Zhang D, Zhoubian S, Cai M, Li F, Yang L, Wang W, et al. DataSciBench: An LLM Agent Benchmark for Data Science. Findings of the Association for Computational Linguistics: ACL 2026. 2026:3685-3728. doi:10.18653/v1/2026.findings-acl.181.

3. Starace G, Jaffe O, Sherburn D, Aung J, Chan JS, Maksin L, et al. PaperBench: Evaluating AI's Ability to Replicate AI Research. Proc Mach Learn Res. 2025;267:56843-56873.

4. Salunkhe M, Ding H, Verma S, Kindratenko V. RECLAIM: Can Agents Reproduce the Claims of Machine Learning Papers? arXiv [Preprint]. 2026. doi:10.48550/arXiv.2609.28850.

5. Ruta MR, Gaidici T, Irwin C, Lifshitz J. ChatGPT for Univariate Statistics: Validation of AI-Assisted Data Analysis in Healthcare Research. J Med Internet Res. 2025;27:e63550. doi:10.2196/63550.

6. Ma Z, Huang H, Zou S, Wang Y, Yang S, Hu Y, et al. LongHorizon-Harness: Advancing Long-Horizon Agents for Real-World Tasks. arXiv [Preprint]. 2026. doi:10.48550/arXiv.2608.01964.

7. Wu Y, Fu DJ, Zhou Y, Wagner SK, Keane PA. Performance, failures, and oversight of a large language model agent for clinical data analysis: evaluation study. J Med Internet Res. 2026;28:e99597. doi:10.2196/99597.

8. Zhu Y, Wang Z, Qi Y, Gu L, Sui D, Hu H, et al. HealthFlow: automating electronic health record analysis via a strategically self-evolving multi-agent framework. NPJ Digit Med. 2026;9:660. doi:10.1038/s41746-026-03097-0.

9. Bu D, Sun J, Li K, He Z, Huang W, Hu J, et al. Empowering AI data scientists using a multi-agent LLM framework with self-evolving capabilities for autonomous, tool-aware biomedical data analyses. Nat Biomed Eng. 2026. doi:10.1038/s41551-026-01634-6.

10. Qu Y, Lu Y, Tu X, Zhang S, She T, Shaw AG, et al. BiomniBench: Process-level Evaluation of LLM Agents for Real-world Biomedical Research. bioRxiv [Preprint]. 2026. doi:10.64898/2026.05.12.724604.

11. Martinek V, Gariboldi A, Tzimotoudis D, et al. Agentomics: an agentic system that autonomously develops novel state-of-the-art solutions for biomedical machine learning tasks. Bioinformatics. 2026;42(Suppl 1):btag250. doi:10.1093/bioinformatics/btag250.

12. Shinn N, Cassano F, Berman E, Gopinath A, Narasimhan K, Yao S. Reflexion: Language Agents with Verbal Reinforcement Learning. arXiv [Preprint]. 2023. doi:10.48550/arXiv.2303.11366.

13. Chen X, Lin M, Schärli N, Zhou D. Teaching Large Language Models to Self-Debug. arXiv [Preprint]. 2023. doi:10.48550/arXiv.2304.05128.

14. Renze M, Guven E. Self-Reflection in LLM Agents: Effects on Problem-Solving Performance. arXiv [Preprint]. 2024. doi:10.48550/arXiv.2405.06682.

15. Dehkalani ED, Shankaran S, Laptook AR, Cotten CM, Grant PE, Ou Y. Large Language Models for Structured Clinical Data Analysis: Dual-Agent Grounding and Validation. arXiv [Preprint]. 2026. doi:10.48550/arXiv.2609.34039.

16. Kurjan A, Cribbs AP. FlowBench: separating planning, fault recovery and interpretation in agentic bioinformatics. bioRxiv [Preprint]. 2026. doi:10.64898/2026.06.12.731844.

17. Gallifant J, Afshar M, Ameen S, Aphinyanaphongs Y, Chen S, Cacciamani G, et al. The TRIPOD-LLM reporting guideline for studies using large language models. Nat Med. 2025;31(1):60-69. doi:10.1038/s41591-024-03425-5.
