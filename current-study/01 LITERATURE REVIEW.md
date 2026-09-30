# Literature Review

**Status:** Working review  
**Version:** 0.1  
**Month:** September 2026

## Scope

This review defines the scientific background and prior art for the active study. It covers the biomedical machine learning testbed, LLM based scientific analysis, biomedical research agents, workflow architecture, reproducibility, accessibility, and reporting standards.

The review is intentionally broader than the final research question. Sources are retained when they establish a scientific fact, close a candidate question, motivate a methodological control, or define a reporting or access requirement. Studies that weaken a proposed novelty claim are retained alongside studies that support the eventual design.

The literature search to date is targeted and iterative rather than a completed systematic review. The search record will be documented separately. The present review therefore distinguishes an observed evidence boundary from a formal claim that no further study exists.

## 1. Biomedical machine learning as the scientific testbed

The active study uses the PTB XL electrocardiography dataset as the candidate biomedical machine learning testbed. PTB XL is a large publicly available collection of 12 lead clinical ECG recordings with diagnostic annotations and patient identifiers that support patient aware evaluation. The original data descriptor established the dataset as a resource for machine learning research and described its structure, metadata, and recommended use. [1]

The proposed study does not treat the ECG task as a new clinical discovery problem. The ECG analysis is a locked computational task that allows the study to examine whether different LLM workflow structures can execute the same biomedical experiment faithfully.

This distinction is important because the scientific target has two components. The first is the biomedical prediction analysis itself. The second is the workflow through which an LLM is asked to reconstruct and execute that analysis. The first must remain fixed if the second is to be interpreted causally.

The candidate reference analysis retains the technical features already established in the archived ECG study. These include HYP versus NORM and MI versus NORM tasks, direct 12 lead waveform input at 100 Hz, patient aware folds, a fixed one dimensional convolutional network, a specified training procedure, AUROC, average precision, Brier score, calibration assessment, the prespecified contrast between phenotype specific normalization effects, and patient level bootstrap uncertainty. These components provide the biomedical ML depth of the experiment. They are not being introduced as new algorithms.

The evaluation literature in clinical machine learning also supports reporting more than a single discrimination statistic. TRIPOD plus AI provides updated reporting guidance for prediction models developed using regression or machine learning methods, including reporting of data, model development, evaluation, performance, and validation. [2] PROBAST plus AI provides a complementary assessment of quality, risk of bias, and applicability for prediction models using regression or artificial intelligence methods. [3] MINIMAR similarly emphasizes adequate reporting of the target population, model architecture, evaluation, and validation so that a medical AI system can be understood and assessed. [4]

For this reason, AUROC will remain a core result but will not be treated as a sufficient indicator that an LLM reproduced the scientific analysis. A workflow could obtain a plausible AUROC while using the wrong cohort, a wrong label definition, an incorrect patient split, a changed preprocessing operation, or an altered statistical estimand. The active study therefore requires numerical outputs to be evaluated together with protocol and implementation fidelity.

## 2. LLMs performing biomedical machine learning

Work preceding the present study already demonstrates that general purpose LLM interfaces can construct machine learning analyses from clinical data. Tayebi Arasteh and colleagues used ChatGPT Advanced Data Analysis with real clinical datasets and study information from published investigations, allowing the system to develop machine learning models without detailed methodological guidance. The resulting models were compared with manually developed models after reimplementation and optimization. [5]

This study closes several possible formulations of the current research question. It is no longer defensible to ask whether an LLM can perform biomedical machine learning at all, whether an LLM can build a clinical prediction model, or whether LLM generated models can reach conventional predictive performance in some clinical datasets.

More recent work has extended this area into biomedical biomarker discovery. Gaudio and colleagues evaluated six LLMs from OpenAI, Anthropic, and Google across three clinical cell free RNA cohorts. The study examined both literature guided feature nomination and end to end construction of classifiers from raw count matrices. For the end to end experiments, the models constructed classifiers from training data and were subsequently given held out test data. The protocol was repeated 50 times under disease naive and disease informed prompts, using fresh sessions and matched conventional machine learning analyses. [6]

