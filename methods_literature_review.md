# Methods literature review

I created this file because the methodological evidence has grown beyond what belongs comfortably in the main literature review.

The main literature review is for the scientific and clinical evidence behind the research question. This file is for evidence about how I should design, analyse, report and reproduce the study.

This is a working evidence review, not a systematic review. I searched by research question and design problem, followed relevant references, and kept papers that changed or clarified a decision. I am not claiming exhaustive coverage.

## Evidence standard

I am giving the most weight to

- peer-reviewed primary studies
- peer-reviewed statistical and methodological papers
- major reporting guidelines and consensus statements
- official dataset documentation when the question is about the dataset itself

I use preprints and general technical documentation only as supplementary evidence when a stronger source does not answer the specific question.

I am not treating a paper as evidence for a conclusion just because it uses PTB-XL or ECG machine learning. The relevance of each paper is limited to the question it actually studied.

## 1. Secondary-data research needs explicit reporting

My study uses an existing research dataset rather than collecting new participant data.

STROBE provides a general reporting framework for observational studies, but STROSA was developed because secondary-data analyses have additional reporting problems that ordinary STROBE items do not fully cover. The authors identified issues including data flow, the study protocol, the unit of analysis, internal validation and definition of variables, the advantages and limitations of secondary data, the role of data owners, and legal considerations.

STROSA-2 extends this work into a 27-criterion consensus standard. It is specifically grounded in German secondary health data, so I am using it as transferable methodological guidance rather than claiming compliance with it.

A 2026 update, Good Practice Secondary Data Analysis version 4, adds recommendations covering the study population, analysis strategy, registration, patient perspective, data dictionaries, interim analyses, distributed computing, documentation of analysis steps, legal framework and scientific communication. It is again focused on German health-related secondary data, so I will use the principles that transfer to PTB-XL rather than treating it as a study-specific checklist.

RECORD extends STROBE for routinely collected health data. PTB-XL is a curated research ECG dataset rather than routine administrative or electronic health record data, so RECORD is less directly applicable. I am keeping it as adjacent evidence rather than as a primary reporting framework.

For this study, the transferable lesson is simple. The protocol needs to state where the data came from, what the unit of analysis is, how records were selected and labelled, what the data flow was, and what analysis decisions were made before seeing the main result.

Sources

Swart and Schmitt 2014. STROSA. DOI 10.1016/j.zefq.2014.08.022.

Swart et al. 2016. STROSA-2. DOI 10.1055/s-0042-108647.

Swart et al. 2026. Good Practice Secondary Data Analysis, Version 4. DOI 10.1055/a-2904-1788.

Benchimol et al. 2015. RECORD. DOI 10.1371/journal.pmed.1001885.

von Elm et al. 2007. STROBE. DOI 10.1097/EDE.0b013e3181577654.

## 2. Statistical analysis plans and preregistration

The main reason to write the statistical analysis plan before the primary comparison is not formality. It is to make clear which choices were made before the result was known.

Watson 2025 provides a statistical analysis plan template for observational studies covering objectives, measures and variables, analytic methods and administrative details. The paper describes prespecification as a way to reduce ad hoc changes and improve transparency.

Thor et al. 2020 argues for registering analysis plans before inspecting the data in detail, with attention to hypotheses, primary outcomes, missing data, statistical methods and planned validation.

OSF also provides a Secondary Data Preregistration template. Its guidance is useful for documenting hypotheses, exclusions, variables, models, outcomes, unplanned analyses and anticipated deviations.

For this study I therefore want the formal protocol and statistical analysis plan to freeze, at minimum

- the target tasks and label rules
- the primary representation comparison
- the model and input representation
- the train, validation and test scheme
- the primary outcome and estimand
- the uncertainty procedure
- exclusions and missing-data handling
- the planned robustness analyses
- what will count as exploratory after the primary analysis

A later deviation is not automatically a flaw. The important point is to record it rather than silently rewriting the original plan.

Sources

Watson 2025. DOI 10.1007/s42519-025-00504-9.

Thor et al. 2020. DOI 10.3389/fonc.2020.00978.

OSF. Secondary Data Preregistration guidance. Accessed September 2026.

