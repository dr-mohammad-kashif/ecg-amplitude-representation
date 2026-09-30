# Literature Search and Evidence Methods

Status: Working search record
Version: 0.1
Date: 30 September 2026
Study phase: Preprotocol
Review status: Targeted and iterative, not yet a completed systematic review

## 1. Aim and scope

This document records how literature and supporting evidence have been located, screened, verified, and retained for the active study.

The search has two purposes.

First, it establishes the scientific background and prior art for LLM based biomedical data analysis, scientific workflow execution, research reproduction, workflow verification, reproducibility, and resource accessibility.

Second, it is used to test the exact candidate contribution against close prior work before the experimental protocol is frozen.

The search is deliberately broader than the final research question. A source may be retained because it establishes an important capability, closes a candidate novelty claim, motivates a methodological control, defines a reporting requirement, or documents the current accessibility of a consumer LLM system.

This record is informed by PRISMA-S and PRISMA 2020 reporting principles for transparent search documentation. Those standards are being used as reporting guidance. The present work is not described as a completed systematic review because the search has been iterative, cross-disciplinary, and partly reconstructed from an earlier research record rather than prospectively registered and executed as a formal systematic review.[1,2]

## 2. Search design

The search is organized as a targeted evidence synthesis with successive prior-art attacks.

The central search question is not simply whether LLMs can analyse biomedical data. That question was closed early because prior work already demonstrates biomedical machine learning, scientific data analysis, research reproduction, and agentic biomedical workflows.

The search therefore concentrates on combinations of the following concepts.

1. General purpose LLMs performing scientific or biomedical data analysis
2. LLM and agent evaluation at the execution or process level
3. Reproduction and replication of published research
4. Workflow architecture, context management, staging, reflection, validation, and independent auditing
5. Biomedical machine learning agents and workflow systems
6. Clinical data analysis with executable or reference based evaluation
7. Free public consumer LLM access
8. Resource constrained or ordinary user access
9. Reproducibility and repeatability of LLM based computational work
10. Reporting standards relevant to LLM, biomedical ML, and computational research
11. Exact or near exact combinations of a fixed biomedical ML task, controlled workflow intervention, and consumer access boundary

The search strategy was deliberately adversarial. Candidate novelty claims were searched after each major narrowing step, including searches intended to find studies that would make the proposed design unnecessary or already established.

## 3. Evidence sources

### 3.1 Scholarly literature sources

The following source types have been used.

| Source type | Examples used | Main purpose |
|---|---|---|
| Biomedical indexing and publisher records | PubMed, Nature Portfolio, JMIR, Springer, PLOS | Bibliographic verification and biomedical methods |
| Computer science proceedings | ACL Anthology, Proceedings of Machine Learning Research, ICLR proceedings | Benchmarks, scientific agents, data science evaluation |
| Preprint servers | arXiv, bioRxiv, medRxiv | Recent work that may not yet have journal or conference publication |
| Search-engine discovery | Web search across scholarly and technical domains | Cross-disciplinary discovery and recent 2026 work |
| Project repositories | GitHub benchmark and research repositories | Benchmark implementation details and publicly documented task structures |
| Dataset and software sources | Official dataset and project documentation | Data provenance and implementation facts |
| Provider documentation | OpenAI, Google, Anthropic, Mistral | Current consumer access, capabilities, usage limits, and product configuration |

Provider documentation is used only for current product and access claims. It is not treated as peer reviewed scientific evidence.

### 3.2 Source hierarchy

Evidence is classified by its role rather than by assuming that every source has the same authority.

Tier 1 consists of peer reviewed scientific papers and published benchmark proceedings used for empirical or methodological claims.

Tier 2 consists of formal reporting and methodological standards.

Tier 3 consists of official dataset, repository, and provider documentation used for version, provenance, implementation, and current access facts.

Tier 4 consists of investigator defined design decisions. These are recorded explicitly and are not presented as conclusions prescribed by the literature.

## 4. Search periods and update policy

The present evidence base combines several stages.

