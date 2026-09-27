# Data provenance

## Dataset

PTB-XL version 1.0.3

The dataset will be obtained from the official PhysioNet distribution.

The version used for this study contains 21799 clinical 12-lead ECG records from 18869 patients. The recordings are 10 seconds long. The dataset includes 71 ECG statements with proposed diagnostic superclasses and subclasses.

The waveform data are provided at 500 Hz and in a 100 Hz version.

## Diagnostic superclasses

The version 1.0.3 documentation lists the following record counts for the major diagnostic superclasses

- NORM 9514
- MI 5469
- STTC 5235
- CD 4898
- HYP 2649

These counts are not mutually exclusive because a record can carry more than one diagnostic statement.

## Evaluation folds

PTB-XL provides recommended folds for machine learning evaluation. The fold assignment respects patient identity so that recordings from the same patient are not separated across folds.

The study will record the exact fold usage once the final task definitions are frozen.

## Source information

Dataset paper  
Wagner et al. 2020  
DOI 10.1038/s41597-020-0495-6

PhysioNet version 1.0.3  
DOI 10.13026/kfzx-aw45

## What will be recorded during analysis

- exact dataset version
- access date
- files used
- data license or access terms
- number of records retained
- patient count
- inclusion and exclusion rules
- label construction
- fold usage
- any derived data created locally

The raw PTB-XL data will not be committed to this repository.

Any derived data saved locally for analysis will be reproducible from the documented source and processing steps where the data terms permit.
