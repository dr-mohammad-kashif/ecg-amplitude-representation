# Prior Art and Gap Analysis

**Status:** Working analysis  
**Version:** 0.1  
**Date:** 30 September 2026

## 1. Purpose and evidence boundary

The proposed study sits at the intersection of biomedical machine learning, LLM based scientific analysis, research reproducibility, workflow design, and resource accessibility. The prior art therefore needs to be examined at several levels.

The relevant question is not whether any single component has appeared before. Most individual components already have precedent. The question is whether the literature contains the same controlled combination of a fixed biomedical ML task, an executable reference analysis, a general purpose LLM acting as the analytical operator, controlled workflow conditions, a strict ordinary user zero cost access population, and multidimensional scientific fidelity evaluation.

This analysis is a current evidence boundary rather than a final claim of novelty. The literature search remains targeted and iterative. Failure to identify an exact precedent is not treated as proof that none exists.

## 2. Scientific data analysis is already established

ScienceAgentBench evaluates language agents on 102 data driven scientific tasks drawn from 44 peer reviewed publications across four disciplines. Each task is represented as a self contained Python target and evaluated using generated programs, execution results, and cost. The benchmark compares direct prompting, agent frameworks, and self debugging. [1]

DataSciBench extends this area to realistic data science tasks with complex evaluation criteria and execution based scoring. Its Intention Function Code framework links the intended operation, generated code, and executable outcome. [2]

These studies close broad questions such as whether an LLM can perform data analysis, generate executable scientific code, or complete realistic data science tasks.

The present study therefore cannot be framed as another general benchmark of LLM data science.

The methodological consequence is important. Execution artifacts, process evidence, and machine checkable outputs should be treated as research data rather than accepting a final narrative response as the endpoint.

## 3. Research reproduction is already established

PaperBench evaluates AI agents on replication of 20 ICML 2024 research papers using 8,316 individually gradable tasks. The benchmark uses hierarchical rubrics to decompose replication into explicit subtasks and evaluates both code production and execution. [3]

RECLAIM, released in September 2026, evaluates whether agents can reproduce claims from 100 NeurIPS 2025 papers. The target result and success criteria are fixed before execution, and runs are subject to GPU hour budgets. The benchmark distinguishes papers that provide code and weights from papers requiring retraining or reimplementation. A separate language model grades run logs and outputs. [4]

These studies close several potential novelty claims.

Reference based reproduction is not new.

Reproduction success rates are not new.

Resource bounded reproduction is not new.

Executable evidence for reproduction is not new.

The distinction relevant here is the experimental unit. The proposed study does not aim to reproduce many unrelated published papers. It uses one locked biomedical ML task so that workflow architecture can be manipulated while the scientific target stays fixed.

## 4. LLM based biomedical machine learning is already established

Tayebi Arasteh and colleagues used ChatGPT Advanced Data Analysis to develop machine learning models from real clinical datasets. The LLM generated models were compared with manually developed models after reimplementation and optimization. [5]

Gaudio and colleagues evaluated six LLMs from OpenAI, Anthropic, and Google for cell free RNA diagnostic biomarker discovery across three clinical cohorts. Their end to end experiments used training data followed by held out test data, fresh sessions, and repeated runs. [6]

These studies close the following formulations:

* Can an LLM build a biomedical prediction model?
* Can an LLM generate a machine learning pipeline from clinical data?
* Can repeated LLM sessions be used to assess biomedical ML consistency?
* Can LLM generated biomedical predictions be compared with conventional ML?

The present study should therefore not be framed as an LLM versus CNN comparison.

The LLM is the analytical operator.

The CNN and associated evaluation procedure are part of the fixed biomedical reference task.

## 5. Clinical analysis against validated reference outputs is already established

Wu and colleagues evaluated Claude across five stages of clinical data analysis using a public clinical dataset and validated reference code. The study compared Chat, Code, and Cowork interaction modes, varied the level of analytical specification, and repeated each condition three times for 27 runs. Execution outputs were compared with reference values, and reported results were checked against execution logs. [7]

This is a close methodological precedent. It demonstrates that a clinical LLM workflow can be evaluated against an independently defined reference while examining multiple workflow stages.

It also provides a reason to separate numerical agreement from scientific correctness. The study found that a good statistical analysis plan did not guarantee correct execution, and that clinically meaningful errors could survive into the reported analysis. [7]

The active study therefore cannot claim that reference based LLM clinical analysis is novel.