The study is especially relevant because it shows that repeated fresh sessions, held out evaluation, conventional comparators, and repeated LLM constructed machine learning pipelines are already established experimental practices. Those features cannot be presented as unique contributions of the current project.

The same study also illustrates why task difficulty and model capability should not be reduced to a single model ranking. End to end completion depended on both the model and the biological task, and only some of the evaluated models consistently completed the full pipeline in the reported setting. [6]

The September 2026 clinical data analysis evaluation by Wu and colleagues moves even closer to the planned study structure. It evaluated Claude across five stages of a clinical data analysis workflow, including question generation, statistical analysis planning, preprocessing and cohort logic, statistical execution, and reporting. Chat, Code, and Cowork interaction modes were tested, with 27 total runs. Execution outputs were compared against validated reference values, and narrative results were checked against execution logs. The study found that correct statistical planning did not guarantee correct implementation, and clinically meaningful execution and reporting errors could remain even when numerical outputs appeared plausible. [7]

These findings are directly relevant to the decision to separate scientific fidelity from numerical fidelity. A successful run cannot be defined only by whether the final numbers resemble a reference. The path to the numbers and the interpretation of those numbers must also be checked.

## 3. Scientific data analysis and research reproduction

The wider scientific agent literature has already moved beyond simple question answering.

ScienceAgentBench evaluated 102 scientific data analysis tasks derived from peer reviewed publications across four disciplines. Each task was converted into a self contained Python program target, and the benchmark evaluated generated programs, execution results, and costs. The authors explicitly argued that reliable end to end scientific automation requires rigorous assessment of individual workflow tasks before broader claims are made. [8]

DataSciBench extends this direction to realistic data science tasks. It uses complex natural language tasks with execution based assessment and programmatic evaluation rules, and evaluates a broad set of contemporary models. [9] These benchmarks establish process and execution as legitimate scientific evaluation targets rather than treating final narrative answers as sufficient.

PaperBench addresses a related problem from another direction. It evaluates AI agents attempting to reproduce published machine learning research, using hierarchical task rubrics that decompose replication into individually gradable subtasks. Its benchmark contains 20 ICML 2024 papers and 8316 gradable tasks. [10]

RECLAIM, released in September 2026, provides an even closer recent precedent for reference based research reproduction. It evaluates reproduction of claims from 100 NeurIPS 2025 papers, fixes in advance the result to reproduce and the success criteria, and imposes a GPU hour budget. A separate language model grades runs from logs and outputs rather than relying on an agent generated report. The reported reproduction rates were low and decreased as more of the original implementation had to be rebuilt. [11]

These studies close another set of broad novelty claims. Reference based reproduction is not new. Resource bounded reproduction is not new. Executable research evaluation is not new. Structured grading of research tasks is not new.

Their relevance to the active study is methodological. They support the use of explicit reference objects, executable evidence, machine readable outputs, prespecified success rules, and retained interaction or execution logs.

The present study differs in its intended causal structure. Rather than asking whether an agent can reproduce many different published papers, it proposes to hold one biomedical ML task constant and manipulate the workflow through which an LLM approaches that task. The validity of this distinction depends on maintaining identical scientific inputs and evaluation targets across workflow conditions.

## 4. Biomedical research agents and workflow architecture

Biomedical agent systems have developed rapidly. Biomni was introduced as a general purpose biomedical AI agent designed to execute research tasks across diverse biomedical domains and to use a broad collection of tools and databases. The work highlights the potential of automated biomedical workflows but uses a specialized agent environment rather than a plain consumer LLM interface. [12]

BioMedAgent provides a recent peer reviewed example. Bu and colleagues developed a multi agent framework that learns to use diverse bioinformatics tools and construct executable workflows. Its BioMed AQA benchmark contains 327 biomedical data tasks, and the reported system performs cross omics analysis, machine learning modelling, and other multistep biomedical tasks. [13]

Recent review literature shows how broad this design space has become. Reviews published in 2026 describe planning, tool invocation, reflection, memory, and iterative refinement as recurring components of biological and biomedical LLM agents. [14,15]

This literature is useful for the active study but also defines an important boundary. The study should not claim that staging, planning, self reflection, memory, validation, or tool orchestration are novel mechanisms. Those concepts are established features of current agent architectures.