The first stage was the exploratory search that surrounded the transition from the original ECG representation study to the LLM workflow study.

The second stage consisted of repeated targeted prior-art attacks as the research question narrowed. These searches included biomedical LLM analysis, scientific data analysis benchmarks, research reproduction, workflow verification, biomedical agents, consumer access, and workflow ablation.

The third stage is the formalization of the evidence record and source inventory.

The fourth stage is the current update performed on 30 September 2026, including targeted searches for methodological standards and recent work published or posted during September 2026.

The literature search remains open until the reference analysis, eligibility specification, workflow protocol, and statistical plan have been frozen. A final update will be performed immediately before protocol freeze.

Provider access is treated differently from scientific literature because the relevant information can change without a new publication. Current access claims therefore use an access epoch consisting of provider, interface, configuration, region, and access date.

## 5. Search axes

### Axis A. Biomedical machine learning

Searches cover PTB XL, ECG classification, patient level evaluation, biomedical prediction, AUROC, average precision, calibration, Brier score, preprocessing, normalization, and reproducibility.

The archived ECG study is used as a reference task, not as evidence that its original scientific question remains novel.

### Axis B. LLM scientific analysis

Searches cover LLM data science, scientific data analysis, executable code generation, clinical data analysis, machine learning pipeline construction, and repeated evaluation.

### Axis C. Research reproduction

Searches cover research reproduction, replication of machine learning papers, executable reproduction, claim reproduction, process traces, resource bounded replication, and reference based evaluation.

### Axis D. Workflow architecture

Searches cover staged workflows, fresh context execution, task decomposition, planner and executor architectures, reflection, self audit, deterministic validation, independent validation, bounded repair, context management, and workflow ablation.

### Axis E. Biomedical agents

Searches cover biomedical data-analysis agents, bioinformatics agents, biomedical machine learning agents, multi-agent scientific systems, clinical data-analysis agents, and process-level biomedical benchmarks.

### Axis F. Consumer accessibility

Searches cover free-tier LLM studies, public web interfaces, ordinary user access, zero-cost consumer interfaces, file analysis under free plans, and distinctions between consumer access and API or paid agent infrastructure.

### Axis G. Reporting and reproducibility

Searches cover TRIPOD-LLM, TRIPOD+AI, PROBAST+AI, MINIMAR, PRISMA-S, FAIR, FAIR4RS, and reproducible computational biology.[4,5]

## 6. Search terms and query construction

The historical research record preserves the major search concepts and the principal sources found, but it does not preserve the full exact text of every search-engine query from every exploratory pass. Exact historical query strings are therefore not reconstructed from memory.

Where exact query text is available from the recorded search activity, it is retained below. Later documentation will distinguish these from reconstructed search families.

### 6.1 Recent targeted prior-art queries recorded in the research activity

The following queries were run during the current prior-art update.

- "RECLAIM agents reproduce claims machine learning papers 2026 arxiv 2609.28850"
- "Performance failures oversight large language model agent clinical data analysis Wu 2026 JMIR e99597"
- "BioMedAgent biomedical data analysis agent Nature Biomedical Engineering 2026 01634-6"
- "DataSciBench ACL 2026 LLM agent benchmark data science 3685 3728"
- "PaperBench evaluating AI ability replicate AI research ICML 2025"
- "cell-free RNA diagnostic biomarker discovery LLM 50 times 2026 Nature Communications 74077"
- "FlowBench agentic bioinformatics planning fault recovery interpretation 2026"
- "LongHorizon-Harness fresh context independent auditor verified state 2026 arxiv"
- "HealthFlow progressive ablation planner reflector executor biomedical data analysis 2026 npj Digital Medicine"
- "CLEAR-Med deterministic validation independent validation agent clinical SQL analysis 2026"
- "Agentomics biomedical machine learning agent AUROC AUPRC repeated runs 2026 Bioinformatics"
- "free-tier LLM clinical data analysis 2026 consumer interface study"
- "ChatGPT Free clinical analysis study 2026 free tier LLM"

These searches were used to identify and verify high-yield recent studies. Exact search strings used in earlier exploratory passes are not all preserved in the exported record.

