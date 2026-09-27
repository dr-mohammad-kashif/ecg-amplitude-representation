# Literature review

I am keeping the first literature review deliberately small. The aim is to establish the dataset, the normal PTB-XL benchmarking practice, the clinical reason for paying attention to ECG amplitude, and the current evidence on preprocessing. I do not want a long list of papers that does not change the study design.

## How sources were selected

The core sources are peer-reviewed journal articles, major clinical consensus work, and the primary PTB-XL dataset paper. A recent study that directly tests ECG preprocessing on PTB-XL is included because it is unusually close to the present question. A preprint is included only as supplemental context and is clearly marked as such.

I have not used blogs, vendor pages, generic tutorial sites, or papers with weak relevance just to increase the reference count.

The first working set contains nine sources. Seven are core sources. One is a supplemental preprint and one is an additional review used for context.

## 1. PTB-XL dataset

Wagner et al. 2020  
Scientific Data  
DOI 10.1038/s41597-020-0495-6

PTB-XL provides the dataset used for this study. The published dataset paper describes the original dataset and its patient-aware fold assignments. The version used for this project is version 1.0.3, documented separately in DATA_PROVENANCE.md.

This is the primary source for what the dataset is and how its recommended splits were constructed.

## 2. PTB-XL benchmarking

Strodthoff et al. 2021  
IEEE Journal of Biomedical and Health Informatics  
DOI 10.1109/JBHI.2020.3022989

This paper established early benchmark results for PTB-XL and compared several deep learning approaches across multiple tasks. It is useful here because it treats PTB-XL as a benchmark rather than as an arbitrary ECG collection and emphasizes evaluation quality, uncertainty and interpretability alongside predictive performance.

This is one of the main reasons the study uses the dataset's suggested evaluation structure rather than inventing a random split.

## 3. ECG preprocessing review

Safdar et al. 2024  
Computers in Biology and Medicine  
DOI 10.1016/j.compbiomed.2023.107908

This review covers ECG preprocessing and AI methods across a broad literature base. It is used for landscape context. It shows how varied preprocessing practice is across ECG machine learning and helps define what belongs in the preprocessing discussion without treating the review itself as evidence for a particular normalization effect.

## 4. Clinical grounding for amplitude and hypertrophy

Bacharova et al. 2023  
Annals of Noninvasive Electrocardiology  
DOI 10.1111/anec.12963

The international consensus statement explains that ECG diagnosis of left ventricular hypertrophy has traditionally relied heavily on QRS voltage criteria. It also emphasizes the limitations of voltage-only criteria and the number of factors that affect measured QRS amplitude.

This is important for the study because it gives the HYP task a clinical reason for taking amplitude changes seriously. It does not imply that amplitude alone defines hypertrophy.

## 5. Direct evidence on preprocessing and PTB-XL

Bickmann et al. 2026  
Studies in Health Technology and Informatics  
DOI 10.3233/SHTI260227

This is the most important recent paper for the present question. The authors tested signal cleaning, trend removal and normalization across six deep learning architectures on PTB-XL, with 24 preprocessing and model combinations repeated ten times. Their results showed that the effect of preprocessing depended strongly on architecture. Some convolutional networks performed best with raw, unnormalized ECGs, while other architectures responded differently.

This changes how the present study should be framed. It would be too broad to ask only whether normalization changes model performance. The present study therefore focuses on whether the effect also differs across diagnostic tasks.

## 6. Recent PTB-XL work on MI and ST/T phenotypes

Jin et al. 2026  
Scientific Reports  
DOI 10.1038/s41598-026-68967-9

This recent PTB-XL study uses patient-disjoint partitions to examine machine learning for MI and ST/T-change ECG phenotypes across several model families and evaluation settings. The authors are careful to describe the PTB-XL labels as operational ECG phenotypes rather than adjudicated active ischemia.

That distinction is useful for the present study. Any later result here will be interpreted as a finding about the dataset labels and the evaluation setup, not as proof of clinical diagnosis.

## 7. Recent evidence on amplitude related features in LVH

Interpretable detection of left ventricular hypertrophy using commercial ECG features and machine learning 2026
Frontiers in Cardiovascular Medicine
DOI 10.3389/fcvm.2026.1825829

This study used PTB-XL+ and evaluated several machine learning models using ECG features that included R-wave, S-wave, QRS amplitude and voltage-time measures. It is useful as a recent example that amplitude-related features remain part of computational LVH analysis.

This paper is supporting evidence for the HYP rationale rather than evidence about normalization itself.

## 8. Supplemental evidence on preprocessing practice

Salimi et al. 2025  
Preprint  
DOI 10.48550/arXiv.2311.04229

This work tests downsampling, normalization and filtering across several ECG datasets and classifiers. The authors report that min-max normalization was slightly detrimental overall and argue against applying preprocessing blindly.

I am treating this as supplemental evidence rather than a foundation for the study because it is a preprint rather than a peer-reviewed journal article. Its value here is that it independently raises the same methodological issue from a different set of datasets and models.

## Additional review used for preprocessing context

Jia et al. 2024  
Bioengineering  
DOI 10.3390/bioengineering11111109

This review focuses on preprocessing and denoising of ECG and related biosignals. It is useful for the broader preprocessing context but is not used to support a specific claim about amplitude normalization.

## What the literature currently says

The literature does not support treating ECG preprocessing as universally neutral or universally beneficial.

The PTB-XL dataset and benchmark papers establish a strong basis for reproducible evaluation.

The clinical literature gives a specific reason to care about amplitude in hypertrophy-related ECG interpretation.

Recent preprocessing work shows that the effect of normalization can depend on the model architecture.

The remaining question for this project is narrower. It is whether the same preprocessing choice can have different consequences across diagnostic tasks, even when the evaluation setup and model are held constant.

That is the question the first experiment will test.

## Sources that were considered but not promoted to the core set

I found several additional ECG machine learning papers that mainly reported predictive performance without changing the methodological question or adding a clear reason to include another task. I am not using them simply to make the reference list look larger.

The review will expand only when a new source changes the study design, interpretation, or a specific robustness check.