Instead, the scientific use of those mechanisms is experimental. The project asks whether selected controls change fidelity when the biomedical task is locked and the consumer LLM is otherwise constrained to the same access environment.

FlowBench is particularly relevant because it separates several aspects of agent behaviour rather than treating all forms of reflection or orchestration as beneficial. The benchmark decomposes performance into planning, fault recovery, biological interpretation, and end to end output fidelity. [16] Its design supports a cautious experimental approach in which added control mechanisms are tested rather than assumed to improve reliability.

That principle is carried into the active experiment. Self audit, deterministic validation, and independent auditing are candidate experimental conditions. They are not assumed to improve performance before the data are collected.

## 5. Workflow structure, fresh context, and verification

The active workflow conditions were derived partly from recurring control structures encountered during the development of PHLOME and Asclepius. Those systems separated state, provenance, validation, unresolved cases, controlled transitions, and reconciliation. The active study does not present those engineering patterns as scientific novelty. They provide a reason to formulate controlled workflow interventions that can be tested against a fixed biomedical task.

The current candidate conditions are W0 through W5.

W0 is a minimal monolithic condition using a concise instruction while keeping the complete scientific specification in a standard study package. Its purpose is to estimate what the system can do without elaborate interaction scaffolding.

W1 makes the workflow specification explicit while keeping execution inside one continuous context. This separates instruction specificity from context architecture.

W2 divides the analysis into predefined stages and uses fresh contexts with structured handoff artifacts. The current stages are data and provenance audit, cohort and label construction, analysis implementation, execution and evaluation, and interpretation and reporting.

W3 adds an explicit adversarial self audit after W2. The audit is bounded to one audit cycle and one repair cycle.

W4 adds deterministic read only validation. The validator examines properties that can be checked mechanically, such as cohort counts, patient overlap, representation, model architecture, training configuration, metric definitions, and bootstrap settings. The validator does not decide what a scientifically appropriate analysis should be, and it does not repair the analysis directly.

W5 adds an independently initiated LLM audit. The auditor receives the locked protocol and the completed analysis evidence but does not inherit the executor's conversational history or self assessment.

The primary comparison is W1 versus W2 because this contrasts explicit monolithic execution with a structured fresh context architecture without simultaneously changing instruction specificity. W0 is retained as a secondary baseline. W3, W4, and W5 are secondary mechanistic conditions.

The design therefore treats workflow architecture as an experimental factor while keeping the underlying scientific task constant. The interpretation of any difference requires the access environment, external execution substrate, study package, and evaluation procedure to remain fixed.

## 6. Scientific fidelity and reproducibility

A recurring issue in the current literature is the difference between a plausible result and a reproducible analytical process.

The Wu et al. study provides a direct example. Some analysis stages produced numerically close results while important execution errors persisted. [7] RECLAIM likewise reports that a common failure mode was writing an implementation without checking it against the numerical information in the source paper. [11]

These results motivate several requirements in the active study.

The reference object must be executable. A protocol alone is insufficient because the protocol can contain ambiguities that only become visible during implementation.

The reference implementation must be independently reproduced before it becomes the numerical reference. This allows the empirical variability between reasonable equivalent implementations to be observed before agreement thresholds are chosen.

The LLM run must preserve the entire chain from study package to code, execution, metrics, and interpretation.

Protocol fidelity and numerical fidelity must be scored separately. A run that obtains an acceptable AUROC using an incorrect cohort should not count as a successful scientific reproduction.

The experimental design must distinguish repeatability from reproducibility. Repeated fresh runs under the same configuration address repeatability. Repetition under prespecified changes in workflow or eligible LLM configuration addresses reproducibility across those conditions.

Reproducibility guidance for computational biology also emphasizes preserving the computational environment, dependencies, workflow, and executable materials. [17] FAIR principles provide a broader framework for making research data findable, accessible, interoperable, and reusable. [18] FAIR4RS extends the same principles to research software and explicitly includes versioning and provenance. [19]

These principles support preserving prompts, interaction records, generated code, execution logs, environment specifications, validator outputs, audit records, and deviations as research artifacts rather than treating them as disposable chat history.

