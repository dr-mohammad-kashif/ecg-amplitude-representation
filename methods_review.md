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

## AI-assisted research

Current evidence on AI text generation and AI-assisted research does not justify treating AI as an unrestricted substitute for human scientific judgment.

For this study, AI can help with search-term generation, literature discovery, code drafts, debugging, documentation, and adversarial review.

Important scientific claims still need verification against the original paper, dataset documentation, or the project's own analysis output.

## Open questions that still need evidence

- What is the best operational definition of information preservation for this study?
- Which normalization rule makes the cleanest controlled comparison?
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
