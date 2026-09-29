# Literature search

I am keeping a record of the searches that are feeding the study design. This is not being presented as a systematic review.

## 29 September 2026

Purpose

I started a second literature pass focused on the research method itself before writing the formal protocol.

Main areas

- protocol and statistical analysis plan design
- prediction-model reporting
- risk of bias and applicability
- observational and secondary-data reporting
- ECG normalization definitions
- preprocessing leakage
- paired comparison of model performance
- calibration
- AI-assisted evidence synthesis
- research reproducibility and data stewardship

Sources and search routes

I used PubMed, BMJ, EQUATOR, OSF, PhysioNet, scikit-learn documentation, Nature Scientific Data, and ACL Anthology.

Example search themes

- ECG normalization machine learning per lead per record
- PTB-XL preprocessing normalization leakage
- ECG amplitude information preservation
- TRIPOD+AI prediction model reporting
- PROBAST+AI risk of bias machine learning
- statistical analysis plan observational study
- secondary data analysis reporting guideline
- PRISMA-S literature search reporting
- OSF secondary data preregistration
- AI evidence synthesis accuracy human oversight
- AI generated text human writing style lexical clues

What changed because of this pass

Normalization is not a single operation. Recent ECG papers use different scopes and transformations, including per-lead, per-segment and global approaches.

A recent 2026 multi-lead paper made the effect of lead-wise normalization especially important by discussing the possible loss of relative inter-lead amplitude information.

I also confirmed that preprocessing transformations that learn parameters need to be fitted using the training data and then applied to held-out data.

Because the raw and normalized versions come from the same test records, the eventual comparison is paired. A correlated ROC comparison such as DeLong is one candidate for AUROC, but I have not frozen the final statistical method.

For the AI-assisted workflow, the current evidence argues for human oversight. A 2025 systematic review of GenAI in evidence synthesis found large miss and error rates for several tasks, especially literature searching. This means I should use AI to speed discovery and extraction while keeping source verification under human control.

Next

I will keep the search open until the remaining design questions in work_plan.md have enough evidence to support the study protocol.
