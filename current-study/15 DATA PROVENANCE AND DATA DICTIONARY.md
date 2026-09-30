# Data Provenance and Data Dictionary

## 1. Purpose

The data provenance record identifies where each analytical input comes from, how it is transformed, which version is used, and which derived objects are created during the study.

The data dictionary defines the variables and artifacts that are required to reconstruct the reference biomedical analysis and to audit whether an LLM workflow used the intended information.

The study separates source data from derived study data. A field appearing in an analysis manifest does not imply that the field was present in the source dataset. Derived variables must have an explicit derivation rule and source lineage.

This distinction is important for three reasons.

First, PTB-XL is a multi-label dataset with several layers of metadata and diagnostic information. The primary experiment uses only a defined subset of those data.[1,2]

Second, the LLM experiment evaluates scientific workflow fidelity. The evaluator must therefore be able to determine whether an incorrect result arose from an incorrect input, an incorrect transformation, an execution problem, or a later analysis error.

Third, version-specific provenance matters. The published PTB-XL paper describes the dataset release used in the original study, while the operational experiment is explicitly tied to PTB-XL version 1.0.3. The study must therefore use the selected version's files and manifests rather than silently combining counts or metadata from different releases.[1,2]

## 2. Provenance hierarchy

The study uses the following provenance chain:

```text
PTB-XL v1.0.3
       |
       +-- ptbxl_database.csv
       |
       +-- scp_statements.csv
       |
       +-- records100/
       |
       +-- records500/
       |
       v
Study input manifest
       |
       +-- cohort and label derivation
       +-- technical eligibility
       +-- patient-aware fold assignment
       v
Reference analysis inputs
       |
       +-- raw representation
       +-- normalized representation
       v
Model outputs
       |
       +-- held-out predictions
       +-- performance metrics
       +-- bootstrap outputs
       v
Fidelity and reproducibility records
```

Every derived object used in a primary evaluation must be traceable upward through this chain.

## 3. Source dataset identity

The reference analysis uses PTB-XL version 1.0.3 from PhysioNet.

The provider documentation identifies the principal metadata file as `ptbxl_database.csv`, with one row per ECG record identified by `ecg_id`. It provides the corresponding `patient_id`, waveform paths, diagnostic SCP codes with likelihoods, signal-related metadata, and the recommended patient-respecting fold assignment.[2]

The waveform data are provided in WFDB format at 500 Hz and as a downsampled 100 Hz release. The reference analysis uses the 100 Hz `records100/` release.[2]

The version-specific dataset identifier and access record must include:

| Field | Required record |
|---|---|
| Dataset | PTB-XL |
| Version | 1.0.3 |
| Provider | PhysioNet |
| Version DOI | 10.13026/kfzx-aw45 |
| Primary waveform release | records100 |
| Source metadata | ptbxl_database.csv |
| Diagnostic mapping | scp_statements.csv |
| File format | WFDB |
| License | Creative Commons Attribution 4.0 International Public License |
| Access month | Month-level record |
| Local manifest | Version-specific file/integrity manifest |

The dataset version is the operative identity for this experiment.

The original PTB-XL publication reports 21,837 records for the dataset release described in that paper, whereas the current version-specific experiment is tied to v1.0.3. The v1.0.3 provider release notes document subsequent removal of duplicate or triplicate records. Therefore the final data manifest must derive its counts from the actual v1.0.3 files rather than copying record counts from the publication.[1,2]

## 4. Source files

### 4.1 ptbxl_database.csv

This is the principal record-level metadata table.

The provider describes 28 columns covering identifiers, general recording metadata, ECG statements, signal metadata and recommended folds.[2]

The study does not require every source column to be passed into the analytical workflow.

The distinction is:

- source field: present in the provider data;
- retained field: copied into the study provenance layer;
- analytic field: used to derive a primary analysis variable;
- audit field: retained to check data integrity or exclusions;
- unused field: present in the source but excluded from the analytical package.

The full source table should remain available to the reference implementation through the permitted dataset access route. The study's analysis manifest should identify exactly which columns are read by each component.

### 4.2 scp_statements.csv

This file provides the definitions and mappings for SCP-ECG statements and their diagnostic organization.[2]

For the primary reference labels, the relevant mapping from individual SCP statements to diagnostic superclasses is part of the derivation chain.

The mapping must be versioned with the dataset rather than independently reconstructed from a secondary source.

### 4.3 records100/

These are the waveform files used by the primary reference analysis.

Each selected waveform must be read using a standards-compatible WFDB reader. The provider documentation describes the 100 Hz release as the convenience downsampled representation of the 500 Hz records.[2]

The primary analysis expects 12 leads and 1,000 samples per record.

### 4.4 records500/