## 7. Accessibility and the zero cost consumer population

The accessibility criterion is a central boundary of the active study.

The eligible population is not all LLMs, all open source models, all models with a free API tier, or all systems that can be accessed through a university or researcher program. It is limited to general purpose LLM systems available through a public consumer facing interface at zero monetary cost to an ordinary user, with every capability required by the experiment available within that same zero cost route.

The distinction is necessary because a model can have a free consumer interface while an important analytical capability is available only through a paid agent product, API, or special research program.

Current provider documentation demonstrates that free consumer access exists but is bounded. OpenAI documents a Free plan with separate limits for tools such as data analysis and file uploads. [20] Google documents file upload and analysis through Gemini without an AI plan, with lower context and usage limits than paid plans. [21] Anthropic documents code execution and file creation for Free users while separately offering higher capacity paid products. [22] Mistral lists a Free consumer plan with limited messages and coding access while distinguishing paid plans and API services. [23]

These sources support the existence and operational characteristics of candidate access routes. They do not establish the scientific novelty of the active study.

The zero cost criterion is therefore best treated as a prespecified population boundary and resource envelope. The research question concerns what an ordinary user can obtain without entering a paid or privileged access pathway. The study does not imply that free consumer systems are intrinsically superior to paid systems, and it does not generalize its findings to models that fall outside the eligibility criteria.

The access boundary also introduces an important reproducibility problem. Free consumer services can change their models, context limits, tools, quotas, and interface behaviour over time. The study therefore requires an access registry containing the provider, product, displayed model, plan, date, region, relevant tool capabilities, context and file limits, memory state, web access state, and any other capability that could alter the experiment.

## 8. Reporting and research governance standards

The active project uses several reporting frameworks for different parts of the study rather than claiming compliance with every available guideline.

TRIPOD plus AI is the principal reporting framework for the biomedical prediction model component. The 2024 update supersedes the original TRIPOD checklist and provides 27 items for prediction model studies using regression or machine learning. [2]

TRIPOD LLM is the principal reporting framework for the LLM component. It contains 19 main items and 50 subitems and explicitly addresses the need to describe LLM configuration, interaction, human oversight, task specific performance, and reproducibility. [24]

PROBAST plus AI is used as a supporting risk of bias and applicability framework for the prediction model component. [3]

MINIMAR is used as a supporting reporting completeness framework, especially for population, model specification, evaluation, and validation. [4]

PRISMA S is applied to the literature search record rather than to the biomedical experiment. It provides 16 items for transparent reporting of literature search methods and was developed to improve reproducibility of information retrieval. [25]

FAIR and FAIR4RS guide research object and software stewardship. [18,19]

STROBE and RECORD are treated as transferable principles where relevant to secondary clinical data description rather than as the governing reporting standards for the computational experiment. Clinical trial frameworks such as CONSORT AI and SPIRIT AI are not used as governing standards because the active study is an in silico workflow experiment rather than a clinical trial.

## 9. Prior art that closes earlier candidate questions

The literature review has already closed several possible research questions.

It is not a new question whether LLMs can perform biomedical machine learning. [5,6]

It is not a new question whether agents can execute scientific data analysis tasks. [8,9]

It is not a new question whether AI agents can reproduce published machine learning research. [10,11]

It is not a new question whether biomedical research agents can execute multistep data analysis. [12,13]

It is not a new question whether repeated independent LLM sessions can be used to measure consistency. [6,7]

It is not a new question whether workflow components such as planning, reflection, validation, or fault recovery can affect agent performance. [13,16]

It is not a new question whether free consumer LLM interfaces can be used for clinical or biomedical analysis. The current literature contains studies conducted through consumer interfaces, including free tier configurations, although access conditions and scientific tasks differ. [7,20-23]

These findings are retained because they define the scientific boundary rather than because they are convenient background references.

## 10. Current evidence boundary

The targeted searches completed so far have not identified an exact published study matching every element of the proposed design simultaneously.

The candidate remaining combination is narrower than the surrounding benchmark literature. The same locked biomedical ML task would be executed under predefined workflow architectures, the primary comparison would isolate monolithic versus structured fresh context execution, access would be limited to genuine zero cost ordinary consumer LLM configurations, and success would require both reference faithful scientific execution and acceptable numerical agreement with an independently established reference.

