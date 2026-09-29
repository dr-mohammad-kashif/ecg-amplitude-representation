# Methods literature review

I created this document to keep the detailed methodological evidence separate from the shorter methods synthesis. It supports the design of the study but is not the final protocol and is not presented as a systematic review.

The citations use numbered Vancouver-style references. The numbered reference list appears at the end of the document. (1,2)

## Secondary-data study design and reporting

This study uses an existing research dataset rather than collecting new participant data.

STROBE is a general reporting framework for observational studies. STROSA and STROSA-2 were developed specifically to address additional reporting problems in secondary-data analyses, including data flow, the study protocol, unit of analysis, variable definitions, internal validation, data sources and limitations. A 2026 update, Good Practice Secondary Data Analysis version 4, provides current guidance for secondary-data research on study population, analysis strategy, registration, data dictionaries and documentation. (3-6)

RECORD is designed for studies using routinely collected health data. PTB-XL is a curated research ECG dataset rather than routine administrative or electronic health-record data, so I treat RECORD as adjacent guidance rather than the primary reporting framework. (7)

The practical lesson for this study is that the protocol needs to state where the data came from, which records were included, what the unit of analysis is, how labels were constructed, what the data flow was and which analytical decisions were specified before the primary result.

## Statistical analysis plans and preregistration

The reason for writing the statistical analysis plan before the primary comparison is to distinguish prespecified analysis from decisions made after seeing the result.

Watson provides a statistical analysis plan template for observational studies covering objectives, variables, analytic methods and documentation. Thor et al. recommend public preregistration of outcome-modeling analysis plans and describe a structure that includes study scope, hypotheses, primary outcomes, missing-data handling, resampling, statistical functions, variables and validation. (8,9)

OSF also provides a Secondary Data Preregistration framework. For this study, the eventual protocol and analysis plan should freeze at least the task definitions, label rules, primary representation comparison, model and input representation, split scheme, primary outcome, estimand, uncertainty method, exclusions and planned robustness analyses.

A later deviation is not automatically a flaw. It should be recorded as a deviation rather than silently replacing the original plan.

## PTB-XL labels and patient structure

PTB-XL is multilabel. The official version 1.0.3 documentation reports 9514 NORM records, 5469 MI records, 5235 STTC records, 4898 CD records and 2649 HYP records, and explicitly notes that these counts overlap because one record may carry multiple diagnostic labels. The dataset also contains multiple ECG records for some patients and provides a stratified fold variable that keeps all records from a patient in the same fold. (10)

This means the HYP versus NORM and MI versus NORM tasks cannot be frozen without first quantifying actual label combinations.

Before the main comparison, I need to know

- which records have target and NORM simultaneously
- which target labels coexist with other diagnostic superclasses
- how many records and patients remain under each candidate rule
- how the exclusions affect class balance
- whether any waveform records are unusable

The exclusion rules should be fixed before the primary result is interpreted.

The patient-aware folds prevent the most obvious patient overlap between training and test sets, but repeated records from the same patient are still not independent observations for uncertainty estimation.

Rutter describes a bootstrap approach for diagnostic accuracy measures when observations are clustered by patient. This makes patient-level resampling a strong candidate for this study. (11)

## Defining normalization precisely

Normalization is not one operation.

ECG studies use different scopes and transformations, including global, per-lead and record-local transformations. Liu et al. describe a global z-score transformation and discuss the consequences of independently normalizing ECG leads. Su et al. provide another example in which absolute amplitude is deliberately retained in a multilead system. Bickmann et al. also show that preprocessing effects can depend on model architecture. (12-14)

I therefore use four working categories

**Record-local normalization**

Parameters are calculated from the same ECG record being transformed.

**Lead-local normalization**

Each lead has its own parameters, generally calculated from that lead within the record.

**Global record-local normalization**

One set of parameters is calculated from all retained leads and time points within a record.

**Population-fitted normalization**

Parameters are estimated from a training population and then applied to other records. Any such parameters must be estimated from training data only.

The current primary candidate is a global record-wise z-score

x' = (x - mu_record) / sigma_record

where the mean and standard deviation are calculated across the retained leads and time points of that record.

The current sensitivity candidate is a record-wise per-lead z-score.

These are candidate conditions rather than final protocol decisions. A z-score changes both location and scale, so the protocol should describe the exact mathematical transformation rather than using the broad word normalization by itself.

