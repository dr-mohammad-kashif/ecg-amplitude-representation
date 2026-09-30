# Reference Biomedical Analysis Protocol

Status: Draft for reference execution
Version: 0.1
Month: September 2026
Study phase: Preprotocol

## 1. Purpose

This document specifies the biomedical machine learning analysis that will serve as the reference computational target for the active LLM workflow study.

The reference analysis is not a clinical ground truth and is not treated as a superior scientific answer to every other valid analysis of PTB XL. It is an executable analysis defined by a locked protocol.

The purpose of the reference analysis is to provide a reproducible scientific object against which LLM workflow conditions can be evaluated.

Primary LLM collection cannot begin until the reference implementation has been executed, independently reproduced, compared, and used to establish the reference-agreement envelope.

## 2. Scientific question of the reference analysis

Under a fixed direct-waveform model, does global record-wise z-score standardization change ECG classification performance differently for PTB XL hypertrophy and myocardial infarction phenotype tasks?

For task $t$, define

$$
\Delta_t = AUROC_{normalized,t} - AUROC_{raw,t}.
$$

The primary cross-task contrast is

$$
\Delta_{HYP} - \Delta_{MI}.
$$

This estimand describes a representation-related performance contrast within the locked computational experiment. It is not interpreted as a causal treatment effect.

## 3. Reference analysis object

The reference object consists of five linked components.

### 3.1 Protocol

The scientific question, dataset version, cohort definitions, waveform representation, preprocessing, model, training configuration, evaluation measures, uncertainty procedure, sensitivity analyses, and interpretation boundaries.

### 3.2 Data and cohort state

The exact PTB XL version, selected metadata, label mapping, eligible records, patient identifiers, fold assignments, technical exclusions, and cohort manifests.

### 3.3 Implementation

The executable code implementing the locked protocol, together with the software environment and repository commit.

### 3.4 Execution

Model fitting, held-out predictions, performance metrics, calibration outputs, bootstrap outputs, runtime logs, and execution metadata.

### 3.5 Interpretation

The prespecified numerical comparison and its scientifically bounded interpretation.

A numerical output without the corresponding protocol and execution evidence does not constitute the complete reference object.

## 4. Dataset

The study uses PTB XL version 1.0.3 from PhysioNet. Version 1.0.3 contains 21,799 clinical 12-lead ECG records from 18,869 patients, with 10-second recordings and both 500 Hz and downsampled 100 Hz waveform releases.[1,2]

The primary analysis uses the 100 Hz records100 release.

The official PTB XL documentation provides patient identifiers, diagnostic statements and likelihoods, signal-quality metadata, and patient-aware recommended folds. Folds 1 through 8 are recommended for training, fold 9 for validation, and fold 10 for testing.[2]

Raw PTB XL waveform files are not stored in this repository.

The exact dataset version, local data location, file manifest, and integrity identifiers will be recorded in the reproducibility and data-provenance records.

## 5. Unit of analysis

The primary predictive unit is the ECG record.

Patient identity remains part of the data structure because some patients contribute multiple ECG records.

Patient clustering is accounted for in the uncertainty analysis.

The same scientific record may therefore contribute one prediction to each representation condition, while patient identity determines the resampling unit for the primary bootstrap.

## 6. Diagnostic tasks and label construction

Two binary phenotype tasks are prespecified:

1. HYP versus NORM
2. MI versus NORM

PTB XL contains multi-label diagnostic information. The primary binary labels use the SCP likelihood information rather than treating the diagnostic superclasses as mutually exclusive.[1,2]

For each task, using a common threshold of at least 50 percent:

| Record status | Definition |
|---|---|
| Target-positive | Target superclass likelihood >=50% |
| Target-negative | NORM likelihood >=50% and target likelihood <50% |
| Target plus NORM | Target-positive |
| Excluded | Neither target nor NORM reaches 50% |

The 50 percent threshold is an investigator-defined operational rule.

The current archived metadata audit reported the following pre-execution cohort counts:

| Task | Positive | Negative | Excluded |
|---|---:|---:|---:|
| HYP vs NORM | 2,258 | 9,434 | 10,107 |
| MI vs NORM | 4,134 | 9,438 | 8,227 |

These counts are retained as the current audit record, not as final reference execution outputs. They must be rederived from the frozen metadata during the reference run.

The sensitivity label construction uses unthresholded superclass presence.

NORM-labelled is used instead of healthy when describing the negative category because the PTB XL NORM annotation is an ECG phenotype label rather than an independent adjudication of overall patient health.

## 7. Data eligibility and technical exclusions

Before model fitting, each required waveform must pass the technical ingestion checks.

A record is technically ineligible for the primary reference analysis if the required waveform:

- is missing;
- cannot be read;
- does not provide 12 leads by 1,000 samples at the expected sampling frequency;
- has an unexpected sampling frequency;
- contains non-finite values;
- has a zero global standard deviation across the complete 12 lead by 1,000 sample record.

Technical exclusions are based on data integrity rather than model performance.

The same eligibility decision is applied to both raw and primary normalized representation conditions.

Each technical exclusion is recorded by ECG identifier and reported by task and fold.

The sensitivity per-lead normalization analysis has a separate technical condition. A record with a zero standard deviation in an individual lead is excluded from that sensitivity analysis only.

## 8. Waveform representation

The primary input is the PTB XL v1.0.3 records100 waveform.

Each record is represented as:

- 12 leads;
- 1,000 samples per lead;
- 100 Hz;
- 10 seconds;
- physical waveform values in mV after standard WFDB loading and conversion.

No independent resampling is performed.

The lead ordering must be retained exactly as provided by the dataset files.

No feature engineering, beat segmentation, morphology extraction, filtering, denoising, augmentation, clipping, or amplitude perturbation is included in the primary reference pipeline.

## 9. Representation conditions

### 9.1 Raw condition

The physical 100 Hz waveform is used without the study's normalization transformation.

### 9.2 Primary normalized condition

For every record, calculate

$$
z_{l,t} =
\frac{x_{l,t} - \mu_r}{\sigma_r}
$$

where $\mu_r$ and $\sigma_r$ are calculated over all 12 leads and all 1,000 samples in that record.

The standard deviation uses $ddof = 0$.

The transformation is record-local. No normalization parameters are estimated from other records.

The same record therefore defines its own centering and scaling parameters independently of the other observations in the cohort.

### 9.3 Normalization sensitivity

The prespecified normalization sensitivity uses a record-wise per-lead z-score.

For each lead $l$,

$$
z_{l,t} =
\frac{x_{l,t} - \mu_l}{\sigma_l},
$$

where $\mu_l$ and $\sigma_l$ are calculated from the 1,000 samples of that lead.

No other normalization procedure is introduced into the reference analysis.

## 10. Data splitting and leakage control

The official patient-aware PTB XL folds are used:

- folds 1 through 8 for training;
- fold 9 for validation;
- fold 10 for held-out testing.

All records from the same patient remain in one fold.[2]

No random record-level split is permitted.

The held-out test fold must not be used for:

- architecture selection;
- hyperparameter selection;
- checkpoint selection;
- threshold selection;
- preprocessing selection;
- any adaptive model-development decision.

The record-local primary normalization transformation does not estimate parameters from other records. Its statistics therefore do not cross the train-test boundary.

## 11. Reference classifier

The reference classifier is a compact one-dimensional convolutional neural network.

| Layer | Specification |
|---|---|
| 1 | Conv1D, 32 filters, kernel size 15, same padding, ReLU |
| 2 | MaxPool1D, pool size 2 |
| 3 | Dropout 0.10 |
| 4 | Conv1D, 64 filters, kernel size 11, same padding, ReLU |
| 5 | MaxPool1D, pool size 2 |
| 6 | Dropout 0.10 |
| 7 | Conv1D, 128 filters, kernel size 7, same padding, ReLU |
| 8 | MaxPool1D, pool size 2 |
| 9 | Dropout 0.10 |
| 10 | Global average pooling |
| 11 | One linear output logit |

