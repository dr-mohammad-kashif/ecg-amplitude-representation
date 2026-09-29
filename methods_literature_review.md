# Methods literature review

I created this document to keep the detailed methodological evidence separate from the shorter methods synthesis. It supports the design of the study but is not the final protocol and is not presented as a systematic review.

The citations use a numbered Vancouver-style reference system. References are listed at the end in the order in which they are first cited.

## Secondary-data study design and reporting

This study uses an existing research dataset rather than collecting new participant data.

STROBE is a general reporting framework for observational studies. STROSA and STROSA-2 were developed specifically to address additional reporting problems in secondary-data analyses, including data flow, the study protocol, unit of analysis, variable definitions, internal validation, data sources and limitations. A 2026 update, Good Practice Secondary Data Analysis version 4, provides current guidance for secondary-data research on study population, analysis strategy, registration, data dictionaries and documentation. (1-4)

RECORD is designed for studies using routinely collected health data. PTB-XL is a curated research ECG dataset rather than routine administrative or electronic health-record data, so I treat RECORD as adjacent guidance rather than the primary reporting framework. (5)

The practical lesson for this study is that the protocol needs to state where the data came from, which records were included, what the unit of analysis is, how labels were constructed, what the data flow was and which analytical decisions were specified before the primary result.

## Statistical analysis plans and preregistration

The reason for writing the statistical analysis plan before the primary comparison is to distinguish prespecified analysis from decisions made after seeing the result.

Watson provides a statistical analysis plan template for observational studies covering objectives, variables, analytic methods and documentation. Thor et al. recommend public preregistration of outcome-modeling analysis plans and describe a structure that includes study scope, hypotheses, primary outcomes, missing-data handling, resampling, statistical functions, variables and validation. (6,7)

OSF provides a Secondary Data Preregistration template and recommends making design and analysis decisions before viewing the data, stating hypotheses and variables precisely, defining exclusion rules and planned outcomes, and documenting deviations. For this study, the eventual protocol and analysis plan should freeze at least the task definitions, label rules, primary representation comparison, model and input representation, split scheme, primary outcome, estimand, uncertainty method, exclusions and planned robustness analyses. (8)

A later deviation is not automatically a flaw. It should be recorded as a deviation rather than silently replacing the original plan.

## PTB-XL labels and patient structure

PTB-XL is multilabel. The official version 1.0.3 documentation reports 9514 NORM records, 5469 MI records, 5235 STTC records, 4898 CD records and 2649 HYP records, and explicitly notes that these counts overlap because one record may carry multiple diagnostic labels. The dataset also contains multiple ECG records for some patients and provides a stratified fold variable that keeps all records from a patient in the same fold. (9)

This means the HYP versus NORM and MI versus NORM tasks cannot be frozen without first quantifying actual label combinations.

Before the main comparison, I need to know

- which records have target and NORM simultaneously
- which target labels coexist with other diagnostic superclasses
- how many records and patients remain under each candidate rule
- how the exclusions affect class balance
- whether any waveform records are unusable

The exclusion rules should be fixed before the primary result is interpreted.

The patient-aware folds prevent the most obvious patient overlap between training and test sets, but repeated records from the same patient are still not independent observations for uncertainty estimation.

Rutter describes a bootstrap approach for diagnostic accuracy measures when observations are clustered by patient. This makes patient-level resampling a strong candidate for this study. (12)

## Defining normalization precisely

Normalization is not one operation.

ECG studies use different scopes and transformations, including global, per-lead and record-local transformations. Liu et al. describe a global z-score transformation and discuss the consequences of independently normalizing ECG leads. Su et al. provide another example in which absolute amplitude is deliberately retained in a multilead system. Bickmann et al. also show that preprocessing effects can depend on model architecture. (13-15)

I therefore use four working categories

**Record-local normalization**

Parameters are calculated from the same ECG record being transformed.

**Lead-local normalization**

Each lead has its own parameters, generally calculated from that lead within the record.

**Global record-local normalization**

One set of parameters is calculated from all retained leads and time points within a record.

**Population-fitted normalization**

Parameters are estimated from a training population and then applied to other records. Any such parameters must be estimated from training data only.

The primary transformation is a global record-wise z-score

x' = (x - mu_record) / sigma_record

where the mean and standard deviation are calculated across the retained leads and time points of that record.

The prespecified sensitivity transformation is a record-wise per-lead z-score.

The primary global transformation changes both location and scale while using one scalar mean and standard deviation for all leads within a record. The prespecified per-lead transformation removes lead-specific scale as well and therefore changes inter-lead amplitude relationships. The protocol will describe these operations mathematically rather than using the broad word normalization by itself.