## Leakage and preprocessing boundaries

Preprocessing can create leakage when information from held-out data contributes to a transformation used for evaluation.

The operational rule for this study is that any transformation that learns population-level parameters will be fitted using the training data only and then applied unchanged to validation and test data. Record-local transformations are different because their parameters come from the individual record itself.

Patient splitting therefore needs to occur before any learned population-level transformation, feature selection or model fitting that could transfer information across records.

TRIPOD+AI also emphasises clear reporting of predictors, outcomes, model development and performance evaluation in prediction-model studies. PROBAST+AI provides a complementary framework for considering bias and applicability across participants or data sources, predictors, outcomes and analysis. (15,16)

## Paired representation comparison

The raw and normalized conditions use the same underlying ECG records. Predictions on the held-out set are therefore paired.

DeLong's method provides a standard comparison for correlated ROC curves. (17)

A patient-level paired bootstrap is also attractive because it can estimate the distribution of the performance difference while respecting the fact that several records may belong to one patient. I currently prefer this as the main uncertainty candidate, with DeLong considered as a complementary AUROC comparison if appropriate for the final design.

The current primary estimand candidate is the difference in AUROC between the raw and normalized representations for the same predefined diagnostic task on the fixed held-out evaluation population.

## AUROC, AUPRC and class prevalence

AUROC measures discrimination across thresholds but does not directly reflect the prevalence of the positive class.

Precision-recall analysis is particularly informative when the positive class is uncommon because precision depends on prevalence. (18)

The primary performance report should therefore include AUROC, AUPRC and the positive-class prevalence for each task, along with uncertainty for the paired raw versus normalized difference.

## Calibration

Calibration is distinct from discrimination.

TRIPOD+AI recommends assessment of calibration in prediction-model studies, and the broader calibration literature distinguishes calibration-in-the-large and calibration slope from discrimination measures. The Brier score provides a summary based on squared probability error. (15,19)

For this study, calibration is currently secondary. The planned display is a calibration plot with Brier score as a summary measure. Calibration slope and intercept will only be added if the final model and evaluation sample make them informative.

## Information preservation

I no longer treat information preservation as one undifferentiated outcome.

I distinguish

1. numerical signal preservation
2. preservation of clinically meaningful waveform structure
3. task-relevant information available to the model

The third is closest to the main research question, but a change in model performance does not by itself prove that clinical information has been destroyed. Performance can also change because of model capacity, optimization, label noise and other properties of the representation.

The main interpretation should therefore be about predictive behaviour under a defined representation and evaluation, not about proving clinical information loss.

## Robustness

A useful sensitivity analysis should answer a specific methodological concern rather than create a grid of alternatives from which a favourable result can be selected.

The most relevant candidates are a prespecified alternative normalization definition, a prespecified alternative label rule, or a second simple model if the primary model depends on a methodological assumption.

Because recent PTB-XL work shows that preprocessing can interact with architecture, changing model architecture and preprocessing at the same time would answer a different question. (14)

## Reproducibility

For a computational study, reproducibility requires more than publishing the final code.

Sandve et al. describe practical rules for reproducible computational research, including recording software, parameters, inputs and the path used to obtain each result. The FAIR principles extend this idea to data, algorithms, tools and workflows by emphasising findability, accessibility, interoperability and reusability. (20,21)

For this study I therefore need to record

- dataset version and source
- software environment and package versions
- preprocessing definitions
- model configuration
- random seeds where applicable
- fold assignments
- boundaries between raw and derived data
- reproducible commands or entry points
- the repository commit associated with each result
- deviations from the prespecified plan

The raw PTB-XL data will remain outside the public repository.

## Independent reproduction

Zaid's planned reproduction should begin from a clean copy of the public repository and the stated environment without being given the expected result in advance.

The reproduction record should identify the repository commit, dataset version, environment, command and any discrepancy.

A mismatch should trigger a trace through the data, code, environment and interpretation rather than being hidden.

## AI-assisted research

Generative AI can assist with literature discovery, search-term generation, code drafting, debugging and documentation, but the output itself is not evidence.

A 2025 systematic review of generative AI in evidence synthesis found substantial task-dependent errors and missed studies in several evidence-synthesis tasks. The authors concluded that current evidence does not justify unsupervised use for high-stakes evidence synthesis. (22)

