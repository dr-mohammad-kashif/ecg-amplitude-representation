# Biomedical ML Workflow Fidelity

This repository contains a research program that moved from an initial ECG representation study to a controlled investigation of biomedical machine-learning workflows executed by general-purpose LLMs.

The active research object is workflow fidelity. The biomedical analysis is fixed while the analyst-facing workflow is varied and evaluated against an independently checked reference analysis.

The primary research question is:

> Under a locked biomedical machine-learning analysis, does changing the analyst-facing workflow from a fully specified monolithic workflow to a structured fresh-context workflow change end-to-end reference-faithful completion under the same zero-cost consumer access envelope?

## Active study

The current study is organized under [current-study](current-study/).

[STUDY PROTOCOL.md](current-study/STUDY%20PROTOCOL.md) is the authoritative integrated design.

The current workspace contains the literature and prior-art record, the fixed biomedical reference analysis, the LLM workflow protocol, the fidelity and statistical frameworks, the consumer eligibility specification, the interaction and resource records, and the frozen prompt package.

Primary LLM data collection has not begun.

## Research history

The original ECG amplitude representation study is preserved under [archive/ecg-amplitude-normalization](archive/ecg-amplitude-normalization/).

That study investigated whether record-wise ECG amplitude normalization changed classification performance differently across PTB-XL phenotype tasks. A deeper literature review found substantial overlap with existing ECG and preprocessing work, so it was archived rather than extended by successive marginal variations.

The archive remains part of the research record and supplies provenance for the biomedical testbed, data audit, preprocessing functions, model definition and several design decisions carried forward into the active study.

[RESEARCH LOG.md](RESEARCH%20LOG.md) records the transition between research phases.

## Research principles

Published evidence, evidence-supported inference, investigator-defined choices and computed results are kept distinct.

The active study does not claim novelty for LLM data analysis, biomedical agents, workflow verification, research reproduction, or individual workflow mechanisms. The research question concerns their controlled combination within one fixed biomedical machine-learning task and a defined consumer-access population.

The repository does not contain the PTB-XL data themselves.

## Citation

The repository includes [CITATION.cff](CITATION.cff) for citation metadata.
