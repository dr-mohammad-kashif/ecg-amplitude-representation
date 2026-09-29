# Literature review

I began with the literature that could change the question itself, rather than trying to collect every paper on ECG machine learning. The review focuses on four areas that matter directly to this study: the PTB-XL dataset, ECG preprocessing, the clinical relevance of amplitude for hypertrophy, and recent evidence on preprocessing effects.

The citations in this document follow a numbered Vancouver-style system. References are listed at the end in the order in which they are first cited. This is a biomedical convention based on the National Library of Medicine and ICMJE recommendations rather than a KAUST-specific requirement. (1,2)

## PTB-XL as the study dataset

PTB-XL is a publicly available clinical 12-lead ECG dataset containing 21,799 records from 18,869 patients in version 1.0.3. Each recording is 10 seconds long, the dataset contains 71 ECG statements, and the labels are multilabel rather than mutually exclusive. The dataset provides both 500 Hz and 100 Hz waveform versions and a patient-aware fold assignment for machine-learning evaluation. (3,4)

This matters for my study because the unit I analyse is not just a row with one diagnosis attached to it. A record can contain several diagnostic statements, and a patient can have more than one ECG record. The final binary task definitions therefore need to be constructed explicitly from the dataset metadata rather than inferred from the superclass counts alone.

The PTB-XL benchmark paper also provides a reference point for how the dataset has been used for machine-learning evaluation. It reinforces the value of keeping the representation comparison controlled so that differences in performance can be attributed to the representation rather than to changes in the evaluation setup. (5)

## ECG preprocessing and normalization

Preprocessing is not a single standardised operation in ECG machine learning. Reviews of ECG preprocessing describe a wide range of signal conditioning, denoising, filtering and scaling procedures, which means that the word normalization is too broad to define my experiment on its own. (6,7)

Recent work has made this issue more specific for PTB-XL. Bickmann et al. compared multiple preprocessing choices across six deep-learning architectures and found that preprocessing effects depended on the architecture. Some convolutional models performed best with raw, unnormalized ECGs, while other architectures reacted differently to preprocessing. (8)

That finding changes the scope of my question. A broad question about whether normalization affects ECG classification is no longer sufficiently specific. The literature already shows that preprocessing can interact with model architecture. I therefore want to hold the model and evaluation procedure fixed and ask whether the same representation change behaves differently across diagnostic tasks.

A second methodological issue is the definition of the normalization operation itself. Recent multi-lead ECG work uses different approaches to scaling across leads and time points. Liu et al. describe a global z-score transformation across the retained signal and discuss the consequences of normalizing leads independently, while Su et al. provide another example in which absolute amplitude is deliberately retained in a multilead ECG system. These papers are useful as methodological examples, not as evidence that one normalization method is universally preferable. (9,10)

The current candidate for the primary representation comparison is therefore a global record-wise z-score, calculated across the retained leads and time points within each record. I am considering a record-wise per-lead z-score as a sensitivity condition because it removes lead-specific scale as well as overall record scale. Neither is yet a final protocol decision.

## Why amplitude matters for the hypertrophy task

The reason HYP remains a candidate task is not that hypertrophy can be reduced to amplitude.

The ISE/ISHNE expert consensus statement on ECG diagnosis of left ventricular hypertrophy describes the historical role of QRS voltage criteria and also emphasises their limitations and the influence of factors other than ventricular mass on ECG voltage. (11)

That gives the representation question a concrete clinical basis. If a preprocessing operation changes amplitude relationships before a model sees the ECG, it is reasonable to ask whether the consequences are the same for a hypertrophy-related phenotype as for a phenotype with a different diagnostic basis.

Recent PTB-XL+ work also shows that QRS amplitude and related ECG features can contribute to machine-learning detection of LVH. I use this as supporting evidence for keeping HYP as a candidate task, not as evidence that amplitude alone determines the label. (12)

## MI as a comparator task

I am retaining MI as a comparator phenotype because its clinical and electrocardiographic basis is not identical to hypertrophy.

Recent PTB-XL work on myocardial infarction and ST/T-change phenotypes used patient-disjoint evaluation and explicitly treated the target as an operational ECG phenotype derived from PTB-XL labels rather than as adjudicated active ischemia in individual patients. (13)