For this project I therefore keep the model in an accelerator role. Scientific claims are checked against the original paper, dataset documentation or the project's own outputs.

## Reporting framework map

I will use reporting frameworks according to study type rather than claiming that the project complies with every checklist.

**TRIPOD+AI**

Relevant to prediction-model development and evaluation. (15)

**PROBAST+AI**

Relevant as a risk-of-bias and applicability self-audit for prediction-model work. (16)

**STROBE**

Relevant for appropriate observational reporting elements. (3)

**STROSA and Good Practice Secondary Data Analysis**

Relevant to the secondary-data structure of this study. (4-6)

**SPIRIT 2025**

Useful only for transferable protocol-discipline ideas because it is principally a randomised-trial protocol framework. (23)

**PRISMA 2020 and PRISMA-S**

Applicable only if this literature search becomes a true systematic review. The current literature review is not described as one. (24,25)

**FAIR**

Relevant to provenance, research objects and reproducibility. (21)

**NeurIPS checklist**

Useful as a secondary transparency check for the machine-learning component, not as a claim about submission to NeurIPS.

## Current design conclusions

The evidence currently supports the following principles

1. Treat the project as a secondary-data computational study with explicit data flow, unit of analysis, label construction and preprocessing definitions.
2. Quantify PTB-XL label overlap before freezing the binary tasks.
3. Preserve patient identity in splitting and uncertainty estimation.
4. Keep the diagnostic task, model, input construction, training procedure and evaluation set fixed when testing the representation effect.
5. Use an explicitly defined normalization formula rather than the generic term normalization.
6. Fit population-level preprocessing parameters on training data only.
7. Report AUROC and AUPRC together with positive-class prevalence.
8. Use a patient-level bootstrap as the leading uncertainty candidate for paired performance differences.
9. Keep calibration secondary unless the research question changes.
10. Interpret the main finding as a representation effect under the defined evaluation rather than proof of clinical information loss.
11. Prespecify robustness analyses.
12. Record environment and provenance well enough for independent reproduction.

## Remaining decisions

The largest unresolved methodological issue is still the model input representation.

The current plan lists logistic regression and random forest, but the full multilead waveform has not yet been assigned a fixed representation for those models. Flattening the signal, engineering features, reducing dimensionality and using a direct waveform model would create different experiments.

The data audit must therefore come first.

## References

