# Data audit

I audited the uploaded PTB-XL version 1.0.3 metadata files before freezing the binary task definitions.

The audit covered `ptbxl_database.csv` and `scp_statements.csv`. No waveform files were used in this audit.

## Files checked

The uploaded copies contain

- `ptbxl_database.csv` with 21,799 rows and 28 columns
- `scp_statements.csv` with 71 SCP statement rows and the expected diagnostic mappings

Every row in `scp_codes` parsed successfully.

All 71 SCP codes appearing in the database are present in `scp_statements.csv`.

The local SHA-256 values of the uploaded copies are

`ptbxl_database.csv`
`7600de9c1b27d181d850b3c6038a35d7c3ddb6bb33b702e3a20252a6859d216b`

`scp_statements.csv`
`ad05b0b1fcae83bb1230755ad9cfc7c96f303feddc08a4a9ad5bdc9ca63bac8f`

These hashes identify the copies audited here. They are not being treated as independent proof of the official download because I did not obtain the official checksum file directly.

## Dataset structure

The uploaded metadata contains the expected 21,799 ECG records and 18,869 unique patients.

There are no duplicate `ecg_id` values and no duplicate waveform paths.

The ECG identifiers run from 1 to 21,837 with 38 gaps. This is expected for version 1.0.3 because the release notes document removal of duplicate records in earlier releases.

There are 2,111 patients with more than one ECG record. The maximum number of records for one patient is 10.

The patient-aware fold assignment is intact. No patient appears in more than one value of `strat_fold`.

The record counts per fold are

| Fold | Records |
| --- | ---: |
| 1 | 2,175 |
| 2 | 2,181 |
| 3 | 2,192 |
| 4 | 2,174 |
| 5 | 2,174 |
| 6 | 2,173 |
| 7 | 2,176 |
| 8 | 2,173 |
| 9 | 2,183 |
| 10 | 2,198 |

The patient counts per fold are also reasonably balanced. Most importantly, the same patient is never split across folds.

Folds 9 and 10 have `validated_by_human = True` for every record in this copy, which agrees with the official PTB-XL documentation that these folds contain at least one human evaluation.

## Waveform integrity audit

The metadata audit was followed by a targeted audit of representative waveform files from the uploaded PTB-XL v1.0.3 records100 data. The purpose was to verify that the actual files matched the representation documented by PhysioNet before the model input was selected.

The paired WFDB records I inspected had

- 12 signal channels
- 100 Hz sampling frequency
- 1,000 samples per channel for the 10-second recording
- 16-bit signal storage
- 1,000 digital units per mV, corresponding to 1 microvolt per least-significant bit
- the lead order I, II, III, AVR, AVL, AVF, V1, V2, V3, V4, V5, V6

The binary file dimensions matched 12 x 1,000 16-bit samples. The waveform data decoded cleanly into the expected matrix shape, and the header checksum values matched the decoded sample sums for the paired files checked. The observed signal values were in the expected millivolt scale for the sampled records.

No truncation or malformed header structure was found in the paired records inspected.

This was a study-specific integrity check, not a revalidation of every waveform in the PTB-XL release. The PTB-XL authors report technical validation of all records in the released dataset, so the purpose here was to verify that the files I will load locally conform to the documented representation.

An isolated waveform file supplied without its matching header was not used for header-dependent validation.

## Diagnostic superclass mapping

The 44 diagnostic SCP statements map into the five published diagnostic superclasses

- NORM
- MI
- STTC
- CD
- HYP

The remaining 27 SCP statements are form or rhythm statements and do not contribute to the diagnostic superclass mapping.

Using the published superclass mapping gives exactly the official version 1.0.3 counts

| Superclass | Records |
| --- | ---: |
| NORM | 9,514 |
| MI | 5,469 |
| STTC | 5,235 |
| CD | 4,898 |
| HYP | 2,649 |

The counts overlap because PTB-XL is multilabel.

There are 411 records with no diagnostic superclass at all. These have only non-diagnostic SCP statements and therefore cannot enter a binary task defined from the five diagnostic superclasses.

## HYP versus NORM

Using superclass presence without applying a likelihood threshold gives

- HYP present in 2,649 records
- NORM present in 9,514 records
- both HYP and NORM present in 5 records
- neither HYP nor NORM present in 9,641 records

The five records carrying both HYP and NORM are not a data-parsing error. They are present in the source annotations.

Among HYP-positive records that do not carry NORM, other diagnostic superclasses are common

- 817 also carry MI
- 1,509 also carry STTC
- 784 also carry CD

This means a future HYP analysis should not use language such as healthy versus hypertrophy unless an explicit mutually exclusive cohort is created. The scientifically cleaner description is a comparison between a PTB-XL HYP-labelled group and a PTB-XL NORM-labelled group under a defined label rule.

## MI versus NORM

Using superclass presence without applying a likelihood threshold gives

- MI present in 5,469 records
- NORM present in 9,514 records
- both MI and NORM present in 1 record
- neither MI nor NORM present in 6,817 records

Among MI-positive records that do not carry NORM, other diagnostic superclasses are common

- 817 also carry HYP
- 1,339 also carry STTC
- 1,793 also carry CD

Again, this is a multilabel phenotype comparison rather than a clean clinical case-control definition.

## Candidate binary label rule

The data audit and recent PTB-XL literature support a simple candidate rule for the primary binary tasks

**Positive**

The target superclass is present.

**Negative**

NORM is present and the target superclass is absent.

