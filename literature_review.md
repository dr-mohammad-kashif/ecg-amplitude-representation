# Literature review

I began with the literature that could change the question itself, rather than trying to collect every paper on ECG machine learning. The review focuses on four areas that matter directly to this study: the PTB-XL dataset, ECG preprocessing, the clinical relevance of amplitude for hypertrophy, and recent evidence on preprocessing effects.

The detailed methodological evidence is kept separately in [methods_literature_review.md](methods_literature_review.md). I did this deliberately so that the scientific rationale for the study is not buried inside a long discussion of reporting standards and statistical methods.

The citations in this document use a numbered Vancouver-style system. References are listed at the end in the order in which they are first cited.

## PTB-XL as the study dataset

PTB-XL is a publicly available clinical 12-lead ECG dataset containing 21,799 records from 18,869 patients in version 1.0.3. Each recording is 10 seconds long, the dataset contains 71 ECG statements, and the labels are multilabel rather than mutually exclusive. The dataset provides both 500 Hz and 100 Hz waveform versions and a patient-aware fold assignment for machine-learning evaluation. (1,2)

This matters for my study because the unit I analyse is not just a row with one diagnosis attached to it. A record can contain several diagnostic statements, and a patient can have more than one ECG record. The final binary task definitions therefore need to be constructed explicitly from the dataset metadata rather than inferred from the superclass counts alone.

The PTB-XL benchmark paper also provides a reference point for how the dataset has been used for machine-learning evaluation. It reinforces the value of keeping the representation comparison controlled so that differences in performance can be attributed to the representation rather than to changes in the evaluation setup. (3)

## ECG preprocessing and normalization

Preprocessing is not a single standardised operation in ECG machine learning. Reviews of ECG preprocessing describe a wide range of signal conditioning, denoising, filtering and scaling procedures, which means that the word normalization is too broad to define my experiment on its own. (4,5)

Recent work has made this issue more specific for PTB-XL. Bickmann et al. compared multiple preprocessing choices across six deep-learning architectures and found that preprocessing effects depended on the architecture. Some convolutional models performed best with raw, unnormalized ECGs, while other architectures reacted differently to preprocessing. (6)

That finding changes the scope of my question. A broad question about whether normalization affects ECG classification is no longer sufficiently specific. The literature already shows that preprocessing can interact with model architecture. I therefore want to hold the model and evaluation procedure fixed and ask whether the same representation change behaves differently across diagnostic tasks.

A second methodological issue is the definition of the normalization operation itself. Recent multi-lead ECG work uses different approaches to scaling across leads and time points. Liu et al. describe a global z-score transformation across the retained signal and discuss the consequences of normalizing leads independently, while Su et al. provide another example in which absolute amplitude is deliberately retained in a multilead ECG system. These papers are useful as methodological examples, not as evidence that one normalization method is universally preferable. (7,8)

The current candidate for the primary representation comparison is therefore a global record-wise z-score, calculated across the retained leads and time points within each record. I am considering a record-wise per-lead z-score as a sensitivity condition because it removes lead-specific scale as well as overall record scale. Neither is yet a final protocol decision.

## Why amplitude matters for the hypertrophy task

The reason HYP remains a candidate task is not that hypertrophy can be reduced to amplitude.

The ISE/ISHNE expert consensus statement on ECG diagnosis of left ventricular hypertrophy describes the historical role of QRS voltage criteria and also emphasises their limitations and the influence of factors other than ventricular mass on ECG voltage. (9)

That gives the representation question a concrete clinical basis. If a preprocessing operation changes amplitude relationships before a model sees the ECG, it is reasonable to ask whether the consequences are the same for a hypertrophy-related phenotype as for a phenotype with a different diagnostic basis.

Recent PTB-XL+ work also shows that QRS amplitude and related ECG features can contribute to machine-learning detection of LVH. I use this as supporting evidence for keeping HYP as a candidate task, not as evidence that amplitude alone determines the label. (10)

## MI as a comparator task

I am retaining MI as a comparator phenotype because its clinical and electrocardiographic basis is not identical to hypertrophy.

Recent PTB-XL work on myocardial infarction and ST/T-change phenotypes used patient-disjoint evaluation and explicitly treated the target as an operational ECG phenotype derived from PTB-XL labels rather than as adjudicated active ischemia in individual patients. (11)

That distinction matters for interpretation. A result on the MI task will describe the effect of the representation on classification of the PTB-XL phenotype I define. It will not, by itself, establish that normalization changes the clinical diagnosis of myocardial infarction.

## Methodological foundation for the study