### 6.2 Methodological search update on 30 September 2026

The following searches were used to verify search and reporting methodology.

- "PRISMA-S 2021 Rethlefsen literature search reporting guideline 10.1186/s13643-020-01542-z"
- "PRISMA 2020 systematic review search strategies reporting 2021 BMJ"
- "PRESS peer review electronic search strategies guideline 2016"
- "TRIPOD-LLM 2025 Nature Medicine 31 60 69"
- "Reproducible computational biology 2020 PLoS Computational Biology e1007881"

These searches were performed as source verification searches rather than as substantive prior-art searches.

## 7. Inclusion criteria for scientific evidence

A source is eligible for the active evidence base when at least one of the following applies.

1. It reports empirical results directly relevant to LLM based scientific, clinical, biomedical, or data-analysis workflows.
2. It evaluates research reproduction, scientific data analysis, agent process quality, workflow reliability, or executable analysis.
3. It directly informs a design choice concerning verification, context management, auditing, execution, resource accounting, or reproducibility.
4. It establishes biomedical or computational facts needed to define the reference task.
5. It provides a formal reporting or methodological standard relevant to the study.
6. It documents the current configuration or accessibility of a consumer LLM system.
7. It identifies a close prior art or a failed novelty candidate.

A source can therefore be retained even when it argues against the proposed contribution. Such sources are important evidence and are not removed because they weaken the novelty case.

## 8. Exclusion criteria

Sources are not used as primary evidence when they are primarily promotional, unsupported commentary, or duplicate descriptions of a result available from a stronger authoritative source.

Search-result snippets are not treated as final evidence when the underlying publication or official source can be inspected.

A repository page is not treated as peer reviewed evidence unless it links to or contains an identifiable scientific publication or benchmark record that supports the specific claim.

News coverage and secondary summaries may be used for discovery, but substantive scientific claims are verified against the underlying paper, conference record, repository, or official provider source when available.

Preprints are retained when they contain relevant recent work, but their status is recorded and they are not silently treated as peer reviewed publications.

## 9. Screening and eligibility process

The present search uses a single-investigator screening process documented in the research record.

Screening occurs in four stages.

### Stage 1. Discovery

Potentially relevant records are identified through targeted keyword searches, direct source-site searches, cited references, benchmark repositories, review articles, and citation chaining.

### Stage 2. Title and abstract or summary screening

Records are retained when their task, system, workflow, or methodological content could materially affect the research question.

### Stage 3. Full-source verification

The publication, proceedings entry, preprint, or official document is inspected before an important scientific claim is entered into the evidence base.

### Stage 4. Evidence extraction

Relevant findings are recorded using a structured evidence representation.

No independent duplicate screening has been performed to date. The search therefore does not claim the inter-reviewer reliability expected of a conventional two-reviewer systematic review.

## 10. Evidence extraction

For each substantive source, the evidence record should preserve the following fields where applicable.

| Field | Recorded information |
|---|---|
| Citation | Verified bibliographic reference |
| Research question | What the source actually tested |
| Population or task | Dataset, task, cohort, or benchmark unit |
| Model type | LLM, agent, multimodel system, conventional ML, or other |
| Access mode | Consumer, API, local, institutional, research allocation, or unspecified |
| Dataset | Dataset and version when reported |
| Workflow architecture | Monolithic, staged, multi-agent, planner, validator, or other |
| Prompt structure | Main instruction, stages, reflection, audit, or equivalent |
| Context structure | Continuous, fresh-context, shared state, or other |
| Verification mechanism | Deterministic, LLM based, human, or absent |
| Human involvement | User, expert, repair, grading, or other intervention |
| Resource accounting | Cost, tokens, time, compute, retry limits, or unavailable |
| Biomedical metrics | AUROC, AUPRC, calibration, clinical measures, or other |
| Reproducibility design | Repeated runs, fresh sessions, seeds, held-out tests, or other |
| Overlap | Elements shared with the current study |
| Non-overlap | Elements that distinguish the source from the current study |
| Design implication | What the source changes or closes in the current design |