## Leakage and preprocessing boundaries

Preprocessing can create leakage when information from held-out data contributes to a transformation used for evaluation.

The operational rule for this study is that any transformation that learns population-level parameters will be fitted using the training data only and then applied unchanged to validation and test data. Record-local transformations are different because their parameters come from the individual record itself.

Patient splitting therefore needs to occur before any learned population-level transformation, feature selection or model fitting that could transfer information across records.

TRIPOD+AI also emphasises clear reporting of predictors, outcomes, model development and performance evaluation in prediction-model studies. PROBAST+AI provides a complementary framework for considering bias and applicability across participants or data sources, predictors, outcomes and analysis. (16,17)

## Model input representation

The data audit confirms that PTB-XL provides both 500 Hz and 100 Hz versions of the same 10-second, 12-lead recordings. The official dataset documentation presents the 100 Hz version as a downsampled convenience version and the 500 Hz version as the higher-resolution waveform. Recent PTB-XL studies use both choices, including direct 100 Hz waveform inputs and 500 Hz waveform inputs. (9,10,11)

The representation question in this study is about amplitude normalization. I therefore want the model input to stay as close to the waveform itself as practical. A feature-engineering pipeline would add another layer in which amplitude could be transformed, discarded or summarized before the model sees the data. That would make it harder to attribute a change in performance to the normalization condition alone.

A direct waveform model keeps the comparison cleaner. The same lead order, sample rate, signal length, model architecture, training procedure and evaluation data can be used for the raw and normalized conditions.

The primary input is the native 100 Hz PTB-XL waveform because it reduces each 10-second record to 1,000 samples per lead while retaining the full 12-lead structure. This makes the direct waveform experiment more computationally manageable without introducing a second resampling rule of my own. Recent PTB-XL work has used 100 Hz signals for raw ECG learning, while other studies have used the 500 Hz release. (10,11)

The primary model is a compact three-block 1D convolutional model. This is not because convolutional models are universally best for ECGs. It is because they can take the multilead waveform directly and allow the representation comparison to be made without first replacing the waveform with handcrafted features.

The model choice and training configuration are fixed in analysis_plan.md. I am not using logistic regression or random forest as primary baselines because applying them to the full waveform would require another representation choice.

The important control is unchanged. Whatever model is selected, the architecture and all training settings must be identical between raw and normalized conditions.

## Paired representation comparison

The raw and normalized conditions use the same underlying ECG records. Predictions on the held-out set are therefore paired.

DeLong's method provides a standard comparison for correlated ROC curves. (18)

A patient-level paired percentile bootstrap is the primary inferential procedure because several records can belong to one patient. DeLong is not used as the primary procedure because its standard formulation does not account for repeated records within patients.

The primary estimand is the cross-task contrast between the two task-specific AUROC changes. For task t, Delta_t is AUROC_normalized,t minus AUROC_raw,t, and the primary contrast is Delta_HYP minus Delta_MI.

## AUROC, AUPRC and class prevalence

AUROC measures discrimination across thresholds but does not directly reflect the prevalence of the positive class.

Precision-recall analysis is particularly informative when the positive class is uncommon because precision depends on prevalence. (19)

The primary performance report should therefore include AUROC, AUPRC and the positive-class prevalence for each task, along with uncertainty for the paired raw versus normalized difference.

## Calibration

Calibration is distinct from discrimination.

TRIPOD+AI recommends assessment of calibration in prediction-model studies, and the broader calibration literature distinguishes calibration-in-the-large and calibration slope from discrimination measures. The Brier score provides a summary based on squared probability error. (16,20)

For this study, calibration is currently secondary. The planned display is a calibration plot with Brier score as a summary measure. I will only consider calibration slope and intercept if the final model and evaluation sample make them informative.

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

Because recent PTB-XL work shows that preprocessing can interact with architecture, changing model architecture and preprocessing at the same time would answer a different question. (15)

## Reproducibility

For a computational study, reproducibility requires more than publishing the final code.

Sandve et al. describe practical rules for reproducible computational research, including recording software, parameters, inputs and the path used to obtain each result. The FAIR principles extend this idea to data, algorithms, tools and workflows by emphasising findability, accessibility, interoperability and reusability. FAIR4RS further adapts the FAIR approach specifically to research software. (21-23)

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

A 2025 systematic review of generative AI in evidence synthesis found substantial task-dependent errors and missed studies in several evidence-synthesis tasks. The authors concluded that current evidence does not justify unsupervised use for high-stakes evidence synthesis. (24)

For this project I therefore keep the model in an accelerator role. Scientific claims are checked against the original paper, dataset documentation or the project's own outputs.

