# Research log

I am using this file to keep the project history visible across research phases. The important record here is why the scientific object changed.

## Phase 1. The ECG question

I began with a focused question about amplitude normalization in ECG machine learning.

The original study used PTB-XL version 1.0.3 and compared the native 100 Hz, 12-lead waveform with a global record-wise z-score representation. I chose HYP versus NORM and MI versus NORM as two prespecified phenotype tasks and fixed the model and evaluation procedure so that the representation change was the intended difference.

I spent substantial time on the data and methods before any primary model result was generated. The PTB-XL metadata were audited, the label rules were made explicit, representative waveform files were checked, the model input and architecture were fixed, and the uncertainty analysis was specified at the patient level because patients can contribute more than one ECG record.

The implementation was also tested. A real issue was found in the unthresholded label sensitivity and corrected before any primary test result was interpreted.

At that stage I was still treating the study as a live ECG research question.

## Phase 2. A deeper literature review changed the question

I then went back to the literature more deeply to check whether the central contrast was actually open.

That review found recent work that was much closer to my question than the earlier literature pass had suggested. XAND-ECG reports PTB-XL experiments using HYP and MI, a global z-score across all leads and time points within each ECG, and direct comparisons of normalization choices. Its findings also report different normalization behaviour across disease families. The project documents use PTB-XL version 1.0.3 and a 100 Hz, 12-lead representation.

A separate 2026 study by Bickmann et al. examined 24 preprocessing combinations across six ECG architectures on PTB-XL and found architecture-dependent effects of preprocessing. That made it difficult to defend a broad representation question as new.

ACL-ECG also uses a global normalization calculated across all leads and time points and explicitly contrasts that with per-lead normalization in a PTB-XL setting.

The result of this review was not a new analysis. It was a change in my understanding of the gap. The question I had frozen was no longer cleanly distinct from work that already existed.

## Phase 3. I tested whether the question could be made more specific

I did not want to abandon the project after finding overlap, so I tested whether the scientific question could be narrowed without simply adding more arbitrary ablations.

I examined several possibilities, including separating centering from scaling, comparing input normalization with internal normalization, using external validation, reinjecting normalization statistics, and asking a broader question about which signal invariances a biomedical representation should preserve.

I then checked those ideas against the literature.

That second pass also showed substantial precedent. Work on normalization and representation learning already covers normalization decomposition, internal and reversible normalization, restoration or reinjection of normalization statistics, and related representation-invariance questions.

I therefore did not turn any of those ideas into a standalone novelty claim.

## Phase 4. I went back to the earlier projects

At that point I returned to PHLOME and Asclepius, not to reuse them as finished methods but to understand which research problems had actually changed how those systems were built.

The recurring ideas were explicit state and context, provenance, uncertainty, validation before handoff, controlled model context, deterministic checks, reconciliation, explicit unresolved states and separate evidence for completion.

I treated these as candidate research questions rather than assuming that a design principle was automatically a scientific contribution.

## Phase 5. I checked those ideas against current ECG research

The same literature test was then applied to the ideas coming from PHLOME and Asclepius.

I considered combinations such as signal quality with model uncertainty, label provenance with model behaviour, clinically grounded metamorphic tests, deterministic ECG validators, evidence-grounded failure analysis, and the interaction between preprocessing and label quality.

Again, the deeper literature showed that most of these areas already had substantial precedent. Recent ECG work addresses label certainty, signal quality, preprocessing effects, and validation or perturbation-based analysis. Broader machine-learning literature also covers several of the proposed methodological patterns.

The useful outcome was not to force a paper out of a weakly differentiated idea. The outcome was a clearer boundary around what I could no longer claim as a new scientific object.

## Phase 6. The research object itself needed to change

After the second round of literature checking, I stopped trying to rescue the original ECG question by adding another comparison.

The important change was conceptual. I was no longer asking how one ECG preprocessing operation behaves. I was asking a different kind of question about how a scientific analysis can be carried out under constrained resources and how the reliability of that workflow can be evaluated.

That meant the unit of research would need to move from an ECG preprocessing intervention to the analysis workflow itself.

## Phase 7. The new direction

The direction that emerged is a controlled study of whether a general-purpose online LLM can reproduce a conventional biomedical machine-learning analysis under constrained, explicitly specified workflow conditions.

The idea is not to ask the broad question of whether an LLM can do data science. That literature is already crowded.

The more specific question is whether workflow constraints such as staged data access, smaller data chunks, fresh context, multi-gate checking and independent audit change the scientific fidelity of an LLM-assisted analysis relative to a conventional reference analysis.