This structure is intentionally more detailed than a conventional narrative bibliography because the central task is to compare workflow designs, not merely to collect topic-matched papers.

## 11. Citation chaining

Backward and forward citation chaining is used selectively.

Backward chaining is applied to high-yield benchmark papers, recent biomedical LLM studies, methodological standards, and papers that appear to be close prior art.

Forward chaining is used when a source is central to a surviving or rejected novelty claim, especially for fast-moving 2025 to 2026 work.

Repository and benchmark pages are also followed when they lead to the peer reviewed paper, preprint, dataset documentation, or evaluation code that supports the relevant claim.

Citation chaining is particularly important for terms such as "agent", "reproduction", "verification", and "free tier", because different communities use these terms differently.

## 12. Grey literature and preprints

The study retains selected grey literature because the field is changing faster than conventional journal publication.

Preprints from arXiv, bioRxiv, and medRxiv are eligible when they contain primary methods or results directly relevant to the candidate design.

Grey literature is not pooled with peer reviewed evidence without marking the distinction.

Provider documentation is treated separately from both scientific literature and grey literature. It is required for current consumer access claims because pricing, tool availability, limits, and model presentation can change between publication dates.

## 13. Benchmark and repository discovery

Benchmark repositories are treated as evidence sources for implementation structure, task definitions, evaluation logic, and provenance.

Examples include repositories associated with ScienceAgentBench, benchmark implementations for data science and scientific analysis, and research code associated with current biomedical agent systems.

Repository evidence is checked against the associated paper or formal benchmark record when available.

The archived ECG repository remains a source of provenance for the candidate reference analysis. It is not treated as evidence supporting the external novelty claim.

## 14. Current consumer access search

The consumer-access component uses official provider documentation together with direct inspection of the consumer interface at the access date.

The eligibility specification requires all of the following.

- public consumer-facing online access
- zero monetary cost for the exact configuration used
- no paid subscription
- no API or API billing
- no promotional API credits
- no institutional, student, enterprise, or researcher entitlement
- no temporary promotional access
- no local model deployment
- no small language model selected for local execution
- general purpose rather than task-specific biomedical specialization
- every capability essential to the study available in the qualifying free consumer route

A free plan with usage limits qualifies under the zero monetary cost criterion. Unlimited use is not required.

A free underlying model accessed through a paid agent product does not qualify.

The exact interface, presented model identity, configuration, region, access date, tool availability, and observed usage limits must be recorded for every included system.

## 15. Quality and authority checks

Bibliographic metadata are verified against the strongest accessible source.

Priority is given to publisher or society records, PubMed, DOI metadata, proceedings records, or the original dataset source.

A URL alone is not sufficient to construct a final citation.

For peer reviewed articles, author list, article title, journal or proceedings, year, volume and pages or article number, and DOI are checked when available.

For preprints, the preprint status and version are recorded.

For provider documentation, the organization, page title, access date, and exact product configuration are recorded.

Search strategy quality is guided by PRISMA-S and, where a database-style strategy is sufficiently formalized, by the considerations in the PRESS guideline.[1,3]

## 16. Reconstructed source inventory

The exported research record contains a raw inventory of 222 unique non-chat URLs. The inventory includes 175 scholarly or research sources plus datasets, repository pages, provider documentation, and other supporting material.

This count is a provenance record from the exported research history. It is not a PRISMA study count, not a final bibliography count, and not an estimate of the number of eligible papers.

The inventory has not yet been normalized to DOI-level records across all sources. Duplicate versions of the same work may therefore occur across publisher, repository, preprint, and project pages.

The raw inventory is retained so that sources that influenced earlier decisions are not silently lost, including sources that later weakened or closed a candidate research question.

## 17. Search decision rules

The search record follows several rules.

### Rule 1

A source that materially changes the research question is retained even when it does not appear in the final narrative literature review.

### Rule 2

A source that closes a novelty claim remains part of the evidence base.

### Rule 3

A source does not become evidence for a claim merely because it uses similar terminology.