This combination should remain a candidate contribution rather than a novelty claim until the complete prior art search and final experimental audit are complete.

The most important implication from the literature is that the study should not ask whether additional scaffolding is generally good. Existing evidence is already sufficient to show that planning, reflection, context management, validation, and recovery can influence workflow outcomes in some settings. [13,16] The scientific question is instead whether a particular workflow intervention changes the reliability of a fixed biomedical ML analysis under a precisely defined access envelope.

The reference analysis must therefore be established before the workflow experiment. The empirical reference-agreement envelope must be derived before primary LLM results are available. The primary workflow comparison must be specified before model selection is influenced by performance. Free access eligibility must be decided independently of model performance.

## 11. Design implications from the literature

The literature reviewed to date leads to the following design requirements.

First, the biomedical task must remain technically substantive. AUROC, average precision, Brier score, calibration, the primary cross task estimand, and patient level uncertainty remain part of the core evaluation.

Second, the study must evaluate executable scientific fidelity rather than narrative plausibility.

Third, the reference pipeline must be independently checked before it is treated as a numerical standard.

Fourth, repeated independent runs are necessary because correctness in one run does not establish repeatability.

Fifth, workflow interventions should be tested individually or in a controlled hierarchy rather than introduced as an undifferentiated bundle.

Sixth, audit and repair must be bounded so that a workflow cannot continue until a favorable result happens to appear.

Seventh, the access population must be defined before primary runs, and model or provider selection must not depend on observed performance.

Eighth, current provider capabilities must be recorded through official documentation because the consumer products are dynamic.

Ninth, the final research record must preserve the complete provenance of prompts, model configurations, generated code, execution outputs, validation, auditing, and deviations.

Tenth, rejected candidate questions and the literature that closed them remain part of the evidence base. The final paper may cite only the most relevant subset, but the research archive should preserve the larger evidentiary trail.

## References

1. Wagner P, Strodthoff N, Bousseljot RD, Kreiseler D, Lunze FI, Samek W, et al. PTB XL, a large publicly available electrocardiography dataset. Sci Data. 2020;7:154. doi:10.1038/s41597-020-0495-6.

2. Collins GS, Moons KGM, Dhiman P, Riley RD, Beam AL, Van Calster B, et al. TRIPOD plus AI statement: updated guidance for reporting clinical prediction models that use regression or machine learning methods. BMJ. 2024;385:e078378. doi:10.1136/bmj-2023-078378.

3. Moons KGM, Damen JAA, Kaul T, Hooft L, Andaur Navarro C, Dhiman P, et al. PROBAST plus AI: an updated quality, risk of bias, and applicability assessment tool for prediction models using regression or artificial intelligence methods. BMJ. 2025;388:e082505. doi:10.1136/bmj-2024-082505.

4. Hernandez-Boussard T, Bozkurt S, Ioannidis JPA, Shah NH. MINIMAR (MINimum Information for Medical AI Reporting): developing reporting standards for artificial intelligence in health care. J Am Med Inform Assoc. 2020;27(12):2011-2015. doi:10.1093/jamia/ocaa088.

5. Tayebi Arasteh S, Han T, Lotfinia M, Kuhl C, Kather JN, Truhn D, et al. Large language models streamline automated machine learning for clinical studies. Nat Commun. 2024;15:1603. doi:10.1038/s41467-024-45879-8.

6. Gaudio HA, Bliss A, Loy CJ, Eweis-LaBolle D, Gardella AE, et al. Benchmarking large language models for cell-free RNA diagnostic biomarker discovery. Nat Commun. 2026;17:7429. doi:10.1038/s41467-026-74077-x.

7. Wu Y, Fu DJ, Zhou Y, Wagner SK, Keane PA. Performance, failures, and oversight of a large language model agent for clinical data analysis: evaluation study. J Med Internet Res. 2026;28:e99597. doi:10.2196/99597.

8. Chen Z, Chen S, Ning Y, Zhang Q, Wang B, Yu B, et al. ScienceAgentBench: toward rigorous assessment of language agents for data-driven scientific discovery. International Conference on Learning Representations; 2025.

