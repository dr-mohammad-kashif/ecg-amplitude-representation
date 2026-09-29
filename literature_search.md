# Literature search

I am keeping a record of the searches that are feeding the study design. This is not being presented as a systematic review.

## September 2026

Purpose

I started a second literature pass focused on the research method itself before writing the formal protocol.

Main areas

- protocol and statistical analysis plan design
- secondary-data reporting
- prediction-model reporting
- risk of bias and applicability
- ECG normalization definitions
- preprocessing leakage
- paired comparison of model performance
- clustered uncertainty
- class imbalance and precision-recall evaluation
- calibration
- AI-assisted evidence synthesis
- research reproducibility and data stewardship

Sources and search routes

I used PubMed, BMJ, EQUATOR, OSF, PhysioNet, Nature Scientific Data, PLOS Computational Biology, Scientific Reports, Sensors and other peer-reviewed journal sources where the specific methodological question required them.

I used official PhysioNet documentation for version-specific dataset facts and official OSF documentation for preregistration workflow.

Example search themes

- secondary data analysis reporting STROSA
- secondary data reporting guideline health research
- statistical analysis plan observational study
- secondary data preregistration
- ECG normalization machine learning per lead per record
- PTB-XL preprocessing normalization
- ECG amplitude normalization inter-lead relationships
- preprocessing leakage machine learning medical data
- correlated ROC comparison DeLong
- patient clustered bootstrap diagnostic accuracy
- precision recall imbalanced classification
- calibration prediction model Brier score
- AI evidence synthesis human oversight
- reproducible computational research software versions

Key additions from this pass

### Secondary-data reporting

STROSA and STROSA-2 add secondary-data-specific reporting issues that are not fully captured by STROBE. A 2026 update, Good Practice Secondary Data Analysis version 4, provides a current secondary-data framework with recommendations on study population, analysis strategy, registration, data dictionaries, documentation and related issues.

### Normalization

The recent ECG literature uses materially different normalization scopes. A 2026 multi-lead ECG paper describes a global z-score across leads and time points within a record and contrasts it with per-lead normalization. This reinforced the need to define normalization mathematically rather than use the word as if it described one operation.

### Label overlap and dependence

PTB-XL diagnostic superclasses overlap, and the dataset includes multiple ECG records per patient. The study therefore needs an explicit label construction and patient-aware uncertainty strategy rather than treating every row as independent.

### Paired uncertainty

Raw and normalized predictions will be paired because they come from the same held-out records. DeLong is a candidate for AUROC comparison. A patient-level bootstrap is also a strong candidate because repeated records can belong to the same patient.

### Class imbalance

AUPRC should be reported alongside AUROC, with the positive-class prevalence stated explicitly.

### Calibration

Calibration is distinct from discrimination. A calibration plot and Brier score are currently the most straightforward secondary measures, with additional calibration summaries considered only if appropriate for the final model.

### Reproducibility

The literature supports recording software versions, inputs, parameters and the exact path by which results were produced. This strengthens the case for keeping the public repository as a real research record rather than only a code dump.

### AI-assisted research

A 2025 systematic review of generative AI in evidence synthesis found substantial errors and missed studies across several tasks. I therefore want AI to accelerate discovery and drafting while keeping source verification and scientific decisions under human control.

## Search boundary

I am not calling this a systematic review.

I have not applied a formal database-wide screening protocol, duplicate removal process, predefined inclusion and exclusion criteria or PRISMA flow.

The purpose of this search is methodological decision support for one computational study.

## Next

The remaining high-impact question is not another general literature search. It is how the PTB-XL waveform will be represented for the primary model and how the final label construction behaves in the actual v1.0.3 data.

Those decisions should be resolved through the data audit and then written into the protocol.

I am using publication years in the reference list for normal citation purposes. The project log itself uses only a month-level heading.


### Version-specific waveform search

I also checked whether the waveform representation needed to be rediscovered locally or whether the current PTB-XL literature already establishes it.

The official v1.0.3 documentation specifies the supplied 100 Hz records100 representation and its WFDB structure. Recent PTB-XL studies provide contemporary examples using 100 Hz, 10-second, 12-lead inputs, including a 2025 PTB-XL v1.0.3 MI study and a 2026 study using a 12 x 1000 neural-network input after conversion to 100 Hz.

This search changed the practical scope of the local waveform audit. I do not need to inspect the entire 3 GB release to establish the basic representation. I only need to verify that the actual files used locally conform to the documented format and then handle any record-level exclusions transparently if implementation reveals them.

The version comparison also matters. Several older PTB-XL papers and codebases used earlier releases, so their sample counts should not be used as evidence that they operated on the current 1.0.3 record set without checking the version.

The search therefore supports using the native 100 Hz waveform representation and keeping the local waveform audit focused on implementation integrity rather than duplicating the dataset authors' full technical validation.

### Version caveat from the recent waveform literature

One recent 2026 paper describes its source as PTB-XL version 1.0.3 but reports the older 21,837-record, 18,885-patient cohort. I will therefore use that paper for its preprocessing and 12 x 1000 input description, not as evidence for the current 1.0.3 record count. The official PhysioNet v1.0.3 release and studies that explicitly state their 1.0.3 use remain the sources for version-specific dataset facts.