No BatchNorm, LayerNorm, or other internal normalization layer is included.

The architecture is identical across raw and normalized representations and across the two primary phenotype tasks.

The architecture is an investigator-defined fixed component of the reference experiment. It is not selected through architecture search and is not presented as a competitive benchmark architecture.

## 12. Training configuration

The reference implementation uses PyTorch.

| Parameter | Primary specification |
|---|---|
| Loss | Binary cross-entropy with logits |
| Class weighting | None |
| Optimizer | AdamW |
| Learning rate | 0.001 |
| Weight decay | 0.0001 |
| Batch size | 128 |
| Maximum epochs | 50 |
| Early stopping patience | 8 |
| Checkpoint rule | Best validation AUROC |
| Primary seed | 1 |

The same initialization seed, data-ordering rules, optimizer settings, stopping rule, and checkpoint rule are used for the raw and normalized fits within each task.

No augmentation, mixup, random amplitude scaling, denoising, or adaptive preprocessing is permitted.

The held-out test set is never used for model selection.

The exact software versions, hardware information, deterministic settings, and repository commit must be recorded with the execution.

## 13. Primary evaluation data

Primary performance evaluation uses predictions generated on the held-out test fold.

The model outputs continuous prediction scores or probabilities sufficient to calculate threshold-independent discrimination measures and probability-based metrics.

The test data used for a representation condition are identical across the raw and normalized fits after the common technical-eligibility rules have been applied.

Any difference in record eligibility between representations must be logged and investigated before primary interpretation.

## 14. Primary performance metrics

For each task and representation, report:

- AUROC;
- average precision;
- positive-class prevalence;
- Brier score;
- calibration assessment.

AUROC is the primary discrimination statistic.

Average precision provides a complementary precision-recall measure.

The Brier score and calibration outputs assess probability quality rather than ranking discrimination.

The primary scientific contrast is calculated from the task-specific AUROCs:

$$
\Delta_{HYP} = AUROC_{normalized,HYP} - AUROC_{raw,HYP}
$$

$$
\Delta_{MI} = AUROC_{normalized,MI} - AUROC_{raw,MI}
$$

and

$$
\Delta_{HYP-MI} =
\Delta_{HYP} - \Delta_{MI}.
$$

The notation $\Delta_{HYP-MI}$ is used only as a label for the cross-task contrast. It does not imply a clinical comparison between hypertrophy and myocardial infarction.

## 15. Calibration

Calibration is reported descriptively using the fixed 0.10 probability bins retained from the archived analysis.

Empty bins are omitted from the display.

The fixed-bin calibration output is an investigator-defined descriptive component and is not presented as the only generally accepted calibration method.

Before reference protocol freeze, any decision to add calibration-in-the-large, calibration slope, or another prespecified measure must be made without reference to primary LLM results and recorded as a protocol change.

## 16. Primary uncertainty analysis

The primary uncertainty procedure is a patient-level paired percentile bootstrap with 5,000 resamples.

The patient, rather than the ECG record, is the resampling unit because some patients contribute multiple recordings.

For each bootstrap replicate:

1. Sample test-set patients with replacement.
2. Include all eligible test records belonging to sampled patients.
3. Preserve the raw and normalized prediction pairing within each record.
4. Compute task-specific AUROC values.
5. Compute the task-specific representation effects.
6. Compute the cross-task contrast when both task-level AUROCs are defined.

The same patient resample is used for the HYP and MI calculations.

The held-out HYP and MI test populations currently overlap at 939 patients before final technical waveform exclusions.

A bootstrap replicate containing only one class for a task is rejected and resampled because AUROC is undefined for a one-class sample.

The primary uncertainty output is the point estimate and 95% percentile bootstrap interval for the cross-task contrast.

Task-specific representation effects also receive 95% percentile bootstrap intervals.

The 5,000-resample count is an investigator-defined reproducibility and Monte Carlo precision choice. It is not presented as a universally required bootstrap count.

