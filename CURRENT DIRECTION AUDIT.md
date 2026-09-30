# Current direction audit

## Status

This document is a decision record for the research direction that emerged after the ECG study was archived.

It is not a protocol and it does not establish novelty.

The purpose is to record what the literature has already closed off and what question remains worth checking before a protocol is written.

## What I can no longer claim

I cannot claim that a study of whether LLMs can perform data science is new. Data-science benchmarks such as DataSciBench, DSBench and ScienceAgentBench already evaluate realistic analytical tasks and executable scientific workflows. PaperBench and RECLAIM address research and machine-learning reproduction. These establish a substantial benchmark literature around LLM-led analysis and reproduction.

I also cannot claim that biomedical LLM workflow evaluation is new. Biomni and BioMedAgent demonstrate biomedical analysis agents, while BiomniBench and related process-oriented evaluations assess biomedical workflows beyond final answers.

I cannot claim that clinical data-analysis reliability has not been tested. Wu et al. evaluated an LLM agent across research-question generation, statistical analysis planning, preprocessing and cohort logic, statistical execution and narrative reporting using a public clinical dataset and validated reference code. The study used repeated independent runs and compared different interaction modes.

I cannot claim that an LLM reproducing a conventional clinical analysis is new. Lagos-Beitz et al. compared ChatGPT Data Analyst with SPSS on the same clinical dataset using a predefined diagnostic-statistics workflow, with prompt refinement, repeated independent sessions and direct numerical concordance.

I cannot claim that an LLM can build a biomedical machine-learning model from clinical data is new. A 2024 Nature Communications study used ChatGPT Advanced Data Analysis to develop machine-learning models from real clinical datasets and compared them with manually developed models. A 2026 Nature Communications study on cell-free RNA biomarker discovery similarly evaluated LLM-constructed classifiers, held-out test data, repeated runs and fresh sessions.

## The remaining research question

The candidate research object is a controlled workflow experiment.

The underlying biomedical machine-learning task would be frozen first. The conventional reference pipeline would be deterministic and independently verified. The same raw data, labels, task definition, target outputs and scoring rules would be used across all LLM conditions.

The experimental factor would be how the analyst-facing workflow exposes the problem.

A possible set of regimes is

1. full-data single-context execution
2. staged data access with predefined information gates
3. staged access plus explicit verification gates
4. staged access plus verification and an independent audit pass

These are only candidate conditions. They are not yet frozen.

The central outcome would be scientific fidelity to the reference analysis, separated into data understanding, protocol fidelity, implementation fidelity, numerical/result fidelity and interpretation fidelity.

Secondary outcomes could include analyst intervention, wall-clock time, failure recovery and computational resource use, but these should not drive the scientific question.

## Why this may still be a useful gap

The studies above largely answer different questions.

Some benchmark broad data-science ability.

Some build autonomous biomedical agents.

Some compare LLM interaction modes or test a clinical analysis pipeline.

Some test whether a natural-language specification can reproduce predefined statistics.

Some allow the LLM to choose the machine-learning method rather than holding the scientific task and reference procedure fixed.

What is still worth testing is whether changing information exposure and verification within the same fixed biomedical ML task measurably changes scientific fidelity when using ordinary browser-accessible general-purpose LLMs.

That distinction is narrower than the earlier framing and makes workflow design itself the experimental variable.

## Major confounds that must be controlled

A future experiment should separate workflow effects from model and interface effects.

The selected models should be compared under the same workflow definitions, but platform-specific features such as code execution, file handling, context limits and hidden tool behaviour must be recorded rather than treated as invisible implementation details.

The reference pipeline must be frozen before LLM runs.

The held-out evaluation data should not be accessible before the stage at which the protocol permits them.

Human corrections during LLM runs must be logged. A human should not silently repair an analysis and then count the corrected output as an LLM success.

Repeated runs should begin from clean sessions where memory carry-over could affect results.

The scoring rubric must distinguish executable correctness from scientific correctness. A script that runs successfully can still implement the wrong cohort, wrong target, wrong preprocessing or wrong statistical estimand.

## Current decision

The direction survives as a candidate research object, but the novelty claim is still open.

I will not create the final protocol until the exact workflow factor, reference analysis and scoring system are specified and the remaining prior-art search does not identify the same experimental design.