## 3. PTB-XL is a multilabel dataset with repeated records per patient

PTB-XL is not a simple one-label-per-record classification dataset.

The dataset contains multiple diagnostic statements for a record, which are aggregated into diagnostic superclasses and subclasses. The official version 1.0.3 documentation reports 9514 NORM records, 5469 MI records, 5235 STTC records, 4898 CD records and 2649 HYP records. These counts overlap because a record can have more than one diagnostic superclass.

This matters directly to the candidate HYP versus NORM and MI versus NORM tasks.

A binary task needs an explicit rule for overlapping labels. A record that contains both the target label and NORM is not equivalent to a record containing only the target label. Likewise, a target label can coexist with other diagnostic superclasses.

The data audit therefore needs to show, before the main comparison

- the exact label combinations present
- the number of records and patients in each combination
- how target-positive records are defined
- how negative records are defined
- which ambiguous combinations are excluded, if any
- how the exclusions affect class balance

I should not choose an exclusion rule after looking at model performance.

PTB-XL also contains multiple records for some patients. Its recommended fold variable keeps records from the same patient together. That prevents the most obvious patient overlap between train and test, but it does not make the records statistically independent within the test set.

This affects uncertainty estimation and interpretation.

A patient-clustered bootstrap has been described specifically for estimating diagnostic accuracy when multiple observations belong to the same patient. Rutter 2000 shows that bootstrap confidence intervals for measures such as AUROC can be constructed while respecting patient clustering.

For the current study, patient-level resampling is therefore a strong candidate for the uncertainty analysis. If a patient has several test records, the bootstrap would resample the patient and carry that patient's test records with it rather than resampling each record independently.

I will still keep the unit of the scientific target explicit. If the task is defined at the ECG-record level, I should not quietly convert it into a patient-level diagnosis by aggregating records.

Sources

Wagner et al. 2020. DOI 10.1038/s41597-020-0495-6.

PhysioNet PTB-XL version 1.0.3 documentation. Version DOI 10.13026/kfzx-aw45.

Rutter 2000. DOI 10.1016/S1076-6332(00)80381-5.

## 4. Normalization is not one operation

The word normalization is too vague to use by itself.

Recent ECG papers use materially different transformations, including global transformations, per-lead transformations and record-local scaling. A recent multi-lead ECG study defines a global z-score across retained leads and time points within each signal and explicitly contrasts this with per-lead normalization. The authors argue that independently normalizing each lead can obscure relative amplitude differences between leads.

Another recent ECG study uses channel-wise mean subtraction and keeps absolute amplitude information relevant to hypertrophy and ST-T changes. I am treating these papers as examples of methodological choices, not as evidence that one approach is clinically correct.

The current evidence therefore supports a more precise vocabulary

**Record-local normalization**

Parameters are calculated from the values in the same ECG record being transformed.

**Lead-local normalization**

Each lead has its own parameters, usually calculated from that lead within the record.

**Global record-local normalization**

One set of parameters is calculated from all retained leads and time points in one record and then applied to every lead in that record.

**Population-fitted normalization**

Parameters are estimated from a training population and then applied to other records. This must be handled with the same split discipline as any learned preprocessing step.

### Candidate primary normalization

The strongest current candidate for the primary normalized representation is a global record-wise z-score

x' = (x - mu_record) / sigma_record

where mu_record and sigma_record are calculated across the retained leads and time points of that record.

The reason this is attractive is not that the literature says it is the best ECG normalization. It is that it creates a clear controlled perturbation of the original representation. One common transformation is applied across all leads rather than independently rescaling each lead.

That means it removes the record's overall mean and scale while avoiding an additional lead-specific rescaling step.

This is still only a candidate. I do not want to freeze it until the data audit and input-representation decision are complete.

### Candidate sensitivity normalization

A record-wise per-lead z-score is a useful sensitivity condition because it is meaningfully different from the global transformation.

It independently centers and rescales each lead. That makes it a stronger test of what happens when between-lead amplitude scale is removed.

The point of this sensitivity analysis would be to answer a methodological question, not to search for the result that looks most interesting.

### Important limitation