Its narrower proposed distinction is the use of a fixed biomedical ML target combined with an explicit workflow architecture comparison and a strict ordinary user zero cost population.

## 6. Biomedical agent systems already use planning, validation, reflection, and tools

BioMedAgent is a multi agent biomedical analysis framework that chains bioinformatics tools into executable workflows and evaluates them on a 327 task benchmark. The system performs cross omics analysis, machine learning modelling, and pathology image segmentation. [8]

HealthFlow, published in August 2026, combines an executor, EHR aware planner, evaluator, reflector, governed memory, and external tools. It performs progressive ablation by adding these components to an executor only baseline. [9]

Agentomics evaluates an autonomous biomedical machine learning agent against a zero shot LLM baseline. It uses repeated runs, prevents access to test portions during development, preserves action and code traces, and records LLM API expenditure. [10]

These papers establish that the following mechanisms are already part of the scientific agent literature:

* task decomposition;
* planning;
* evaluation agents;
* reflection;
* tool use;
* persistent memory;
* held out testing;
* repeated runs;
* action traces;
* resource measurement.

The active experiment therefore does not treat any of those mechanisms as a new engineering invention.

Instead, selected mechanisms become experimental factors.

## 7. Fresh context and independent auditing are already established

LongHorizon Harness explicitly separates execution context from verified task state. Its manager, fresh context executor, and read only auditor architecture uses externally verified state to determine what progress can be trusted. [11]

CLEAR Med, submitted in September 2026, separates an invocation agent from an independent validation agent. It retains executed SQL and the resulting data, applies deterministic checks, and permits one bounded repair or abstention. [12]

These studies close the claim that fresh context, independent auditing, deterministic validation, or bounded repair are individually new ideas.

The active design uses them differently. The question is whether these controls change fidelity when applied to the same locked biomedical ML experiment under the same access envelope.

## 8. Workflow effects should not be assumed to be positive

FlowBench evaluates agentic bioinformatics by separating planning, fault recovery, biological interpretation, and end to end output fidelity. Its purpose is partly to avoid collapsing independently failing capabilities into one metric. [13]

This is important for the present design because it argues against assuming that additional workflow structure automatically improves reliability.

The secondary conditions should therefore be treated as mechanistic tests:

W3 asks what self audit adds to W2.

W4 asks what deterministic validation adds to W2.

W5 asks what an independent LLM audit adds to W2.

The study should allow all three to show no benefit, a benefit, or a tradeoff between fidelity and resource burden.

## 9. Free consumer LLM access has been studied, but not in this exact setting

The zero cost population is a defining boundary of the proposed study, but it is not by itself a novelty claim.

Dinç and colleagues evaluated GPT 5.3 mini, Gemini 3 Flash, and Claude Sonnet 4.6 through free public web interfaces for parent education in pediatric immune thrombocytopenia. Their methods explicitly excluded paid subscriptions, enterprise versions, developer console access, APIs, retrieval augmented tools, plugins, browsing, uploaded documents, and customized clinical configurations. Model access date and configuration were recorded. [14]

These studies establish that genuinely free consumer LLMs can be treated as a distinct experimental population.

The study boundary therefore needs to be stated precisely:

> Eligible systems are general purpose LLMs accessible through public consumer facing online interfaces at zero monetary cost to an ordinary user, without API billing, paid subscriptions, institutional or researcher entitlement, special promotional access, local deployment, or paid agent products. All capabilities essential to the experimental workflow must be available within the qualifying free consumer configuration.

This excludes a common source of ambiguity in the literature. A free underlying model accessed through a paid agent product is not a free consumer workflow.

Current provider documentation confirms the practical distinction. ChatGPT Free provides data analysis and file uploads with separate tool limits. [15] Gemini provides file upload and analysis without an AI plan, with lower usage limits than paid plans. [16] Claude provides a Free consumer plan with code execution and file creation, while Claude Code, Claude Cowork, Claude Science, and Research are associated with paid plans. [17] Mistral provides a Free consumer plan with limited messages and coding access while separately offering paid plans and API services. [18]

The exact experimental eligibility of each provider remains a separate access audit.

## 10. PTB XL does not provide novelty by itself

PTB XL is an established public ECG dataset with 12 lead recordings, diagnostic annotations, and patient level metadata suitable for machine learning evaluation. [19]

The ECG analysis is therefore not proposed as a new biomedical discovery.

Its role is to provide a technically substantial reference problem with:

* structured clinical labels;
* repeated records per patient;
* a patient aware evaluation structure;
* direct waveform data;
* a fixed neural network;
* AUROC and average precision;
* Brier score;
* calibration;
* a cross task estimand;
* patient level bootstrap uncertainty.

These outputs remain important because a generic workflow benchmark would not demonstrate biomedical ML depth.

The scientific task stays fixed while the analytical workflow changes.

## 11. Prior art matrix

| Study element | Existing evidence | Current interpretation |
|---|---|---|
| LLMs performing biomedical ML | Tayebi Arasteh et al. [5] and Gaudio et al. [6] | Established |
| Repeated LLM biomedical ML runs | Gaudio et al. [6] | Established |
| Clinical analysis against reference values | Wu et al. [7] | Established |
| Scientific data analysis benchmarks | ScienceAgentBench [1], DataSciBench [2] | Established |
| Research reproduction benchmarks | PaperBench [3], RECLAIM [4] | Established |
| Biomedical multi agent analysis | BioMedAgent [8], HealthFlow [9] | Established |
| Biomedical ML agents with resource accounting | Agentomics [10] | Established |
| Fresh context execution | LongHorizon Harness [11] | Established |
| Independent auditing | LongHorizon Harness [11], CLEAR Med [12] | Established |
| Deterministic validation | CLEAR Med [12] and related systems | Established |
| Bounded repair | CLEAR Med [12] and related systems | Established |
| Workflow component ablation | HealthFlow [9], FlowBench [13] | Established |
| Free public consumer LLM evaluation | Dinç et al. [14], 2026 free and paid tier comparison [15] | Established |
| Zero monetary cost as a strict population boundary | Present in some recent studies, but with varying definitions [14,15] | Relevant boundary, not sufficient novelty |
| Same locked biomedical ML task across workflow regimes | No exact match identified in the targeted search | Candidate contribution |
| W1 versus W2 as a controlled workflow comparison | No exact match identified in the targeted search | Candidate contribution |
| Access envelope separated from workflow intervention | No exact match identified in the targeted search | Candidate contribution |
| Joint protocol fidelity and biomedical numerical fidelity under the same task | Adjacent evidence exists [7,13] | Candidate contribution |

The final four rows remain provisional. They are observations about the current search boundary, not evidence that the study is the first of its kind.

## 12. Why the strict free tier matters, and why it is not the whole novelty claim

The study's free access criterion does more than reduce financial cost.

It defines a reproducible population of systems available to an ordinary user without:

* paid model subscriptions;
* API credits;
* developer infrastructure;
* institutional accounts;
* researcher allocations;
* paid agent products;
* local hardware;
* specialised small language models.

That boundary matters because many recent agentic systems rely on infrastructure that is not available through the ordinary free consumer route. The analytical workflow available to a resource limited researcher can therefore differ substantially from the workflow evaluated in a research agent paper.

At the same time, recent studies have already shown that free consumer LLMs can be evaluated experimentally. [14,15]

The defensible contribution is therefore not:

> Free LLMs have never been studied.

Nor is it:

> Free access makes the experiment novel.

The narrower statement is:

> The experiment is restricted to a prespecified zero cost ordinary user population and asks whether workflow architecture changes the fidelity of a fixed biomedical ML analysis within that population.

The access criterion therefore strengthens the definition of the study population and resource envelope. It does not substitute for the scientific contribution.

## 13. Why a fixed within task design is scientifically important

Most prior systems change several variables simultaneously.

A benchmark may change the scientific question between tasks.

An agent study may change the model, tool environment, memory, planner, evaluator, and task.

A free tier comparison may change the provider and model.

A research reproduction benchmark may change the paper, dataset, architecture, software environment, and task objective from one run to another.

These designs answer their own questions, but they do not isolate the effect of workflow architecture on one fixed biomedical ML target.

The proposed study instead locks the scientific package.

The LLM must not redefine:

* the scientific question;
* the labels;
* the cohort;
* the train, validation, and test split;
* the signal representation;
* the model;
* the training procedure;
* the primary estimand;
* the uncertainty method;
* the interpretation boundaries.

The workflow is the controlled object.

This is why W1 versus W2 is more informative than a simple ChatGPT versus Gemini comparison.

## 14. Scientific fidelity versus numerical fidelity

The prior art strongly supports treating these as separate dimensions.

A run can produce an apparently plausible AUROC while violating the scientific protocol.

Examples include:

* using an incorrect cohort;
* allowing patient overlap across train and test;
* redefining the label;
* changing the preprocessing operation;
* changing the network architecture;
* selecting a checkpoint using test performance;
* calculating the wrong bootstrap unit;
* replacing the primary estimand with another metric.

Conversely, a scientifically faithful implementation can show a small numerical difference because of reference repeatability or implementation variability.

The reference analysis therefore must be executed, independently reproduced, and characterized before numerical agreement thresholds are selected.

This also means the study should not collapse all aspects of fidelity into a single 0 to 100 score. A binary end to end completion endpoint can coexist with separate continuous numerical error and categorical failure data.

## 15. What remains a candidate contribution

The present targeted search has not identified an exact published study that simultaneously contains all of the following:

1. one fixed biomedical ML task;
2. one independently established executable reference analysis;
3. repeated general purpose LLM runs;
4. a primary W1 versus W2 workflow architecture comparison;
5. W3 self audit, W4 deterministic validation, and W5 independent audit as secondary interventions;
6. a strict ordinary user zero cost population;
7. a standardized external execution substrate;
8. separate assessment of protocol fidelity and biomedical ML result fidelity;
9. explicit resource and access failure accounting.

This combination is narrower than the novelty claims already closed by the literature.

It should still be treated as provisional because the search is targeted rather than systematic, because new literature continues to appear, and because exact experimental overlap may be difficult to discover through terminology alone.

## 16. Claims that should not be made

The following statements are not supported:

* LLMs have never performed biomedical machine learning.
* LLMs have never reproduced predefined analyses.
* Workflow control is a new idea.
* Self audit is a new idea.
* Deterministic validation is a new idea.
* Independent auditing is a new idea.
* Free consumer LLMs have never been studied.
* The free tier alone makes the study novel.
* This is the first LLM research reproduction benchmark.

The current defensible position is more limited:

> Prior work has established LLM based biomedical ML, scientific data analysis evaluation, research reproduction, biomedical agents, workflow verification, and free consumer LLM evaluation. The targeted search has not identified the same controlled W1 versus W2 experiment on one locked biomedical ML task within a strict zero cost ordinary user population.

## 17. Remaining threats to the gap

### Search completeness

The search remains targeted. A later systematic search may identify additional overlap.

### Public task contamination

PTB XL and the archived ECG study are public. Prior exposure of the scientific task to an LLM cannot be ruled out.

### Provider drift

Consumer products can change model identity, limits, tools, and interaction behaviour. Access epochs must therefore be recorded.

### Interface confounding

The consumer system includes its visible interface and available tools. The experiment should treat this as part of the actual accessible system and document it rather than pretending all providers expose identical capabilities.

### Human intervention

A human repair that is not recorded can turn an LLM failure into an apparent success. Human scientific intervention therefore needs its own terminal classification.

### Reference variability

The reference analysis cannot be assumed to be deterministic merely because the protocol is fixed. Reference repeatability and independent implementation variability must be measured.

### Statistical dependence

Repeated runs under one LLM configuration are clustered observations rather than independent biological samples. The statistical plan must account for the workflow and configuration structure.

### Resource measurement

Consumer interfaces do not necessarily expose server side compute or token accounting. The study should measure observable interaction resources and report hidden infrastructure cost only when it is actually known.

## 18. Current gap statement

General purpose LLMs can already perform biomedical machine learning and clinical data analysis. Scientific benchmarks and research reproduction benchmarks already evaluate executable workflows. Biomedical agent systems already implement planning, tool use, reflection, validation, memory, and multistep execution. Free public consumer LLMs have also been evaluated in clinical settings.

The remaining candidate gap is narrower. The targeted search has not identified an exact study testing whether workflow architecture changes the reference faithful completion of one fixed biomedical machine learning analysis when the same scientific package, execution substrate, evaluation target, and strict ordinary user zero cost access envelope are maintained.

The candidate contribution therefore depends on the controlled combination of these elements rather than on any one of them.

The gap remains provisional until the dedicated search methods record, final literature update, and reference analysis are complete.

## References

1. Chen Z, Chen S, Ning Y, Zhang Q, Wang B, Yu B, et al. ScienceAgentBench: toward rigorous assessment of language agents for data-driven scientific discovery. In: International Conference on Learning Representations; 2025.

2. Zhang D, Zhoubian S, Cai M, Li F, Yang L, Wang W, et al. DataSciBench: an LLM agent benchmark for data science. Findings of the Association for Computational Linguistics: ACL 2026. 2026:3685-3728. doi:10.18653/v1/2026.findings-acl.181.