The study design is also informed by a separate body of methodological research. The detailed rationale is documented in [methods_literature_review.md](methods_literature_review.md).

The study is based on secondary data, so I am using secondary-data reporting guidance alongside broader observational reporting guidance. STROSA identified aspects of secondary-data research that require more explicit reporting than STROBE alone, while later guidance has expanded recommendations around registration, data dictionaries and documentation. (12-15)

Because the study develops and evaluates prediction models, TRIPOD+AI and PROBAST+AI provide relevant reporting and risk-of-bias frameworks. I will use them as design and reporting checks rather than claim blanket compliance with every item. (16,17)

The analysis plan is being written before the primary comparison because published methodological work supports prespecifying objectives, outcomes, variables and analytical methods, and OSF provides a dedicated Secondary Data Preregistration template that explicitly recommends making these decisions before viewing the data. Public registration makes later deviations visible rather than silently rewriting the plan. (18-20)

The reproducibility plan also draws on published guidance for computational research and on the FAIR principles, which apply not only to data but also to algorithms, tools and workflows. I have also incorporated FAIR4RS principles because this study will eventually contain research software as well as narrative research records. The NeurIPS checklist is an additional machine-learning transparency check focused on reproducibility, transparency, ethics and societal impact. (21-24)

I am not describing the literature search as a systematic review. PRISMA 2020 and PRISMA-S remain relevant as reference points for what would be required if the search were later converted into a systematic review, but they are not being claimed as reporting standards for the current exploratory search. (25,26)

This methodological layer does not replace the scientific literature review. It supports the way I will design, document and report the experiment.

## What the literature currently supports

The first literature pass leaves me with a narrower question than I started with.

PTB-XL gives me a large, multilabel, patient-structured dataset with standardised ECG metadata and patient-aware folds. (1-3)

The preprocessing literature shows that normalization is not one operation and that preprocessing can interact with model architecture. (4-8)

Clinical literature gives a specific reason to think carefully about amplitude for hypertrophy, while recent PTB-XL work provides a contrasting diagnostic phenotype for MI. (9-11)

The methodological literature gives me a framework for handling the study as secondary-data computational research, including explicit label construction, prespecified analysis, model-reporting checks, provenance and reproducibility. (12-24)

What is still open is whether a defined amplitude transformation has different consequences across diagnostic tasks when the model, input construction and evaluation procedure are held constant. That is the question I am taking into the data audit.

## References