The 500 Hz release is part of the source dataset but is not the primary analytical waveform.

It must not be silently substituted for the 100 Hz representation.

If the 500 Hz files are accessed for an audit or cross-check, that use must be recorded separately.

## 5. Source identifiers and linkage

The study uses two distinct identifiers.

| Variable | Role | Use in primary model |
|---|---|---|
| `ecg_id` | Unique ECG record identifier | No |
| `patient_id` | Patient identifier linking repeated ECGs | No |

`ecg_id` is used to link metadata, waveform files, cohort decisions, predictions and evaluation artifacts.

`patient_id` is used for patient-aware fold verification and patient-level bootstrap resampling.

Neither identifier is an input feature to the neural network.

Identifiers must remain in the provenance and audit layers even when they are removed from model tensors.

No identifier-derived feature, hashing trick, patient count feature, or record-order feature is permitted in the primary reference model.

## 6. Source diagnostic information

The primary diagnostic information is obtained from the PTB-XL SCP annotation structure.

The `scp_codes` field contains statement-to-likelihood information. The provider notes that an unknown likelihood is represented as zero in the source table.[2]

The study uses the prescribed superclass mapping and the target/NORM likelihood rule defined in the reference biomedical analysis protocol.[3]

For each primary phenotype task, the derivation must preserve:

- target superclass likelihood;
- NORM superclass likelihood;
- presence of the target superclass;
- presence of NORM;
- the resulting target-positive, target-negative or excluded status.

The raw `scp_codes` field is source information.

The task-specific target likelihood, NORM likelihood and binary status are derived analytical variables.

## 7. Primary label derivation

Two binary tasks are defined:

1. HYP versus NORM
2. MI versus NORM

For each task:

| Derived status | Operational definition |
|---|---|
| Target-positive | Target superclass likelihood >=50% |
| Target-negative | NORM likelihood >=50% and target likelihood <50% |
| Target plus NORM | Target-positive |
| Excluded | Neither target nor NORM reaches 50% |

The >=50% threshold is an investigator-defined operational rule documented in the reference protocol.[3]

The same rule must be applied independently of model output.

No post hoc relabeling is permitted because of class balance, model performance, or execution difficulty.

The unthresholded-superclass-presence construction is retained as a prespecified sensitivity analysis rather than being mixed into the primary label definition.

## 8. Label lineage

The label lineage for a primary record is:

```text
scp_codes
   |
   v
SCP statement mapping
   |
   v
diagnostic superclass likelihoods
   |
   +-- target likelihood
   +-- NORM likelihood
   |
   v
task-specific label rule
   |
   v
primary binary status
```

A derived label record should retain the source `ecg_id`, task, target likelihood, NORM likelihood, derived status and label-rule version.

This allows an evaluator to identify whether a classification discrepancy was introduced in source interpretation or later in model fitting.

## 9. Technical eligibility variables

Technical eligibility is determined before model fitting.

For each waveform, retain explicit indicators for:

- waveform present;
- waveform readable;
- expected lead count;
- expected sample count;
- expected sampling frequency;
- finite-value check;
- global standard deviation check;
- primary analytical eligibility.

A technical exclusion must have a recorded reason rather than a missing row.

The primary reference protocol excludes a record when the required waveform is missing, unreadable, has unexpected dimensions or sampling frequency, contains non-finite values, or has zero global standard deviation across the complete record.[3]

The exclusion decision is made without using model performance.

For the per-lead normalization sensitivity, lead-specific zero-variance conditions are recorded separately because they do not define primary-reference eligibility.[3]

## 10. Waveform data dictionary

| Variable or artifact | Type | Unit or shape | Source or derivation | Primary role |
|---|---|---|---|---|
| `ecg_id` | Integer identifier | One per ECG | PTB-XL metadata | Linkage |
| `patient_id` | Identifier | One per patient | PTB-XL metadata | Grouping and bootstrap |
| `filename_lr` | String | WFDB path | PTB-XL metadata | 100 Hz waveform lookup |
| Lead signal | Numeric array | 12 x 1,000 | WFDB waveform | Model input |
| Sampling frequency | Numeric | Hz | WFDB header | Eligibility audit |
| Lead count | Integer | Count | WFDB header | Eligibility audit |
| Sample count | Integer | Samples per lead | WFDB header | Eligibility audit |
| Signal unit | Numeric metadata | mV after standard loading/conversion | WFDB metadata and loader | Input definition |
| Global record mean | Float | mV | Derived from 12 x 1,000 values | Normalization parameter |
| Global record SD | Float | mV | Derived from 12 x 1,000 values, ddof=0 | Normalization parameter |
| Global z-scored waveform | Numeric array | 12 x 1,000 | Derived | Primary normalized input |
| Per-lead mean | Float | mV | Derived per lead | Sensitivity normalization |
| Per-lead SD | Float | mV | Derived per lead | Sensitivity normalization |
| Per-lead z-scored waveform | Numeric array | 12 x 1,000 | Derived | Sensitivity input |