A z-score is not pure amplitude scaling. It changes both location and scale.

The protocol therefore needs to say exactly what operation is being tested rather than describing every transformation as amplitude normalization.

Sources

Liu, Wu and Yuan 2026. ACL-ECG. DOI 10.3390/s26031080.

Su et al. 2026. An Edge-Cloud Collaborative ECG-Assisted Diagnostic System. DOI 10.3390/s26123753.

Bickmann et al. 2026. Architecture-Specific Impact of Preprocessing on Machine Learning Models for ECG Classification. DOI 10.3233/SHTI260227.

Safdar et al. 2024. DOI 10.1016/j.compbiomed.2023.107908.

## 5. Leakage and the boundary between record-local and learned preprocessing

Preprocessing can leak information when information from held-out data contributes to a transformation that is later used to evaluate the same held-out data.

This problem has been demonstrated empirically in machine-learning research. Data leakage can inflate performance when preprocessing, feature selection or related operations use information across training and test data.

The safe general rule is that any transformation that estimates parameters from a population should fit those parameters using only the training data and then apply them unchanged to validation or test data.

A record-local normalization is different because its parameters are derived from the record itself rather than from other records. It does not use the test labels or other patients' test data. I still need to make this operation explicit in the protocol because readers should be able to distinguish record-local transformation from population-fitted preprocessing.

Patient splitting should occur before any learned transformation, feature selection or model fitting that could transfer information across records.

Sources

Bickmann et al. 2026. DOI 10.3233/SHTI260227.

Nature Communications 2024. Data leakage inflates prediction performance in connectome-based machine learning models.

Leakage and the reproducibility crisis in machine-learning-based science. Peer-reviewed methodological investigation across multiple scientific fields.

Collins et al. 2024. TRIPOD+AI. DOI 10.1136/bmj-2023-078378.

## 6. Keeping the representation comparison paired

The raw and normalized inputs are generated from the same underlying ECG records.

That creates a paired comparison. The model is not being tested on two independently sampled populations. Each held-out record has two representations.

For AUROC, DeLong's method is a direct method for comparing correlated ROC curves.

A bootstrap comparison is also attractive because it can estimate the distribution of the performance difference and can be extended to patient-level resampling when several records belong to the same patient.

At this stage I do not want to freeze a p-value based analysis simply because DeLong is available. The more important decision is to define the estimand clearly.

The current candidate is

**Primary estimand candidate**

The difference in AUROC between the raw and normalized representations for the same predefined diagnostic task on the fixed held-out evaluation population.

The eventual uncertainty procedure should respect patient clustering. A patient-level paired bootstrap is therefore a strong candidate for a unified analysis of AUROC, AUPRC and other paired performance differences.

DeLong can remain a secondary or complementary AUROC comparison if its assumptions and the final prediction setup make it appropriate.

Sources

DeLong, DeLong and Clarke-Pearson 1988. PMID 3203132.

Rutter 2000. DOI 10.1016/S1076-6332(00)80381-5.

## 7. AUROC, AUPRC and class prevalence

AUROC is useful for ranking discrimination, but it does not directly reflect the prevalence of the positive class.

The precision-recall curve is particularly informative when classes are imbalanced because precision is directly affected by the positive-class prevalence.

PTB-XL diagnostic superclasses are not evenly distributed and the final binary task construction may change the balance further.

For that reason, I should report

- AUROC
- AUPRC
- the positive-class prevalence in each evaluation set
- uncertainty for the raw versus normalized difference

I do not need to force the same inferential test onto AUROC and AUPRC. A patient-level paired bootstrap can provide a common way to estimate uncertainty for both, provided the resampling and interval construction are fixed before the analysis.

Sources

Saito and Rehmsmeier 2015. DOI 10.1371/journal.pone.0118432.

Wagner et al. 2020. DOI 10.1038/s41597-020-0495-6.

## 8. Calibration should stay secondary to the main representation comparison

Discrimination asks whether the model can rank positive cases above negative cases.

Calibration asks whether predicted probabilities agree with observed outcome frequencies.

