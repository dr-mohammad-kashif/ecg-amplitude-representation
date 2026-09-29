# Methods review

I am using this document to collect methodological guidance that can change the design of the ECG study. It is a working document for the current design phase, not the final protocol.

## Why I am doing this first

The first literature pass answered questions about PTB-XL, ECG preprocessing, amplitude-related clinical reasoning, and recent preprocessing work.

I now need to examine the study process itself.

The main questions are about protocol structure, prediction-model evaluation, risk of bias, literature searching, reproducibility, preregistration, and AI-assisted research.

## Protocol guidance

SPIRIT 2025 is a protocol reporting framework for randomised trials. My study is not a randomised trial, so I am not claiming SPIRIT compliance. I am using it only as a source for protocol discipline and transparent planning where the ideas transfer to a secondary-data computational study.

## Prediction-model reporting

TRIPOD+AI is directly relevant when reporting studies that develop or evaluate prediction models using regression or machine learning.

PROBAST+AI is relevant as a self-audit for risk of bias and applicability. Its domains cover participants and data sources, predictors, outcomes, and analysis.

I will use relevant items from these frameworks in the final protocol and report without claiming that the whole study is a clinical prediction-model paper if that is not what the final design becomes.

## Observational-data reporting

STROBE is designed for observational studies such as cohort, case-control, and cross-sectional studies.

The PTB-XL data are existing clinical records rather than data collected by me. I will use STROBE as a reporting check where its items fit the data source and study description.

## Machine-learning research quality

The NeurIPS paper checklist is useful as a second machine-learning lens for reproducibility, transparency, ethics, and responsible reporting.

I will use it as a checklist for the computational work rather than claiming that this project is a NeurIPS submission.

## Literature search reporting

PRISMA and PRISMA-S are intended for systematic reviews and transparent literature searches.

I am not calling the current literature review systematic.

I will borrow the useful search-record ideas first. If the evidence search later becomes a true systematic review, I will follow the appropriate reporting framework.

## Preregistration

OSF supports preregistration and has a Secondary Data Preregistration template for studies using an existing dataset.

A preregistration is useful here because the study uses an existing dataset and I want the main label rules, hypotheses, analysis choices, outcomes, exclusions and planned deviations recorded before the primary result is known.

I will decide the exact preregistration contents after the protocol and data audit are complete.

## Data and workflow stewardship

The FAIR principles emphasize findability, accessibility, interoperability and reusability. They apply not only to datasets but also to algorithms, tools and workflows.

For this project, that means the repository should make the study plan, provenance, code and derived outputs understandable and traceable without publishing the raw PTB-XL data.

## What the recent normalization literature changes

The recent literature makes it clear that the word normalization is too broad on its own.

Studies on ECG machine learning use several approaches, including min-max scaling, z-score scaling, robust scaling, channel-wise transformations, and global transformations.

A recent 2026 multi-lead ECG study describes a global z-score transformation across leads and time points and notes that per-lead normalization can obscure inter-lead amplitude relationships. I am treating this as a methodological clue, not as a recommendation for my study.

Other recent work uses per-lead min-max normalization or per-segment z-score normalization. That variation is exactly why my protocol needs to define the normalization mathematically and specify whether the transformation is record-local, lead-local, or fitted from training data.

The 2026 PTB-XL architecture study also found that preprocessing effects depended on the model architecture. That means the first comparison should keep the model and evaluation procedure fixed while the representation changes.

## Leakage and preprocessing

The preprocessing literature and machine-learning documentation make an important distinction.

If a transformation learns parameters from data, those parameters should be learned from the training portion and then applied to held-out data.

A normalization rule that uses each record's own values is different from a rule that learns population-level parameters. I need to make that distinction explicit before the primary analysis.

For this reason, the protocol will state exactly where every normalization parameter comes from.

I will also split patients before any transformation that could learn information across records.

## Paired raw versus normalized evaluation

The raw and normalized versions will come from the same underlying ECG records.

That means the predictions on the held-out set are paired.

For AUROC, a comparison method for correlated ROC curves such as the DeLong approach is a candidate. A paired bootstrap is another candidate because it can estimate the distribution of the performance difference directly.

I am not freezing the statistical test yet. I want to check the assumptions and choose the simplest defensible method after the task definition and prediction setup are known.

The important point is that I should compare the two representations as paired evaluations of the same held-out records, not as two unrelated test samples.

## Calibration

TRIPOD+AI treats calibration as agreement between predicted probabilities and observed outcomes and recommends graphical calibration assessment alongside other performance measures.

The Brier score is one overall measure of the squared difference between predicted probabilities and observed outcomes.

I will keep calibration in the plan, but the final implementation will depend on the class balance and the probability outputs of the chosen models.

## Information preservation

The word information is still too broad for the final protocol.

I am separating at least three ideas

- numerical signal preservation
- preservation of clinically meaningful waveform structure
- preservation of task-relevant information for the model

These are not interchangeable.

The study may eventually use task performance as the main operational measure while treating direct signal-level measures as secondary evidence if they materially improve interpretation.

I need more literature before freezing this part.

## Primary estimand

A possible primary estimand is the difference in AUROC between the raw and normalized representations on the same held-out patient set for a defined diagnostic task.

I am treating this as a candidate until the outcome and statistical plan are frozen.

## Model choice

I am keeping logistic regression and random forest as the first models.

The reason is not that they are universally the best ECG models.

They give me relatively simple baselines that make it easier to interpret a representation comparison before introducing architecture-specific behavior.

The recent literature showing architecture-dependent preprocessing effects makes this control especially important.

## Robustness

A robustness check should answer a specific methodological concern.

Examples that may be appropriate include

- a second simple classifier
- a defensible alternative normalization definition
- a reasonable alternative label rule
- a paired bootstrap analysis
- a repeat across a second evaluation configuration

I do not want a large grid of variations that exists only to find a favorable result.

## AI-assisted research

Current evidence does not support treating AI as an unrestricted substitute for human scientific judgment.

For this study, AI can help with search-term generation, literature discovery, code drafts, debugging, documentation, and adversarial review.

Important scientific claims still need verification against the original paper, dataset documentation, or the project's own analysis output.

The AI workflow will remain documented in ai_notes.md, but I will keep that record factual and short.

## Reporting standards that may be used

- TRIPOD+AI for prediction-model reporting
- PROBAST+AI for risk of bias and applicability
- STROBE for relevant observational-data reporting
- SPIRIT 2025 for transferable protocol ideas
- PRISMA-S if the literature search becomes systematic
- NeurIPS checklist for machine-learning transparency and reproducibility
- FAIR principles for research objects, provenance and reuse

## Open questions that still need evidence

- What is the best operational definition of information preservation for this study?
- Which normalization rule makes the cleanest controlled comparison?
- Should the first normalization be record-wise, lead-wise, global, or another form?
- How should overlapping PTB-XL labels be handled?
- What should the primary estimand be?
- Which uncertainty procedure is appropriate for the paired raw versus normalized comparison?
- Which calibration analysis is suitable for the final class distributions?
- What is the minimum useful robustness analysis?
- Which reporting checklist items should become mandatory fields in the protocol?
- What parts of the AI-assisted workflow should be tested or audited rather than simply described?

## Current status

This document is not complete.

I am still gathering the evidence needed to lock the protocol.