The intended comparison is also important. The LLM is not being treated as a replacement for the ECG classifier. It would be compared with the analyst or workflow that assembles and executes the analysis, while the raw data, frozen protocol and evaluation target are held constant.

For the first implementation, the candidate models must be general-purpose models that an ordinary user can access directly online for free. Local models and small language models are outside the scope of this study.

This is still a research direction, not a frozen protocol. The next step is another literature and benchmark review to identify exactly what has already been tested, then define the experimental object, comparison conditions, fidelity measures, cost measures and failure criteria.


## Phase 8. I checked the new direction against the literature

I started the next literature pass by checking the proposed LLM study against work on data-science agents, scientific reproduction, biomedical research agents, and clinical data analysis.

The first result is that the broad question is already occupied.

DataSciBench and DSBench evaluate LLMs or agents on realistic data-science tasks, including data analysis and end-to-end data modelling. ScienceAgentBench evaluates language agents on data-driven scientific tasks using executable programs and explicit scientific-task validation. PaperBench and the newer RECLAIM benchmark evaluate whether agents can reproduce published machine-learning research. These studies make a simple question about whether an LLM can perform data science or reproduce an analysis too broad to stand alone. [DataSciBench](https://aclanthology.org/2026.findings-acl.181/) [DSBench](https://proceedings.iclr.cc/paper_files/paper/2025/hash/50e9ad960ae78b741a6b4fea533f2eaf-Abstract-Conference.html) [ScienceAgentBench](https://github.com/OSU-NLP-Group/ScienceAgentBench) [PaperBench](https://proceedings.mlr.press/v267/starace25a.html) [RECLAIM](https://arxiv.org/abs/2609.28850)

Biomedical research is also no longer an open category. Biomni and BioMedAgent demonstrate general or multi-agent systems that carry out biomedical analysis workflows. BiomniBench evaluates biomedical agents at the process level rather than scoring only final answers. Open-Rosalind, R-LAM and related work study constrained, auditable or reproducibility-oriented scientific workflows. These papers mean that a claim such as "workflow constraints make biomedical LLM analysis more reliable" is also too broad. [Biomni](https://pubmed.ncbi.nlm.nih.gov/42424436/) [BioMedAgent](https://www.nature.com/articles/s41551-026-01634-6) [BiomniBench](https://www.biorxiv.org/content/10.64898/2026.05.12.724604v2) [Open-Rosalind](https://www.biorxiv.org/content/10.64898/2026.05.06.722404v1)

The closest study I have found so far is a September 2026 JMIR evaluation of an LLM agent for clinical data analysis. It used a public clinical dataset and reference code, tested five stages of the analysis workflow, compared Chat, Code and Cowork interaction modes, repeated conditions independently, and evaluated research questions, statistical analysis plans, execution against reference values, result-to-log fidelity and reporting errors. The Chat condition was run on a free tier. This directly overlaps with the parts of my proposed design that involve a fixed clinical analysis, ordinary LLM interaction, repeated runs and scientific fidelity. [Wu et al., 2026](https://pmc.ncbi.nlm.nih.gov/articles/PMC13552643/)

That paper changes what I think the useful gap might be.

I do not think the study should be framed as another benchmark of general LLM data-analysis ability. I also do not think it should be framed as another comparison of autonomous agent architectures.

The potentially useful question is narrower. I am interested in whether the way information and analytical responsibility are exposed to an ordinary online general-purpose LLM changes the fidelity of a fixed biomedical machine-learning analysis.

The experimental factor would therefore be the workflow, not merely the model. A single frozen biomedical analysis would be supplied under controlled conditions such as unrestricted dataset access, staged data exposure, fresh-context execution, explicit verification gates, and independent audit. The same target analysis and evaluation criteria would be used across conditions.

This distinction matters because several existing papers study stronger agent scaffolding, tool libraries, or domain-specific agent systems. My proposed setting is deliberately less engineered. The unit being evaluated would be a browser-accessible general-purpose LLM used as an analyst, not a bespoke autonomous research agent.

Even this narrower question is not yet established as novel. Multi-turn medical benchmarks already show that changing when evidence is released can alter model behaviour, and recent scientific-agent work shows that constrained execution and intermediate verification can affect reliability. Those studies are not the same task, but they close off the easy claim that staged context or gating is itself a new idea. [MINT](https://arxiv.org/abs/2604.04325) [ESFlow](https://egusphere.copernicus.org/preprints/2026/egusphere-2026-2237/) [R-LAM](https://arxiv.org/abs/2601.09749)

I therefore regard the new direction as promising enough to investigate further but not yet sufficiently differentiated to freeze as a research question.

The next literature pass needs to answer a more specific question.

Has anyone already performed a controlled within-task experiment in which the same biomedical machine-learning protocol and data are given to ordinary online general-purpose LLMs under different information-access and verification regimes, with scientific fidelity measured against a deterministic reference analysis?

Until that question is answered cleanly, I will not write the final protocol or treat the workflow-factor idea as a novelty claim.


## Phase 9. A second search found closer precedents

I then searched more narrowly for studies in which an LLM was asked to carry out a fixed or partially fixed analysis rather than simply answer a data-science benchmark.

A 2024 Nature Communications study had already used ChatGPT Advanced Data Analysis on real clinical datasets from published studies. ChatGPT was given the study information and data and was allowed to develop machine-learning models; the resulting models were compared with manually developed models. The authors also repeated the analyses in separate chat sessions to assess consistency. That closes off a simple comparison of an LLM-built biomedical ML pipeline against a conventional model as a research gap. [Nature Communications, 2024](https://www.nature.com/articles/s41467-024-45879-8)

A 2026 Nature Communications study on cell-free RNA diagnostic biomarker discovery goes even closer to the intended setting. The LLM constructed binary classifiers, requested held-out test data only after model construction, produced CSV predictions and feature rankings, and the protocol was repeated 50 times per clinical cohort under two prompt conditions. Fresh sessions were used to avoid cross-conversation memory, with identical random seeds maintained across comparative analyses. [Nature Communications, 2026](https://www.nature.com/articles/s41467-026-74077-x)

A separate 2026 study compared a predefined statistical workflow executed in SPSS with ChatGPT's Data Analyst environment using the same clinical dataset. The investigators refined the natural-language specification, locked the prompt, repeated it across independent sessions and measured numerical concordance and execution time. That means reproducibility of a predefined natural-language analysis is already being studied directly, although the task was diagnostic statistics rather than a full biomedical machine-learning pipeline. [Investigative and Clinical Urology, 2026](https://doi.org/10.4111/icu.20250642)

These papers change the boundary again. The new study cannot claim that it is the first to compare an LLM with conventional biomedical analysis, the first to reproduce a predefined analysis, or the first to use repeated fresh sessions or held-out data.

The remaining question I am interested in is more specific.

I want to test whether controlled information-access and verification regimes change the scientific fidelity of a fixed biomedical machine-learning workflow when the same general-purpose online LLM is used as the analyst. The reference analysis would be deterministic and frozen. The scientific task, data, target outputs and scoring rules would remain fixed while the analyst-facing workflow changes.

The key comparison is therefore not simply LLM versus conventional software. It is the effect of the workflow regime on the fidelity of the LLM-led analysis.

I have not found an exact study in this targeted search that uses the same biomedical ML task and directly randomizes or ablates information-access and verification regimes while holding the underlying analysis target fixed. That is not enough to call the question novel yet. The search is targeted rather than systematic, and nearby work on multi-turn medical reasoning, constrained scientific agents and workflow verification means the remaining gap needs to be defined very carefully.

For now, I am keeping the direction open and will not freeze the protocol until the workflow factor can be specified as an actual experimental variable rather than a collection of convenient prompt tricks.


## Archival maintenance

While checking the archived code after the repository move, I found that one unit test for the unthresholded label sensitivity did not match the implemented rule. The code treats any mapped diagnostic-superclass statement as present when the threshold is set to None, but the test used a zero-likelihood HYP statement and expected it to be absent.

I changed that test fixture to use an unrelated diagnostic statement that is actually absent from the HYP and NORM classes. I also added a small pytest configuration so the preserved tests can run directly from the archive directory.

I reran the archived unit tests after the correction. All six tests passed. This maintenance change does not alter the study protocol, model architecture, analysis plan or any result because the primary analysis was never run.


## Phase 10. The first formal workspace for the new study

After the final integrated prior art and methods audit, I opened a separate current study workspace rather than adding provisional study documents to the archived ECG folder.

The working design now separates the fixed biomedical machine learning reference task from the LLM workflow being evaluated. The primary comparison is currently defined as a fully specified monolithic workflow versus a structured fresh context workflow. Minimal instruction, self audit, deterministic validation, and independent audit remain secondary conditions.

The zero cost consumer access criterion is part of the study population rather than a casual implementation detail. A configuration must be available to an ordinary user through a public consumer interface at no monetary cost, without an API, subscription, institutional or researcher entitlement, paid agent product, promotional credit, local deployment, or specialized small language model. The required capabilities must also be available within that zero cost route.

The reference analysis has not yet been executed. Numerical agreement criteria and the primary run count therefore remain open.

The current study documents are being built from the evidence and decision record accumulated during the earlier literature passes. The literature record will retain sources that support the design as well as sources that closed earlier candidate questions.
