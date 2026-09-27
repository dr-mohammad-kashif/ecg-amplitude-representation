# Research log

This is a running record of decisions made during the study.

Each entry should answer four questions

1. What was the question or problem?
2. What did we do?
3. What did we observe?
4. What changed as a result?

## 27 September 2026

Created the repository and wrote the first version of the research question and analysis plan.

## 27 September 2026

Completed the first focused literature pass.

The main change from the initial idea is that the study should not ask only whether normalization changes performance. Recent PTB-XL work has already shown architecture-dependent effects from preprocessing. The question was therefore narrowed to whether the same preprocessing choice can have different consequences across diagnostic tasks when the model and evaluation setup are held constant.

The initial source set was kept deliberately small and weighted toward the primary dataset paper, established benchmarks, clinical consensus work, peer-reviewed preprocessing evidence, and one clearly labeled preprint used only as supplemental context.

The next step is the dataset audit. The candidate tasks will not be frozen until the label structure, class membership and exclusion rules have been checked directly in PTB-XL.