## 17. Secondary bootstrap analyses

The same patient-level paired bootstrap framework is used for:

- task-specific representation effects in AUROC;
- raw versus normalized average precision differences;
- raw versus normalized Brier score differences.

Calibration plots are descriptive and are not converted into the primary endpoint.

## 18. Sensitivity analyses

The following analyses are prespecified.

### 18.1 Normalization scope

Compare the primary record-wise global z-score with the record-wise per-lead z-score.

### 18.2 Label definition

Compare the primary >=50% likelihood rule with unthresholded superclass presence.

### 18.3 Random seed

Repeat the locked analysis using seeds 1, 2, and 3.

Sensitivity analyses must use the same protocol components other than the factor being examined.

No sensitivity analysis may replace the primary analysis.

## 19. Reference execution checks

Before the reference numerical outputs can be used by the LLM experiment, the following checks must pass.

### Check R0. Protocol implementation

The implementation matches the written protocol.

### Check R1. Reference execution

The primary implementation completes the locked analysis and produces all expected artifacts.

### Check R2. Repeat execution

The same implementation is rerun under the same locked environment and configuration to characterize execution repeatability.

### Check R3. Independent reproduction

An independently written implementation reconstructs the same scientific protocol without receiving the original implementation's source code or numerical outputs in advance.

### Check R4. Reference comparison

The original and independent implementations are compared at the structural and numerical levels.

### Check R5. Reference-agreement envelope

The natural numerical variation among compliant reference executions is characterized. For each scalar numerical outcome, the envelope is anchored to R1 and uses the larger absolute discrepancy between R1-R2 and R1-R3. R1-R2 represents repeatability of the locked implementation. R1-R3 represents agreement with the independent implementation. The R2-R3 discrepancy is recorded but does not widen the operational envelope because R1 is the locked reference.

### Check R6. Numerical agreement criteria freeze

Numerical agreement criteria are frozen before primary LLM results are collected. They are operational reproducibility criteria for this fixed task, data version, implementation environment, and evaluation procedure. They are not a formal statistical equivalence margin and are not generalized beyond the prespecified study setting.

Until Check R6 is complete, the reference numerical outputs are provisional and cannot be used as the final primary LLM acceptance threshold.

## 20. Reference agreement hierarchy

The reference comparison uses three levels.

### Structural agreement

Exact agreement is expected for properties such as:

- dataset version;
- task;
- label rule;
- cohort membership;
- patient fold assignment;
- waveform dimensions and units;
- preprocessing definition;
- model architecture;
- training configuration;
- bootstrap unit;
- number of bootstrap resamples.

### Numerical agreement

AUROC, average precision, Brier score, calibration outputs, task-specific delta values, and the cross-task contrast are compared using the prespecified reference-agreement criteria. Scalar outcomes use an envelope anchored to R1. Vector-valued calibration outputs are evaluated component-wise using the corresponding R1-R2 and R1-R3 empirical discrepancies.

No arbitrary fixed tolerance is imposed. The numerical agreement criteria are derived from compliant R1-R2 repeatability and R1-R3 independent-agreement observations and frozen at R6 before primary LLM outcomes are available.

### Interpretive agreement

The scientific report must correctly describe:

- the direction and magnitude of the primary contrast;
- the associated uncertainty;
- the role of normalization;
- the distinction between numerical results and protocol fidelity;
- the limits of inference.

Agreement of confidence-interval overlap is not itself a reference-agreement criterion.

## 21. Reference artifact manifest

The reference execution package must contain, at minimum:

| Artifact | Purpose |
|---|---|
| reference_manifest | Dataset, environment, protocol, software, seed, and execution identifiers |
| cohort_manifest | Record and patient eligibility, labels, folds, and exclusions |
| implementation_manifest | Model and training configuration |
| Generated source code | Exact executable implementation |
| Environment record | Python, PyTorch, NumPy, pandas, SciPy, scikit-learn, WFDB, hardware |
| Checkpoint files | Fitted models required for evaluation |
| Test predictions | Raw and normalized predictions for each task |
| Metric outputs | AUROC, average precision, prevalence, Brier, calibration |
| Bootstrap outputs | Resampling results and percentile intervals |
| Execution logs | Runtime and failure information |
| Independent reproduction record | Independent implementation and comparison |
| Reference-agreement record | Structural and numerical reference comparison |