TRIPOD+AI recommends graphical assessment of calibration and distinguishes it from discrimination. The broader prediction-model literature also recommends examining calibration visually and, where appropriate, using quantities such as calibration-in-the-large and calibration slope rather than relying on a single significance test.

The Brier score measures the mean squared difference between predicted probabilities and binary outcomes. It can therefore provide a useful summary, but it does not replace a calibration plot because it combines multiple aspects of predictive performance.

For this study I am leaning toward

- calibration plot as the main calibration display
- Brier score as a summary measure
- calibration slope and intercept only if the final model and sample size make them informative

Calibration will remain secondary unless the research question changes.

Sources

Collins et al. 2024. TRIPOD+AI. DOI 10.1136/bmj-2023-078378.

Stevens and Poppe 2019. DOI 10.1016/j.jclinepi.2019.09.016.

## 9. What should count as information preservation

The word information can become misleading if it is used as a synonym for model performance.

I am separating three concepts

1. Numerical signal preservation. What numerical properties changed after transformation?
2. Clinically meaningful waveform structure. What morphology or amplitude relationships changed?
3. Task-relevant information available to the model. Did the fixed model retain useful predictive information for the target under the representation change?

The third is closest to the main research question, but it still does not justify a strong causal claim that normalization destroyed clinical information.

A lower AUROC could reflect many things, including model capacity, optimization, representation changes, label noise or task difficulty.

The main study should therefore phrase its conclusion in terms of predictive performance under a defined representation and evaluation setup.

Direct signal-level comparisons can be used as descriptive secondary analyses if they make the result easier to interpret. They should not be presented as proof of clinical information loss unless they actually measure that construct.

## 10. Robustness should test reasons for uncertainty, not provide a result search

A useful sensitivity analysis changes one scientifically defensible assumption at a time.

For this study, the most relevant candidates are

- a second normalization definition
- a stricter or alternative label rule decided before looking at the result
- a second simple model if the primary model is sensitive to a modelling assumption
- a second uncertainty procedure if the main inference depends strongly on it

A large grid of models, transformations and labels would make it difficult to distinguish a planned robustness test from selective result searching.

The recent PTB-XL preprocessing literature also gives a reason to keep model architecture fixed when the scientific question is the effect of representation. Bickmann et al. 2026 showed that preprocessing effects can depend on architecture. Changing the architecture and preprocessing at the same time would answer a different question.

Source

Bickmann et al. 2026. DOI 10.3233/SHTI260227.

## 11. Reproducibility is part of the research design

For a computational study, reproducibility is not just a final GitHub upload.

Sandve et al. 2013 recommend keeping track of how every computational result was produced, including software versions, parameters and inputs. This fits the current repository approach.

The FAIR principles also treat algorithms, tools and workflows as research objects that benefit from findability, accessibility, interoperability and reuse.

For this study I therefore need to record

- dataset version and source
- software environment and package versions
- preprocessing definitions
- model configuration
- random seeds where randomness is used
- fold assignments
- generated data boundaries
- exact analysis commands or reproducible entry points
- repository commit associated with a result
- deviations from the preregistered or prespecified plan

The raw PTB-XL data should remain outside the public repository. The repository should still contain enough information to reconstruct the analysis environment and derived outputs.

Sources

Sandve et al. 2013. DOI 10.1371/journal.pcbi.1003285.

Wilkinson et al. 2016. DOI 10.1038/sdata.2016.18.

## 12. Independent reproduction

The planned independent reproduction by Zaid is useful because it tests more than whether the code runs.

The clean reproduction should start from the public repository and the stated environment, without giving the expected result in advance. It should record the repository commit, data version, command used, environment and any discrepancy.

A mismatch is not automatically evidence that the original result was wrong. It is evidence that something in the data, code, environment or interpretation needs to be traced.

The goal is to make the primary result reconstructible by a second person from the research record.

## 13. AI-assisted research needs source verification

The current evidence does not support treating generative AI as an unrestricted replacement for human evidence synthesis.

A 2025 systematic review of GenAI in evidence synthesis found substantial error and omission rates across searching, screening and data extraction tasks. The reported performance varied by task and system, so the numbers should not be generalized to every current model. The methodological conclusion that matters for this study is that unsupervised AI evidence synthesis is not adequately reliable for high-stakes scientific decisions.