## Reporting framework map

I will use reporting frameworks according to study type rather than claiming that the project complies with every checklist.

**TRIPOD+AI**

Relevant to prediction-model development and evaluation. (16)

**PROBAST+AI**

Relevant as a risk-of-bias and applicability self-audit for prediction-model work. (17)

**STROBE**

Relevant for appropriate observational reporting elements. (1)

**STROSA and Good Practice Secondary Data Analysis**

Relevant to the secondary-data structure of this study. (2-4)

**SPIRIT 2025**

Useful only for transferable protocol-discipline ideas because it is principally a randomised-trial protocol framework. (25)

**PRISMA 2020 and PRISMA-S**

Applicable only if this literature search becomes a true systematic review. The current literature review is not described as one. (26,27)

**FAIR and FAIR4RS**

Relevant to provenance, research objects and research software. (22,23)

**NeurIPS checklist**

Useful as a secondary transparency check for the machine-learning component, not as a claim about submission to NeurIPS. The checklist explicitly focuses on reproducibility, transparency, research ethics and societal impact. (28)

## Current design conclusions

The evidence currently supports the following principles

1. Treat the project as a secondary-data computational study with explicit data flow, unit of analysis, label construction and preprocessing definitions.
2. Quantify PTB-XL label overlap before freezing the binary tasks.
3. Preserve patient identity in splitting and uncertainty estimation.
4. Keep the diagnostic task, model, input construction, training procedure and evaluation set fixed when testing the representation effect.
5. Use an explicitly defined normalization formula rather than the generic term normalization.
6. Fit population-level preprocessing parameters on training data only.
7. Report AUROC and AUPRC together with positive-class prevalence.
8. Use a patient-level paired percentile bootstrap as the primary uncertainty procedure for paired performance differences.
9. Keep calibration secondary unless the research question changes.
10. Interpret the main finding as a representation effect under the defined evaluation rather than proof of clinical information loss.
11. Prespecify robustness analyses.
12. Record environment and provenance well enough for independent reproduction.

## Remaining decisions

The major scientific design is now frozen.

The remaining work is implementation verification. The frozen label rule, waveform representation, model structure, normalization and primary estimand now need unit tests, a train-and-validation smoke test and resource checks before the formal protocol and statistical analysis plan are written.

## References

