# Data provenance

I am using PTB-XL version 1.0.3 from PhysioNet.

The version I am working with contains 21799 clinical 12-lead ECG records from 18869 patients. Each recording is 10 seconds long. The dataset contains 71 ECG statements and provides mappings into diagnostic classes and subclasses.

The waveform data are available at 500 Hz and in a 100 Hz version.

## Diagnostic labels

The PTB-XL documentation reports the following counts for the major diagnostic superclasses

- NORM 9514
- MI 5469
- STTC 5235
- CD 4898
- HYP 2649

These groups are not mutually exclusive because one record can have more than one diagnostic statement.

## Folds

PTB-XL provides a patient-aware fold assignment for machine learning. Records from the same patient remain in the same fold.

The dataset documentation recommends folds 1 to 8 for training, fold 9 for validation and fold 10 for testing.

I will keep the exact fold use in the research log once I have frozen the final task definitions.

## Source

The dataset paper is Wagner et al. 2020.

The specific PhysioNet version I am using is 1.0.3.

Version DOI 10.13026/kfzx-aw45

## What I will record as the analysis develops

- the date I accessed the dataset
- the files I actually used
- the final inclusion and exclusion rules
- how I constructed the labels
- which folds were used
- how many records and patients remained after filtering
- any derived data I created locally

I am not committing the raw PTB-XL data to GitHub.
