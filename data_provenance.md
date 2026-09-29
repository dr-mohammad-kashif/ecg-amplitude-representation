# Data provenance

I am using PTB-XL version 1.0.3 from PhysioNet.

The official dataset page currently lists version 1.0.3 as the latest released version. The version contains 21799 clinical 12-lead ECG records from 18869 patients. Each recording is 10 seconds long. The dataset contains 71 ECG statements and provides mappings into diagnostic classes and subclasses.

The waveform data are available at 500 Hz and in a 100 Hz version.

## Official access

Dataset page

https://physionet.org/content/ptb-xl/1.0.3/

Download page for the version 1.0.3 ZIP

https://physionet.org/content/ptb-xl/get-zip/1.0.3/

Version DOI

https://doi.org/10.13026/kfzx-aw45

The current study uses the 1.0.3 release because that is the latest listed version on the official PhysioNet record at the time of this research.

## Diagnostic labels

The PTB-XL documentation reports the following counts for the major diagnostic superclasses

- NORM 9514
- MI 5469
- STTC 5235
- CD 4898
- HYP 2649

These groups are not mutually exclusive because one record can have more than one diagnostic statement.

## Primary binary labels

The primary binary task rule uses a common SCP likelihood threshold of >=50% for both target and NORM labels. Target-plus-NORM is retained as target-positive and records reaching neither threshold are excluded. The unthresholded superclass-presence rule is retained as a prespecified sensitivity analysis. Full counts are recorded in data_audit.md.

## Folds

PTB-XL provides a patient-aware fold assignment for machine learning. Records from the same patient remain in the same fold.

The dataset documentation recommends folds 1 to 8 for training, fold 9 for validation and fold 10 for testing.

I will keep the exact fold use in the research log once I have frozen the final task definitions.

## Source files

The minimum metadata files needed for the initial data audit are

- `ptbxl_database.csv`
- `scp_statements.csv`

The primary waveform analysis uses the corresponding PTB-XL v1.0.3 records100 WFDB files. Each input record is 12 leads by 1,000 samples at 100 Hz.

## What I will record as the analysis develops

- the files I actually used
- the final inclusion and exclusion rules
- how I constructed the labels
- which folds were used
- how many records and patients remained after filtering
- any derived data I created locally
- the dataset checksum or other integrity check where practical

I am not committing the raw PTB-XL data to GitHub.