1. von Elm E, Altman DG, Egger M, Pocock SJ, Gøtzsche PC, Vandenbroucke JP; STROBE Initiative. The Strengthening the Reporting of Observational Studies in Epidemiology (STROBE) statement: guidelines for reporting observational studies. Epidemiology. 2007;18(6):800-804. doi:10.1097/EDE.0b013e3181577654.
2. Swart E, Schmitt J. STandardized Reporting Of Secondary data Analyses, a recommendation. Z Evid Fortbild Qual Gesundhwes. 2014;108(9):511-516. doi:10.1016/j.zefq.2014.08.022.
3. Swart E, et al. A consensus German reporting standard for secondary data analyses, version 2 (STROSA-2). Gesundheitswesen. 2016;78(Suppl 1):e145-e160. doi:10.1055/s-0042-108647.
4. Swart E, Alibone M, Epping J, Grobe TG, Hoffmann F, Horenkamp-Sonntag D, Ihle P, March S, Rommel A, Stallmann C, Tesch F. Good Practice Secondary Data Analysis: Guidelines and Recommendations, Version 4. Gesundheitswesen. 2026. doi:10.1055/a-2904-1788.
5. Benchimol EI, Smeeth L, Guttmann A, Harron K, Moher D, Petersen I, et al. The REporting of studies Conducted using Observational Routinely-collected health Data (RECORD) statement. PLoS Med. 2015;12(10):e1001885. doi:10.1371/journal.pmed.1001885.
6. Watson HJ. A statistical analysis plan template for observational studies: promoting quality and rigor in research. J Stat Theory Pract. 2025;19:91. doi:10.1007/s42519-025-00504-9.
7. Thor M, Oh JH, Apte AP, Deasy JO. Registering study analysis plans before dissecting your data: updating and standardizing outcome modeling. Front Oncol. 2020;10:978. doi:10.3389/fonc.2020.00978.
8. Open Science Framework. Welcome to Registrations & Preregistrations. OSF Support. Available from: https://help.osf.io/article/330-welcome-to-registrations.
9. Wagner P, Strodthoff N, Bousseljot R-D, Samek W, Schaeffter T. PTB-XL, a large publicly available electrocardiography dataset (version 1.0.3). PhysioNet. 2022. doi:10.13026/kfzx-aw45.
10. Nayyab R, Waris A, Zaheer I, Khan MJ, Hazzazi F, Ijaz MA, et al. Enhancing ECG disease detection accuracy through deep learning models and P-QRS-T waveform features. PLoS One. 2025;20(6):e0325358. doi:10.1371/journal.pone.0325358.
11. Zeng L, Pan J, Lu Y, Pan X. Stabilizing extreme few-shot ECG classification via self-supervised contrastive pretraining. Ann Noninvasive Electrocardiol. 2026;31(3):e70188. doi:10.1111/anec.70188.
12. Rutter CM. Bootstrap estimation of diagnostic accuracy with patient-clustered data. Acad Radiol. 2000;7(6):413-419. doi:10.1016/S1076-6332(00)80381-5.
13. Liu W, Wu Z, Yuan Z. ACL-ECG: anatomy-aware contrastive learning for multi-lead electrocardiograms. Sensors (Basel). 2026;26(3):1080. doi:10.3390/s26031080.
14. Su H, Wang S, Wang H, Qiu K. An edge-cloud collaborative ECG-assisted diagnostic system leveraging cross-lead knowledge distillation and large language models. Sensors (Basel). 2026;26(12):3753. doi:10.3390/s26123753.
15. Bickmann L, Plagwitz L, Büscher A, Varghese J. Architecture-specific impact of preprocessing on machine learning models for ECG classification. Stud Health Technol Inform. 2026;336:529-533. doi:10.3233/SHTI260227.
16. Collins GS, Moons KGM, Dhiman P, Riley RD, Beam AL, Van Calster B, et al. TRIPOD+AI statement: updated guidance for reporting clinical prediction models that use regression or machine learning methods. BMJ. 2024;385:e078378. doi:10.1136/bmj-2023-078378.
17. Moons KGM, Damen JAA, Kaul T, et al. PROBAST+AI: an updated quality, risk of bias, and applicability assessment tool for prediction models using regression or artificial intelligence methods. BMJ. 2025;388:e082505. doi:10.1136/bmj-2024-082505.
18. DeLong ER, DeLong DM, Clarke-Pearson DL. Comparing the areas under two or more correlated receiver operating characteristic curves: a nonparametric approach. Biometrics. 1988;44(3):837-845. PMID:3203132.
19. Saito T, Rehmsmeier M. The precision-recall plot is more informative than the ROC plot when evaluating binary classifiers on imbalanced datasets. PLoS One. 2015;10(3):e0118432. doi:10.1371/journal.pone.0118432.
20. Stevens RJ, Poppe KK. Validation of clinical prediction models: what does the "calibration slope" really measure? J Clin Epidemiol. 2020;118:93-99. doi:10.1016/j.jclinepi.2019.09.016.
21. Sandve GK, Nekrutenko A, Taylor J, Hovig E. Ten simple rules for reproducible computational research. PLoS Comput Biol. 2013;9(10):e1003285. doi:10.1371/journal.pcbi.1003285.
22. Wilkinson MD, Dumontier M, Aalbersberg I, Appleton G, Axton M, Baak A, et al. The FAIR Guiding Principles for scientific data management and stewardship. Sci Data. 2016;3:160018. doi:10.1038/sdata.2016.18.
23. Barker M, Chue Hong NP, Katz DS, Lamprecht A-L, Martinez-Ortiz C, Psomopoulos F, et al. Introducing the FAIR Principles for research software. Sci Data. 2022;9:622. doi:10.1038/s41597-022-01710-x.
24. Clark J, Barton B, Albarqouni L, et al. Generative artificial intelligence use in evidence synthesis: a systematic review. Res Synth Methods. 2025;16:601-619. doi:10.1017/rsm.2025.16.
25. SPIRIT 2025. SPIRIT 2025 statement: updated guideline for protocols of randomised trials. BMJ. 2025;389:e081477. doi:10.1136/bmj-2024-081477.
26. Page MJ, McKenzie JE, Bossuyt PM, Boutron I, Hoffmann TC, Mulrow CD, et al. The PRISMA 2020 statement: an updated guideline for reporting systematic reviews. BMJ. 2021;372:n71. doi:10.1136/bmj.n71.
27. Rethlefsen ML, Kirtley S, Waffenschmidt S, Ayala AP, Moher D, Page MJ, Koffel JB, et al. PRISMA-S: an extension to the PRISMA statement for reporting literature searches in systematic reviews. Syst Rev. 2021;10(1):39. doi:10.1186/s13643-020-01542-z.
28. NeurIPS. Paper Checklist Guidelines. NeurIPS. Available from: https://neurips.cc/public/guides/PaperChecklist.