For this project, AI can assist with

- generating search terms
- finding candidate papers
- summarising papers after retrieval
- drafting code
- debugging
- documentation
- adversarial review of the study plan

But the source of a scientific claim remains the original paper, dataset documentation or analysis output.

The repository's AI note should therefore stay factual and short. It should record meaningful AI assistance and how the result was verified, not become a second narrative about the use of AI.

Source

Clark et al. 2025. DOI 10.1017/rsm.2025.16.

## 14. Reporting framework map

I do not want to claim compliance with every checklist I read. The study type matters.

**TRIPOD+AI**

Useful for prediction-model development and evaluation reporting, especially participant flow, predictors, outcome definition, model development, performance and calibration.

**PROBAST+AI**

Useful as a risk-of-bias and applicability self-audit across participants or data sources, predictors, outcomes and analysis.

**STROBE**

Useful for relevant observational reporting elements, especially describing the data source and study population.

**STROSA and Good Practice Secondary Data Analysis**

Useful because this is a secondary-data study. I will use the transferable items around data flow, unit of analysis, definitions, data sources, analysis documentation and registration.

**SPIRIT 2025**

Useful only for protocol discipline where its concepts transfer. It is primarily a randomised-trial protocol framework, so I will not claim SPIRIT compliance.

**PRISMA 2020 and PRISMA-S**

Useful only if the literature search becomes a genuine systematic review. The current search is not being called a systematic review.

**FAIR**

Useful for the repository, provenance and reuse of computational research objects.

**NeurIPS paper checklist**

Useful as a secondary transparency and reproducibility checklist for the machine-learning component. It is not a claim about publication venue or formal compliance.

## 15. What the evidence currently supports

The following now look defensible as design principles, but several still need to be frozen in the protocol.

1. The study should be treated as a secondary-data computational study with explicit data flow, unit of analysis, label construction and preprocessing definitions.

2. PTB-XL label overlap must be quantified and the binary task construction must be frozen before the primary result.

3. Patient identity must remain in the data split, and the provided patient-aware PTB-XL folds are preferable to a random record-level split for the primary evaluation.

4. The primary representation comparison should keep the diagnostic task, model, input handling, training procedure and evaluation set fixed while changing only the defined representation.

5. A global record-wise z-score is currently the clearest candidate for the primary normalization because it applies one transformation across leads within each record. A per-lead record-wise z-score is a useful candidate sensitivity analysis.

6. Any transformation that learns population-level parameters must be fitted on training data only. Record-local transformations need their local scope stated explicitly.

7. AUROC and AUPRC should be reported together with positive-class prevalence. The raw versus normalized comparison is paired because both predictions come from the same held-out records.

8. A patient-level bootstrap is currently the strongest candidate for uncertainty because PTB-XL can contain multiple records per patient.

9. Calibration should be secondary and should be shown graphically, with Brier score as a useful summary.

10. The main interpretation should be about predictive behaviour under a defined representation, not proof that clinical information was or was not lost.

11. Robustness analyses should test prespecified methodological concerns rather than search across many alternatives.

12. The repository should capture the environment, code version, dataset version, parameters and analysis provenance well enough for independent reproduction.

## 16. Important questions still open

The methodological pass has narrowed the questions, but it has not finished the study design.

The most important unresolved issue is the model input representation. Logistic regression and random forest are currently listed as simple models, but the protocol still needs to specify how the 12-lead waveform is converted into model input. Flattening a long multilead waveform, engineering features, dimensionality reduction and using a direct waveform model are not equivalent choices.

The following must be resolved before the formal protocol is frozen

- exact model input representation
- exact candidate normalization formula and scope
- final label construction and exclusions
- the scientific unit of observation
- primary model
- primary estimand
- patient-level bootstrap implementation and interval method
- calibration implementation
- missing or unusable waveform handling
- minimum robustness analysis
- exact reproducibility entry point

The next step is therefore the PTB-XL data audit and a focused decision on model input representation. The formal protocol should be written only after those decisions are supported by the data and the evidence review.
