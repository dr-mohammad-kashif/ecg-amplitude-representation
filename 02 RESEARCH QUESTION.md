# Research question

## What I am asking

Under a fixed direct-waveform model, does global record-wise z-score standardization change ECG classification performance differently for PTB-XL hypertrophy and myocardial infarction phenotypes?

## Why I am asking it

Normalization is easy to think of as a harmless preparation step. I am less interested in whether it is commonly used than in whether the assumption behind it holds for the task I am studying.

If amplitude contains information that is useful for one diagnosis and less useful for another, changing amplitude relationships could affect those tasks differently.

## Working hypothesis

My working hypothesis is that the change in AUROC under global record-wise z-score standardization will not be identical for the HYP and MI tasks.

This remains a hypothesis. The effect could be small, could be dominated by model variability, or could disappear under the prespecified sensitivity analyses.

## Prespecified tasks

I will study two binary PTB-XL phenotype comparisons

- HYP versus NORM-labelled records
- MI versus NORM-labelled records

The primary label definition uses a 50% or higher SCP diagnostic likelihood for both the target superclass and NORM. A target-plus-NORM record is assigned to the target class. A record with neither target nor NORM at that threshold is excluded.

The unthresholded superclass-presence rule is a prespecified label-definition sensitivity analysis.

I use NORM-labelled rather than healthy when describing the study population because the PTB-XL NORM label is an ECG phenotype, not an independent adjudication of overall patient health.

## What this will not show

I am not using this analysis to make claims about clinical utility or superiority, and it cannot establish a causal effect in patients. The conclusions will be limited to the PTB-XL data and the analysis I actually run.