3. Starace G, Jaffe O, Sherburn D, Aung J, Chan JS, Maksin L, et al. PaperBench: evaluating AI's ability to replicate AI research. Proc Mach Learn Res. 2025;267:56843-56873.

4. Salunkhe M, Ding H, Verma S, Kindratenko V. RECLAIM: can agents reproduce the claims of machine learning papers? arXiv [Preprint]. 2026. doi:10.48550/arXiv.2609.28850.

5. Tayebi Arasteh S, Han T, Lotfinia M, Kuhl C, Kather JN, Truhn D, et al. Large language models streamline automated machine learning for clinical studies. Nat Commun. 2024;15:1603. doi:10.1038/s41467-024-45879-8.

6. Gaudio HA, Bliss A, Loy CJ, Eweis-LaBolle D, Gardella AE, De Vlaminck I. Benchmarking large language models for cell-free RNA diagnostic biomarker discovery. Nat Commun. 2026;17:7429. doi:10.1038/s41467-026-74077-x.

7. Wu Y, Fu DJ, Zhou Y, Wagner SK, Keane PA. Performance, failures, and oversight of a large language model agent for clinical data analysis: evaluation study. J Med Internet Res. 2026;28:e99597. doi:10.2196/99597.

8. Bu D, Sun J, Li K, He Z, Huang W, Hu J, et al. Empowering AI data scientists using a multi-agent LLM framework with self-evolving capabilities for autonomous, tool-aware biomedical data analyses. Nat Biomed Eng. 2026. doi:10.1038/s41551-026-01634-6.

9. Zhu Y, Wang Z, Qi Y, Gu L, Sui D, Hu H, et al. HealthFlow: automating electronic health record analysis via a strategically self-evolving multi-agent framework. NPJ Digit Med. 2026;9:660. doi:10.1038/s41746-026-03097-0.

10. Agentomics: an agentic system that autonomously develops novel state-of-the-art solutions for biomedical machine learning tasks. Bioinformatics. 2026;42(Suppl 1):btag250. doi:10.1093/bioinformatics/btag250.

11. Ma Z, Huang H, Zou S, Wang Y, Yang S, Hu Y, et al. LongHorizon-Harness: advancing long-horizon agents for real-world tasks. arXiv [Preprint]. 2026. doi:10.48550/arXiv.2608.01964.

12. Dehkalani ED, Shankaran S, Laptook AR, Cotten CM, Grant PE, Ou Y. Large language models for structured clinical data analysis: dual-agent grounding and validation. arXiv [Preprint]. 2026. doi:10.48550/arXiv.2609.34039.

13. Kurjan A, Cribbs AP. FlowBench: separating planning, fault recovery and interpretation in agentic bioinformatics. bioRxiv [Preprint]. 2026. doi:10.64898/2026.06.12.731844.

14. Dinç O, Akay E, Ates B. Freely accessible large language models for parent education in pediatric immune thrombocytopenia: an expert-rated cross-sectional study of safety, readability, and guideline concordance. Front Pediatr. 2026;14:1889520. doi:10.3389/fped.2026.1889520.

15. OpenAI. ChatGPT Free Tier FAQ [Internet]. San Francisco: OpenAI; 2026 [cited 2026 Sep 30]. Available from: https://help.openai.com/en/articles/9275245-chatgpt-free-tier-faq

16. Google. Upload and analyse files in Gemini Apps [Internet]. Mountain View: Google; 2026 [cited 2026 Sep 30]. Available from: https://support.google.com/gemini/answer/14903178

17. Anthropic. Plans and pricing [Internet]. San Francisco: Anthropic; 2026 [cited 2026 Sep 30]. Available from: https://claude.com/pricing

18. Mistral AI. Pricing [Internet]. Paris: Mistral AI; 2026 [cited 2026 Sep 30]. Available from: https://mistral.ai/pricing/

19. Wagner P, Strodthoff N, Bousseljot RD, Kreiseler D, Lunze FI, Samek W, et al. PTB-XL, a large publicly available electrocardiography dataset. Sci Data. 2020;7:154. doi:10.1038/s41597-020-0495-6.

## Evidence status

References 1 through 14 and 19 were checked against conference proceedings, journal pages, PubMed, or official publisher pages during the present review. References 15 through 18 are official provider sources and are used only for current access and capability claims.

The final novelty conclusion remains open until the dedicated search methods record is completed and the remaining literature axes are screened against the exact experimental design.