### Rule 4

A recent preprint can trigger a design change, but its publication status must remain explicit.

### Rule 5

Provider facts are time-stamped because they can change independently of the scientific literature.

### Rule 6

Investigator-defined choices are not rewritten as literature-derived conclusions.

### Rule 7

The final gap statement must be regenerated after the last literature update rather than copied forward from an earlier pass.

## 18. Evidence classification

Every substantive statement derived from the search record is assigned one of four classes.

**Evidence fact**

A directly supported fact from a peer reviewed paper, formal standard, official dataset source, or current official provider documentation.

**Evidence-supported inference**

A conclusion formed by considering multiple sources or by connecting an empirical finding to a methodological implication.

**Investigator-defined choice**

A deliberate study boundary or design decision selected to isolate the research question when the literature does not prescribe a unique solution.

**Computed result**

A quantity produced by analysis, simulation, or another reproducible computation.

The classification is carried forward into the protocol and statistical documents.

## 19. Relationship to the prior-art record

The current prior-art synthesis is recorded separately in [02 PRIOR ART AND GAP ANALYSIS.md](02%20PRIOR%20ART%20AND%20GAP%20ANALYSIS.md).

That document contains the current comparison of the candidate study with benchmark literature, biomedical agents, research reproduction, clinical LLM analysis, workflow verification, and free consumer evaluations.

This document instead answers a narrower methodological question.

It records how the evidence boundary was constructed and how future searches must be performed so that the prior-art statement remains auditable.

## 20. Planned final update

Before the study protocol is frozen, the search will be updated across the same major axes.

The update will prioritize work published or posted after the last substantive search, direct searches for the final W1 versus W2 wording and close synonyms, exact searches combining biomedical ML and workflow architecture, and any new evidence concerning free consumer access.

The final update will then be used to regenerate the prior-art matrix and the candidate gap statement.

No numerical experimental result will be used to define the search conclusion.

## 21. Limitations

The current record has several limitations.

The historical search was iterative rather than prospectively registered.

Exact search strings from all exploratory passes are not preserved in the exported record.

The evidence base spans several disciplines with different terminology and indexing practices.

Some recent work is available only as a preprint.

Current provider access changes over time.

The search has not yet undergone independent duplicate screening.

For these reasons, the current record supports a transparent targeted evidence synthesis but does not justify describing the literature review as exhaustive or systematic.

## References

1. Rethlefsen ML, Kirtley S, Waffenschmidt S, Ayala AP, Moher D, Page MJ, et al. PRISMA-S: an extension to the PRISMA statement for reporting literature searches in systematic reviews. Syst Rev. 2021;10:39. doi:10.1186/s13643-020-01542-z.

2. Page MJ, Moher D, Bossuyt PM, Boutron I, Hoffmann TC, Mulrow CD, et al. PRISMA 2020 explanation and elaboration: updated guidance and exemplars for reporting systematic reviews. BMJ. 2021;372:n160. doi:10.1136/bmj.n160.

3. McGowan J, Sampson M, Salzwedel DM, Cogo E, Foerster V, Lefebvre C. PRESS peer review of electronic search strategies: 2015 guideline statement. J Clin Epidemiol. 2016;75:40-46. doi:10.1016/j.jclinepi.2016.01.021.

4. Gallifant J, Afshar M, Ameen S, Aphinyanaphongs Y, Chen S, Cacciamani G, et al. The TRIPOD-LLM reporting guideline for studies using large language models. Nat Med. 2025;31(1):60-69. doi:10.1038/s41591-024-03425-5.

5. Papin JA, Mac Gabhann F, Sauro HM, Nickerson D, Rampadarath A. Improving reproducibility in computational biology research. PLoS Comput Biol. 2020;16(5):e1007881. doi:10.1371/journal.pcbi.1007881.

## Evidence status

References 1 through 5 were checked against publisher, PubMed, or journal records during the current methods update.

The scientific source inventory and prior-art references are maintained in the linked study documents rather than duplicated here.

The search remains open until the final protocol freeze.