The global mean and SD are record-local. No normalization parameter is learned from another record or from the training cohort.[3]

## 11. Metadata retained for provenance but not for modeling

The PTB-XL metadata include demographic, recording, signal-quality and validation-related fields.[2]

The primary reference model does not use these metadata fields as predictors.

Examples include:

- age;
- sex;
- height;
- weight;
- recording site;
- device;
- recording date;
- signal-quality annotations;
- diagnostic report text;
- validation fields.

These fields may remain in the source dataset and provenance archive, but their presence does not authorize their use in the neural-network input.

The final study package must state explicitly which metadata are exposed to each workflow condition.

This distinction prevents an LLM from silently constructing a tabular or multimodal shortcut that is scientifically different from the prescribed direct-waveform task.

## 12. Patient-aware split variables

The provider's `strat_fold` variable defines the recommended 10-fold split while respecting patient assignments.[2]

The primary reference split is:

| Fold set | Role |
|---|---|
| 1-8 | Training |
| 9 | Validation |
| 10 | Held-out test |

All records from a patient must remain in the same fold.

Derived split variables should include:

- `strat_fold`;
- `analysis_split`;
- `patient_split_check`.

The split must be verified independently of model training.

A record-level random split is not an acceptable substitute.

The held-out test fold must not influence model architecture selection, hyperparameter selection, checkpoint selection, preprocessing selection or any adaptive model-development decision.[3]

## 13. Derived model and evaluation data

After model execution, the following derived objects require provenance:

| Artifact | Required fields |
|---|---|
| Test prediction table | `ecg_id`, patient identifier linkage, task, representation, prediction score |
| Metric table | task, representation, metric, estimate |
| Bootstrap table | task, representation, resample ID, patient resample definition, estimate |
| Calibration table | task, representation, probability bin, observed event rate, predicted probability summary |
| Cohort manifest | record, patient, task, label status, fold, technical eligibility |
| Exclusion manifest | record, exclusion stage, exclusion reason |
| Environment manifest | environment ID, software versions, hardware summary |
| Execution manifest | run ID, source commit, dataset version, command, terminal state |

The prediction table must not replace the original source labels.

A derived result is always interpreted in relation to its source record and derivation pathway.

## 14. Missingness and unknown values

Missingness must be distinguished from a meaningful zero.

For source metadata, the original dataset coding conventions must be retained.

For diagnostic likelihoods, the provider documentation notes that an unknown likelihood in `scp_codes` is represented as zero.[2]

The analysis code must not silently reinterpret a source zero as a clinically confirmed absence unless that interpretation is explicitly part of the prespecified label derivation.

Variables that are not required for the primary task should not be imputed merely to make a complete table.

Any derived imputation introduced for a sensitivity analysis must have its own provenance and must not enter the primary reference pipeline unless prespecified.

## 15. Data transformations

Every transformation applied to analytical data must be classified as one of the following:

### Source-preserving transformation

A representation change that retains the underlying record identity and information, such as reading a WFDB signal into an in-memory numeric array.

### Analytical transformation

A transformation explicitly defined by the reference protocol, such as the record-wise z-score normalization.

### Exclusion transformation

A deterministic rule that removes a record or observation because it does not meet a stated technical or label criterion.

### Derived evaluation object

A result generated after model execution, such as a prediction, metric or bootstrap estimate.

No transformation may be introduced solely because an LLM or human operator believes it would improve performance.

## 16. Information exposure boundary for LLM workflows

The LLM workflow experiment must distinguish the full source dataset from the information deliberately exposed to a consumer LLM.

The primary study package should expose only the information required to execute the frozen scientific task and its specified audits.

The exact package contents are finalized in the LLM workflow protocol and prompt/context registry.[4,5]

The provenance system must record:

- which source files were exposed;
- which derived labels were exposed;
- which waveform files or paths were exposed;
- which reference implementation files were withheld;
- which numerical reference results were withheld;
- which prior LLM trajectories were withheld.

This prevents the data provenance record from being confused with the information actually available to an experimental workflow.

## 17. Leakage controls

The following are treated as data-leakage risks:

- placing test predictions or reference results in the study package before primary collection;
- exposing source code that directly reveals the target implementation when the condition is intended to generate the implementation;
- exposing post hoc labels derived using test results;
- using patient identifiers as model features;
- allowing records from one patient to cross the training and test folds;
- using held-out test performance to select preprocessing or hyperparameters;
- using information produced by another LLM run when that information is not part of the specified workflow condition.