9. Zhang D, Zhoubian S, Cai M, Li F, Yang L, Wang W, et al. DataSciBench: an LLM agent benchmark for data science. Findings of the Association for Computational Linguistics: ACL 2026. 2026:3685-3728. doi:10.18653/v1/2026.findings-acl.181.

10. Starace G, Jaffe O, Sherburn D, Aung J, Chan JS, Maksin L, et al. PaperBench: evaluating AI's ability to replicate AI research. Proc Mach Learn Res. 2025;267:56843-56873.

11. Salunkhe M, Ding H, Verma S, Kindratenko V. RECLAIM: can agents reproduce the claims of machine learning papers? arXiv [Preprint]. 2026. doi:10.48550/arXiv.2609.28850.

12. Huang K, Zhang S, Wang H, Qu Y, Lu Y, Roohani Y, et al. Biomni: a general-purpose biomedical AI agent. bioRxiv [Preprint]. 2025. doi:10.1101/2025.05.30.656746.

13. Bu D, Sun J, Li K, et al. Empowering AI data scientists using a multi-agent LLM framework with self-evolving capabilities for autonomous, tool-aware biomedical data analyses. Nat Biomed Eng. 2026. doi:10.1038/s41551-026-01634-6.

14. Wei Z, Qi C, Wang W, et al. Artificial intelligence agents for biological research: a survey. Brief Bioinform. 2026;27(1):bbag075. doi:10.1093/bib/bbag075.

15. Dip SA, Mallick D, Shuvo UA, Soumma SB, Rafsani F, Paul BK, et al. Large language model agents for biological intelligence across genomics, proteomics, spatial biology, and biomedicine. Brief Bioinform. 2026;27(2):bbag110. doi:10.1093/bib/bbag110.

16. Kurjan A, Cribbs AP. FlowBench: separating planning, fault recovery and interpretation in agentic bioinformatics. bioRxiv [Preprint]. 2026. doi:10.64898/2026.06.12.731844.

17. Papin JA, Mac Gabhann F, Sauro HM, Nickerson D, Rampadarath A. Improving reproducibility in computational biology research. PLoS Comput Biol. 2020;16(5):e1007881. doi:10.1371/journal.pcbi.1007881.

18. Wilkinson MD, Dumontier M, Aalbersberg IJ, Appleton G, Axton M, Baak A, et al. The FAIR guiding principles for scientific data management and stewardship. Sci Data. 2016;3:160018. doi:10.1038/sdata.2016.18.

19. Barker M, Chue Hong NP, Katz DS, Lamprecht AL, Martinez-Ortiz C, Psomopoulos F, et al. Introducing the FAIR principles for research software. Sci Data. 2022;9:622. doi:10.1038/s41597-022-01710-x.

20. OpenAI. ChatGPT Free Tier FAQ [Internet]. San Francisco: OpenAI; 2026 [cited 2026 Sep 30]. Available from: https://help.openai.com/en/articles/9275245-chatgpt-free-tier-faq

21. Google. Gemini Apps limits and upgrades for Google AI subscribers [Internet]. Mountain View: Google; 2026 [cited 2026 Sep 30]. Available from: https://support.google.com/gemini/answer/16275805

22. Anthropic. Create and edit files with Claude [Internet]. San Francisco: Anthropic; 2026 [cited 2026 Sep 30]. Available from: https://support.claude.com/en/articles/12111783-create-and-edit-files-with-claude

23. Mistral AI. Pricing [Internet]. Paris: Mistral AI; 2026 [cited 2026 Sep 30]. Available from: https://mistral.ai/pricing/

24. Gallifant J, Afshar M, Ameen S, et al. The TRIPOD LLM reporting guideline for studies using large language models. Nat Med. 2025;31:60-69. doi:10.1038/s41591-024-03425-5.

25. Rethlefsen ML, Kirtley S, Waffenschmidt S, Ayala AP, Moher D, Page MJ, Koffel JB; PRISMA-S Group. PRISMA-S: an extension to the PRISMA statement for reporting literature searches in systematic reviews. Syst Rev. 2021;10:39. doi:10.1186/s13643-020-01542-z.