That distinction matters for interpretation. A result on the MI task will describe the effect of the representation on classification of the PTB-XL phenotype I define. It will not, by itself, establish that normalization changes the clinical diagnosis of myocardial infarction.

## What the literature currently supports

The first literature pass leaves me with a narrower question than I started with.

PTB-XL gives me a large, multilabel, patient-structured dataset with standardised ECG metadata and patient-aware folds. (3,4)

The preprocessing literature shows that normalization is not one operation and that preprocessing can interact with model architecture. (6,8-10)

Clinical literature gives a specific reason to think carefully about amplitude for hypertrophy, while recent PTB-XL work provides a contrasting diagnostic phenotype for MI. (11-13)

What is still open is whether a defined amplitude transformation has different consequences across diagnostic tasks when the model, input construction and evaluation procedure are held constant. That is the question I am taking into the data audit.

## References

1. International Committee of Medical Journal Editors. Recommendations for the conduct, reporting, editing, and publication of scholarly work in medical journals: preparing a manuscript for submission to a medical journal. ICMJE. Available from: https://www.icmje.org/recommendations/browse/manuscript-preparation/preparing-for-submission.html
2. Patrias K, Wendling DL, technical editor. Citing medicine: the NLM style guide for authors, editors, and publishers. 2nd ed. Bethesda (MD): National Library of Medicine (US); 2007-2015.
3. Wagner P, Strodthoff N, Bousseljot R-D, Samek W, Schaeffter T. PTB-XL, a large publicly available electrocardiography dataset (version 1.0.3). PhysioNet. 2022. doi:10.13026/kfzx-aw45.
4. Wagner P, Strodthoff N, Bousseljot R-D, Kreiseler D, Lunze FI, Samek W, et al. PTB-XL, a large publicly available electrocardiography dataset. Sci Data. 2020;7:154. doi:10.1038/s41597-020-0495-6.
5. Strodthoff N, Wagner P, Schaeffter T, Samek W. Deep learning for ECG analysis: benchmarks and insights from PTB-XL. IEEE J Biomed Health Inform. 2021;25(5):1519-1528. doi:10.1109/JBHI.2020.3022989.
6. Safdar MF, Nowak RM, Pałka P. Pre-processing techniques and artificial intelligence algorithms for electrocardiogram (ECG) signals analysis: a comprehensive review. Comput Biol Med. 2024;170:107908. doi:10.1016/j.compbiomed.2023.107908.
7. Jia Y, Pei H, Liang J, Zhou Y, Yang Y, Cui Y, et al. Preprocessing and denoising techniques for electrocardiography and magnetocardiography: a review. Bioengineering. 2024;11(11):1109. doi:10.3390/bioengineering11111109.
8. Bickmann L, Plagwitz L, Büscher A, Varghese J. Architecture-specific impact of preprocessing on machine learning models for ECG classification. Stud Health Technol Inform. 2026;336:529-533. doi:10.3233/SHTI260227.
9. Liu W, Wu Z, Yuan Z. ACL-ECG: anatomy-aware contrastive learning for multi-lead electrocardiograms. Sensors (Basel). 2026;26(3):1080. doi:10.3390/s26031080.
10. Su H, Wang S, Wang H, Qiu K. An edge-cloud collaborative ECG-assisted diagnostic system leveraging cross-lead knowledge distillation and large language models. Sensors (Basel). 2026;26(12):3753. doi:10.3390/s26123753.
11. Bacharova L, Chevalier P, Gorenek B, Jons C, Li Y-G, Locati ET, et al. ISE/ISHNE expert consensus statement on ECG diagnosis of left ventricular hypertrophy: the change of the paradigm. J Electrocardiol. 2023;81:85-93. doi:10.1016/j.jelectrocard.2023.08.005.
12. Zhou Q, Luo X, Du K. Interpretable detection of left ventricular hypertrophy using commercial ECG features and machine learning: a study based on the PTB-XL+ dataset. Front Cardiovasc Med. 2026;13:1825829. doi:10.3389/fcvm.2026.1825829.
13. Jin M, Tang X, Lei Y, et al. Machine-learning classification of myocardial infarction and ST/T-change ECG phenotypes across complementary evaluation settings. Sci Rep. 2026. doi:10.1038/s41598-026-68967-9.