1. Wagner P, Strodthoff N, Bousseljot R-D, Samek W, Schaeffter T. PTB-XL, a large publicly available electrocardiography dataset (version 1.0.3). PhysioNet. 2022. doi:10.13026/kfzx-aw45.
2. Wagner P, Strodthoff N, Bousseljot R-D, Kreiseler D, Lunze FI, Samek W, et al. PTB-XL, a large publicly available electrocardiography dataset. Sci Data. 2020;7:154. doi:10.1038/s41597-020-0495-6.
3. Strodthoff N, Wagner P, Schaeffter T, Samek W. Deep learning for ECG analysis: benchmarks and insights from PTB-XL. IEEE J Biomed Health Inform. 2021;25(5):1519-1528. doi:10.1109/JBHI.2020.3022989.
4. Safdar MF, Nowak RM, Pałka P. Pre-processing techniques and artificial intelligence algorithms for electrocardiogram (ECG) signals analysis: a comprehensive review. Comput Biol Med. 2024;170:107908. doi:10.1016/j.compbiomed.2023.107908.
5. Jia Y, Pei H, Liang J, Zhou Y, Yang Y, Cui Y, et al. Preprocessing and denoising techniques for electrocardiography and magnetocardiography: a review. Bioengineering. 2024;11(11):1109. doi:10.3390/bioengineering11111109.
6. Bickmann L, Plagwitz L, Büscher A, Varghese J. Architecture-specific impact of preprocessing on machine learning models for ECG classification. Stud Health Technol Inform. 2026;336:529-533. doi:10.3233/SHTI260227.
7. Liu W, Wu Z, Yuan Z. ACL-ECG: anatomy-aware contrastive learning for multi-lead electrocardiograms. Sensors (Basel). 2026;26(3):1080. doi:10.3390/s26031080.
8. Su H, Wang S, Wang H, Qiu K. An edge-cloud collaborative ECG-assisted diagnostic system leveraging cross-lead knowledge distillation and large language models. Sensors (Basel). 2026;26(12):3753. doi:10.3390/s26123753.
9. Bacharova L, Chevalier P, Gorenek B, Jons C, Li Y-G, Locati ET, et al. ISE/ISHNE expert consensus statement on ECG diagnosis of left ventricular hypertrophy: the change of the paradigm. J Electrocardiol. 2023;81:85-93. doi:10.1016/j.jelectrocard.2023.08.005.
10. Zhou Q, Luo X, Du K. Interpretable detection of left ventricular hypertrophy using commercial ECG features and machine learning: a study based on the PTB-XL+ dataset. Front Cardiovasc Med. 2026;13:1825829. doi:10.3389/fcvm.2026.1825829.
11. Jin M, Tang X, Lei Y, et al. Machine-learning classification of myocardial infarction and ST/T-change ECG phenotypes across complementary evaluation settings. Sci Rep. 2026 Sep 23. doi:10.1038/s41598-026-68967-9.
12. von Elm E, Altman DG, Egger M, Pocock SJ, Gøtzsche PC, Vandenbroucke JP; STROBE Initiative. The Strengthening the Reporting of Observational Studies in Epidemiology (STROBE) statement: guidelines for reporting observational studies. Epidemiology. 2007;18(6):800-804. doi:10.1097/EDE.0b013e3181577654.
13. Swart E, Schmitt J. STandardized Reporting Of Secondary data Analyses, a recommendation. Z Evid Fortbild Qual Gesundhwes. 2014;108(9):511-516. doi:10.1016/j.zefq.2014.08.022.
14. Swart E, et al. A consensus German reporting standard for secondary data analyses, version 2 (STROSA-2). Gesundheitswesen. 2016;78(Suppl 1):e145-e160. doi:10.1055/s-0042-108647.
15. Swart E, Alibone M, Epping J, Grobe TG, Hoffmann F, Horenkamp-Sonntag D, Ihle P, March S, Rommel A, Stallmann C, Tesch F. Good Practice Secondary Data Analysis: Guidelines and Recommendations, Version 4. Gesundheitswesen. 2026. doi:10.1055/a-2904-1788.
16. Collins GS, Moons KGM, Dhiman P, Riley RD, Beam AL, Van Calster B, et al. TRIPOD+AI statement: updated guidance for reporting clinical prediction models that use regression or machine learning methods. BMJ. 2024;385:e078378. doi:10.1136/bmj-2023-078378.
17. Moons KGM, Damen JAA, Kaul T, et al. PROBAST+AI: an updated quality, risk of bias, and applicability assessment tool for prediction models using regression or artificial intelligence methods. BMJ. 2025;388:e082505. doi:10.1136/bmj-2024-082505.
18. Watson HJ. A statistical analysis plan template for observational studies: promoting quality and rigor in research. J Stat Theory Pract. 2025;19:91. doi:10.1007/s42519-025-00504-9.
19. Thor M, Oh JH, Apte AP, Deasy JO. Registering study analysis plans before dissecting your data: updating and standardizing outcome modeling. Front Oncol. 2020;10:978. doi:10.3389/fonc.2020.00978.
20. Open Science Framework. Welcome to Registrations & Preregistrations. OSF Support. Available from: https://help.osf.io/article/330-welcome-to-registrations.
21. Sandve GK, Nekrutenko A, Taylor J, Hovig E. Ten simple rules for reproducible computational research. PLoS Comput Biol. 2013;9(10):e1003285. doi:10.1371/journal.pcbi.1003285.
22. Wilkinson MD, Dumontier M, Aalbersberg I, Appleton G, Axton M, Baak A, et al. The FAIR Guiding Principles for scientific data management and stewardship. Sci Data. 2016;3:160018. doi:10.1038/sdata.2016.18.
23. Barker M, Chue Hong NP, Katz DS, Lamprecht A-L, Martinez-Ortiz C, Psomopoulos F, et al. Introducing the FAIR Principles for research software. Sci Data. 2022;9:622. doi:10.1038/s41597-022-01710-x.
24. NeurIPS. Paper Checklist Guidelines. NeurIPS. Available from: https://neurips.cc/public/guides/PaperChecklist.
25. Page MJ, McKenzie JE, Bossuyt PM, Boutron I, Hoffmann TC, Mulrow CD, et al. The PRISMA 2020 statement: an updated guideline for reporting systematic reviews. BMJ. 2021;372:n71. doi:10.1136/bmj.n71.
26. Rethlefsen ML, Kirtley S, Waffenschmidt S, Ayala AP, Moher D, Page MJ, Koffel JB, et al. PRISMA-S: an extension to the PRISMA statement for reporting literature searches in systematic reviews. Syst Rev. 2021;10(1):39. doi:10.1186/s13643-020-01542-z.