The provenance registry should make it possible to determine whether any such exposure occurred.

A leakage finding is a scientific protocol failure, not merely a documentation defect.

## 18. Versioning and integrity

The following objects should carry version or integrity identifiers:

- PTB-XL dataset version;
- source metadata files;
- SCP mapping file;
- local waveform manifest;
- derived cohort manifest;
- label derivation code;
- analysis code;
- prompt and study-package versions;
- environment record;
- generated predictions;
- statistical outputs.

Cryptographic hashes may be recorded for large or important files where practical.

The hash identifies file integrity. It does not establish that the file contains scientifically correct content.

Dataset and artifact hashes should therefore be accompanied by descriptive provenance.

## 19. Data access and redistribution

The repository does not redistribute PTB-XL raw waveform files.

The provenance layer should instead provide:

- the dataset name and version;
- official source location;
- version DOI;
- license information;
- expected source-file structure;
- instructions for obtaining the permitted dataset;
- validation checks needed to confirm that the expected files are present.

The provider states that PTB-XL v1.0.3 is distributed under a Creative Commons Attribution 4.0 International Public License.[2]

Any derivative artifact released from the study must be reviewed separately for licensing and redistribution constraints.

## 20. Data-quality audit

Before reference execution, the data pipeline must verify:

1. the expected PTB-XL version is present;
2. the source metadata file is readable;
3. every selected `ecg_id` maps to the expected patient identifier;
4. the expected waveform path exists or has an explicit failure state;
5. the waveform header reports the expected dimensions and sampling frequency;
6. the diagnostic mapping file is available;
7. fold assignments are present;
8. no patient is assigned to multiple primary folds;
9. the primary label derivation produces only prespecified statuses;
10. technical exclusions have explicit reasons;
11. the resulting cohort manifest is reproducible.

These checks are data-provenance checks. They do not replace the later model and statistical fidelity checks.[6]

## 21. Version-specific count reconciliation

Source-level counts must always carry their dataset version.

The historical PTB-XL publication and the v1.0.3 source package should not be treated as interchangeable numerical descriptions.[1,2]

The final data manifest will therefore contain, as separate fields:

- published-source count, when cited for historical context;
- version-specific manifest count;
- task-specific analytic count before technical exclusions;
- task-specific analytic count after technical exclusions;
- held-out test count after technical exclusions.

Only the version-specific execution manifest is treated as the operative count for the current study.

No count is copied between versions without an explicit derivation.

## 22. Evidence basis

The source-data identity, file structure, field descriptions, sampling representations, fold assignment and licensing information are derived from the PTB-XL publication and official PhysioNet v1.0.3 documentation.[1,2]

The use of explicit provenance, qualified metadata and data lineage is supported by the FAIR data principles.[7]

RECORD and STROBE principles are relevant to transparent description of secondary observational data sources, but they do not govern this in-silico prediction experiment as a whole.[8]

The task-specific data dictionary, label derivation schema, leakage controls, information-exposure boundary, artifact manifest and version-reconciliation rules are investigator-defined components of the present study, aligned with the frozen biomedical reference protocol and reproducibility plan.[3,6]

No primary execution results are included.

## References

1. Wagner P, Strodthoff N, Bärs R, et al. PTB-XL, a large publicly available electrocardiography dataset. Sci Data. 2020;7:154. doi:10.1038/s41597-020-0495-6.
2. PhysioNet. PTB-XL, a large publicly available electrocardiography dataset v1.0.3. Version 1.0.3. PhysioNet; 2022. doi:10.13026/kfzx-aw45.
3. Reference Biomedical Analysis Protocol. current-study/08 REFERENCE BIOMEDICAL ANALYSIS PROTOCOL.md. Study repository; 2026.
4. LLM Workflow Experimental Protocol. current-study/09 LLM WORKFLOW EXPERIMENTAL PROTOCOL.md. Study repository; 2026.
5. Workflow Conditions and Ablation Plan. current-study/10 WORKFLOW CONDITIONS AND ABLATION PLAN.md. Study repository; 2026.
6. Reproducibility and Computational Environment. current-study/14 REPRODUCIBILITY AND COMPUTATIONAL ENVIRONMENT.md. Study repository; 2026.
7. Wilkinson MD, Dumontier M, Aalbersberg IJJ, et al. The FAIR Guiding Principles for scientific data management and stewardship. Sci Data. 2016;3:160018. doi:10.1038/sdata.2016.18.
8. Benchimol EI, Smeeth L, Guttmann A, et al. The REporting of studies Conducted using Observational Routinely-collected health Data (RECORD) statement. PLoS Med. 2015;12(10):e1001885. doi:10.1371/journal.pmed.1001885.