The exact filenames may change when the repository implementation is built, but the artifact classes must be preserved.

## 22. Interpretation boundaries

The reference analysis does not establish:

- clinical utility;
- clinical superiority;
- patient benefit;
- causal biological information loss;
- prospective deployment performance;
- general performance across other ECG datasets;
- general LLM capability beyond this fixed computational target.

A change in AUROC does not by itself prove that the corresponding transformation destroyed clinically meaningful information.

The reference analysis establishes what the locked computational protocol produces under the defined execution conditions.

## 23. Scientific status of the protocol

The following are evidence-derived facts supporting the reference object:

1. PTB XL v1.0.3 is a defined public dataset with patient identifiers and patient-aware fold assignments.[1,2]
2. Direct waveform deep-learning analysis of PTB XL is an established computational setting.[3]
3. ECG preprocessing can affect performance in an architecture-dependent manner.[4]
4. Prediction-model reporting should distinguish discrimination, calibration, development procedures, and evaluation.[5]

The following are investigator-defined components:

1. HYP versus NORM and MI versus NORM as the two reference tasks.
2. The >=50% diagnostic likelihood threshold.
3. The global record-wise z-score as the primary representation comparison.
4. The per-lead z-score sensitivity.
5. The compact CNN architecture.
6. The training hyperparameters and seed set.
7. The primary cross-task estimand.
8. The patient-level paired percentile bootstrap with 5,000 resamples.
9. The reference-agreement procedure.
10. The interpretation boundaries.

The operational details are frozen only when this draft is converted into the final reference protocol after the reference implementation audit. Any change after that point must be recorded in the protocol change log.

## References

1. Wagner P, Strodthoff N, Bousseljot RD, Kreiseler D, Lunze FI, Samek W, et al. PTB-XL, a large publicly available electrocardiography dataset. Sci Data. 2020;7:154. doi:10.1038/s41597-020-0495-6.

2. PhysioNet. PTB-XL, a large publicly available electrocardiography dataset v1.0.3 [Internet]. Cambridge, MA: PhysioNet; 2022 [cited 2026 Sep 30]. doi:10.13026/kfzx-aw45. Available from: https://physionet.org/content/ptb-xl/1.0.3/

3. Strodthoff N, Wagner P, Schaeffter T, Samek W. Deep Learning for ECG Analysis: Benchmarks and Insights from PTB-XL. IEEE J Biomed Health Inform. 2021;25(5):1519-1528. doi:10.1109/JBHI.2020.3022989.

4. Bickmann L, Plagwitz L, Büscher A, Varghese J. Architecture-Specific Impact of Preprocessing on Machine Learning Models for ECG Classification. Stud Health Technol Inform. 2026;336:529-533. doi:10.3233/SHTI260227.

5. Collins GS, Moons KGM, Dhiman P, Riley RD, Beam AL, Van Calster B, et al. TRIPOD+AI statement: updated guidance for reporting clinical prediction models that use regression or machine learning methods. BMJ. 2024;385:e078378. doi:10.1136/bmj-2023-078378.

6. Papin JA, Mac Gabhann F, Sauro HM, Nickerson D, Rampadarath A. Improving reproducibility in computational biology research. PLoS Comput Biol. 2020;16(5):e1007881. doi:10.1371/journal.pcbi.1007881.

## Evidence status

References 1 through 5 were checked against the journal or official dataset record during the current protocol update. Reference 6 provides general computational reproducibility guidance.

This protocol deliberately contains no primary performance results. Reference values become eligible for use in the LLM experiment only after the reference execution checks and reference-agreement procedure described above have passed.