**Excluded**

Neither the target superclass nor NORM is present.

Under this rule

| Task | Positive | Negative | Excluded |
| --- | ---: | ---: | ---: |
| HYP vs NORM | 2,649 | 9,509 | 9,641 |
| MI vs NORM | 5,469 | 9,513 | 6,817 |

For HYP, the five HYP+NORM records would remain positive. For MI, the single MI+NORM record would remain positive.

This rule matches the structure of a recent PTB-XL binary MI benchmark in which MI was assigned when an MI-superclass code was present, the Healthy class required NORM with no MI code, and records containing neither were excluded. The authors reported a 14,982-record PTB-XL subset with 5,469 MI and 9,513 Healthy records.

For HYP, a recent PTB-XL+ LVH study used a 50% likelihood threshold and explicitly classified records with co-occurring LVH and NORM as LVH. That study obtained 2,258 LVH and 9,434 normal records before its feature analysis.

I therefore do not want to invent a new label convention without acknowledging these precedents.

## Likelihood scores

The values in `scp_codes` are statement likelihoods. The PTB-XL documentation describes the SCP dictionary as statement and likelihood pairs, with zero used when the likelihood is unknown.

I checked the effect of a 50% likelihood threshold as a sensitivity definition.

| Definition | HYP | NORM | MI |
| --- | ---: | ---: | ---: |
| Any mapped statement present | 2,649 | 9,514 | 5,469 |
| Maximum mapped likelihood >= 50% | 2,258 | 9,438 | 4,134 |

At the 50% threshold, four records carry both HYP and NORM at or above the threshold. There are no MI+NORM overlaps at or above 50%.

This is important because published PTB-XL studies do not all use the same certainty threshold. I will therefore keep likelihood thresholding as a prespecified sensitivity decision rather than silently mixing thresholded and unthresholded labels.

## Patient-level dependence

The primary scientific unit remains the ECG record.

However, 2,111 patients contribute multiple ECG records. Some patients also contribute records that receive different binary labels at different examinations.

Among the current candidate binary datasets, the number of patients with both positive and negative task records is

| Task | Patients with conflicting task labels |
| --- | ---: |
| HYP vs NORM | 49 |
| MI vs NORM | 129 |

These are not automatically errors. A patient can have different ECG findings at different recordings.

Because the same patient can contribute more than one evaluation record, the uncertainty analysis should respect patient clustering rather than treating every record as independent.

## Demographic and signal-quality metadata

Age and sex are complete in this copy.

The value 300 appears as age in 293 records. This is not a literal age of 300 years. PTB-XL uses values in the 300 range for ages above 89 for privacy protection, so these records should not be treated as biologically invalid. If age is used later, this encoding will need to be handled explicitly.

Height is missing for 14,825 records and weight is missing for 12,378 records. Because the primary question is about ECG signal representation, I do not plan to include height or weight as model inputs.

Signal-quality annotations are sparse and heterogeneous. For example, `static_noise` is populated for 3,260 records, `baseline_drift` for 1,598, `burst_noise` for 613, and `electrodes_problems` for 30. These fields should be treated as audit information until the actual waveform data have been inspected.

I will not exclude records solely from these metadata fields before checking the corresponding waveforms and writing an explicit signal-quality rule.

## What the audit changed

The data audit changed three parts of the study design.

First, the candidate binary tasks can now be defined from the actual v1.0.3 label structure instead of from superclass counts alone.

Second, I do not need to invent an elaborate mutually exclusive diagnostic cohort. A target-present versus NORM-present-without-target rule has direct precedent in recent PTB-XL binary work and keeps the study closer to the dataset's native multilabel structure.

Third, patient clustering is not a theoretical concern. It is present in the actual task cohorts, so the patient-level uncertainty plan should be implemented rather than left as a general methodological note.

## What the audit does not answer

This audit does not inspect the waveform values.

I have not yet checked

- waveform readability
- actual sample counts
- missing or corrupted waveform files
- channel ordering in the downloaded waveform files
- signal amplitude ranges
- baseline offsets
- whether any records require waveform-level exclusion
- the practical memory and compute cost of the 500 Hz and 100 Hz versions

Those checks require access to the waveform files.

## References

1. Wagner P, Strodthoff N, Bousseljot R-D, Samek W, Schaeffter T. PTB-XL, a large publicly available electrocardiography dataset (version 1.0.3). PhysioNet. 2022. doi:10.13026/kfzx-aw45.
2. Wagner P, Strodthoff N, Bousseljot R-D, Kreiseler D, Lunze FI, Samek W, et al. PTB-XL, a large publicly available electrocardiography dataset. Sci Data. 2020;7:154. doi:10.1038/s41597-020-0495-6.
3. Aydın F, Usta S, Kalaycıoğlu E, Aydemir O. Source-only transportability of engineered ECG features for healthy-versus-myocardial infarction classification. Diagnostics (Basel). 2026;16(13):2061. doi:10.3390/diagnostics16132061.
4. Zhou Q, Luo X, Du K. Interpretable detection of left ventricular hypertrophy using commercial ECG features and machine learning: a study based on the PTB-XL+ dataset. Front Cardiovasc Med. 2026;13:1825829. doi:10.3389/fcvm.2026.1825829.
5. Bickmann L, Plagwitz L, Büscher A, Varghese J. Architecture-specific impact of preprocessing on machine learning models for ECG classification. Stud Health Technol Inform. 2026;336:529-533. doi:10.3233/SHTI260227.