1. International Committee of Medical Journal Editors. Recommendations for the conduct, reporting, editing, and publication of scholarly work in medical journals: preparing a manuscript for submission to a medical journal. ICMJE. Available from: https://www.icmje.org/recommendations/browse/manuscript-preparation/preparing-for-submission.html
2. Patrias K, Wendling DL, technical editor. Citing medicine: the NLM style guide for authors, editors, and publishers. 2nd ed. Bethesda (MD): National Library of Medicine (US); 2007-2015.
3. von Elm E, Altman DG, Egger M, Pocock SJ, Gotzsche PC, Vandenbroucke JP; STROBE Initiative. The Strengthening the Reporting of Observational Studies in Epidemiology (STROBE) statement: guidelines for reporting observational studies. Epidemiology. 2007;18(6):800-804. doi:10.1097/EDE.0b013e3181577654.
4. Swart E, Schmitt J. STandardized Reporting Of Secondary data Analyses, a recommendation. Z Evid Fortbild Qual Gesundhwes. 2014;108(9):511-516. doi:10.1016/j.zefq.2014.08.022.
5. Swart E, et al. A consensus German reporting standard for secondary data analyses, version 2 (STROSA-2). Gesundheitswesen. 2016;78(Suppl 1):e145-e160. doi:10.1055/s-0042-108647.
6. Swart E, Alibone M, Epping J, Grobe TG, Hoffmann F, Horenkamp-Sonntag D, et al. Good Practice Secondary Data Analysis: Guidelines and Recommendations, Version 4. Gesundheitswesen. 2026. doi:10.1055/a-2904-1788.
7. Benchimol EI, Smeeth L, Guttmann A, Harron K, Moher D, Petersen I, et al. The REporting of studies Conducted using Observational Routinely-collected health Data (RECORD) statement. PLoS Med. 2015;12(10):e1001885. doi:10.1371/journal.pmed.1001885.
8. Watson HJ. A statistical analysis plan template for observational studies: promoting quality and rigor in research. J Stat Theory Pract. 2025;19:91. doi:10.1007/s42519-025-00504-9.
9. Thor M, Oh JH, Apte AP, Deasy JO. Registering study analysis plans (SAPs) before dissecting your data: updating and standardizing outcome modeling. Front Oncol. 2020;10:978. doi:10.3389/fonc.2020.00978.
10. Wagner P, Strodthoff N, Bousseljot R-D, Samek W, Schaeffter T. PTB-XL, a large publicly available electrocardiography dataset (version 1.0.3). PhysioNet. 2022. doi:10.13026/kfzx-aw45.
11. Rutter CM. Bootstrap estimation of diagnostic accuracy with patient-clustered data. Acad Radiol. 2000;7(6):413-419. doi:10.1016/S1076-6332(00)80381-5.
12. Liu W, Wu Z, Yuan Z. ACL-ECG: anatomy-aware contrastive learning for multi-lead electrocardiograms. Sensors (Basel). 2026;26(3):1080. doi:10.3390/s26031080.
13. Su H, Wang S, Wang H, Qiu K. An edge-cloud collaborative ECG-assisted diagnostic system leveraging cross-lead knowledge distillation and large language models. Sensors (Basel). 2026;26(12):3753. doi:10.3390/s26123753.
14. Bickmann L, Plagwitz L, Büscher A, Varghese J. Architecture-specific impact of preprocessing on machine learning models for ECG classification. Stud Health Technol Inform. 2026;336:529-533. doi:10.3233/SHTI260227.
15. Collins GS, Moons KGM, Dhiman P, Riley RD, Beam AL, Van Calster B, et al. TRIPOD+AI statement: updated guidance for reporting clinical prediction models that use regression or machine learning methods. BMJ. 2024;385:e078378. doi:10.1136/bmj-2023-078378.
16. Moons KGM, Damen JAA, Kaul T, et al. PROBAST+AI: an updated quality, risk of bias, and applicability assessment tool for prediction models using regression or artificial intelligence methods. BMJ. 2025;388:e082505. doi:10.1136/bmj-2024-082505.
17. DeLong ER, DeLong DM, Clarke-Pearson DL. Comparing the areas under two or more correlated receiver operating characteristic curves: a nonparametric approach. Biometrics. 1988;44(3):837-845. PMID:3203132.
18. Saito T, Rehmsmeier M. The precision-recall plot is more informative than the ROC plot when evaluating binary classifiers on imbalanced datasets. PLoS One. 2015;10(3):e0118432. doi:10.1371/journal.pone.0118432.
19. Stevens RJ, Poppe KK. Validation of clinical prediction models: what does the calibration slope really measure? J Clin Epidemiol. 2020;122:93-99. doi:10.1016/j.jclinepi.2019.09.016.
20. Sandve GK, Nekrutenko A, Taylor J, Hovig E. Ten simple rules for reproducible computational research. PLoS Comput Biol. 2013;9(10):e1003285. doi:10.1371/journal.pcbi.1003285.
21. Wilkinson MD, Dumontier M, Aalbersberg I, Appleton G, Axton M, Baak A, et al. The FAIR Guiding Principles for scientific data management and stewardship. Sci Data. 2016;3:160018. doi:10.1038/sdata.2016.18.
22. Clark J, Barton B, Albarqouni L, et al. Generative artificial intelligence use in evidence synthesis: a systematic review. Res Synth Methods. 2025;16:601-619. doi:10.1017/rsm.2025.16.
23. SPIRIT 2025. SPIRIT 2025 statement: updated guideline for protocols of randomised trials. BMJ. 2025;389:e081477. doi:10.1136/bmj-2024-081477.
24. Page MJ, McKenzie JE, Bossuyt PM, Boutron I, Hoffmann TC, Mulrow CD, et al. The PRISMA 2020 statement: an updated guideline for reporting systematic reviews. BMJ. 2021;372:n71. doi:10.1136/bmj.n71.
25. Rethlefsen ML, Kirtley S, Waffenschmidt S, Ayala AP, Moher D, Page MJ, et al. PRISMA-S: an extension to the PRISMA statement for reporting literature searches in systematic reviews. Syst Rev. 2021;10(1):39. doi:10.1186/s13643-020-01542-z.
26. Pollard T, Moody BE, Lehman L, Gow B, Fernandes C, Xie C, et al. PhysioNet as a global platform for biomedical research. Nat Health. 2026. doi:10.1038/s44360-026-00096-z.
