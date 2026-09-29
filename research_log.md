# Research log

I am using this file to keep track of why I made decisions, not just what files I changed.

A useful entry for me answers four questions

1. What was I trying to figure out?
2. What did I do?
3. What did I learn?
4. What did I change?

## September 2026

I created the repository and wrote the first version of the study question and analysis plan.

I then did the first literature pass. The main thing that changed was the question itself.

I had originally been thinking more generally about whether normalization changes ECG model performance. The recent PTB-XL preprocessing work made that too broad. Preprocessing can already behave differently across model architectures, so I narrowed the study to a question I can test more cleanly.

I now want to see whether the same preprocessing choice can behave differently across diagnostic tasks while keeping the model and evaluation setup fixed.

I have not looked at the final model results yet. The next step is the data audit, where I will check the PTB-XL labels and freeze the task definitions before running the main comparison.

I decided not to move straight into model training.

Before I write the formal study protocol, I am checking the study design itself against current research guidance. I want to make sure the label construction, normalization rule, primary outcome, uncertainty method, leakage controls, robustness analysis and reporting plan are decisions I can defend from the literature.

I am also keeping a running work plan so that the study does not lose earlier decisions as the repository grows.

The public repository should stay focused on the actual study. I do not want to add documents or metadata that exist only to make the project look more advanced. New files should have a real research purpose.

The methods review then changed several design details.

Normalization is not one operation. Recent ECG papers use per-lead, per-record, global and other scaling choices, and a recent multi-lead study reported that per-lead normalization can obscure inter-lead amplitude relationships. I therefore need to define exactly what the transformation does before I call it a single normalization condition.

I also checked the leakage question more closely. If a transformation learns parameters from data, those parameters must come from the training portion before the held-out data are transformed. A record-local transformation is different because its parameters are derived from that record itself. I need to make that distinction explicit in the protocol.

Because the raw and normalized inputs come from the same held-out records, the final comparison will be paired. A correlated-ROC method such as DeLong is one candidate for comparing AUROC values, with a patient-level paired bootstrap as another option. I have not frozen the statistical test yet.

I also decided that information preservation needs a more precise definition. I am separating numerical signal preservation, preservation of clinically meaningful waveform structure, and task-relevant information available to the model. The protocol should not use the word information without making clear which of these is meant.

The methodological literature reconnaissance is now sufficient to narrow the next design decisions.

Secondary-data guidance reinforced that the protocol needs explicit data flow, unit of analysis, label construction, exclusions and analysis documentation. Because PTB-XL is multilabel, the HYP versus NORM and MI versus NORM tasks cannot be frozen without first quantifying overlaps in the actual v1.0.3 data.

The statistical literature also changed my uncertainty plan. PTB-XL can contain multiple records per patient, so treating every record as independent for confidence intervals would ignore within-patient clustering. A patient-level bootstrap is now the strongest candidate for the paired uncertainty analysis.

The current primary normalization candidate is a global record-wise z-score across retained leads and time points within each record. A per-lead record-wise z-score is the most useful current sensitivity candidate. I have not frozen either one.

The largest remaining methodological gap is the model input representation. Logistic regression and random forest were chosen as simple starting models, but I have not yet specified how the full multilead waveform enters them. That choice changes the experiment enough that it needs to be resolved before the formal protocol.

I created methods_literature_review.md to keep the detailed methodological evidence separate from the shorter decision-focused methods_review.md.

I am keeping the research record month-level rather than using exact day stamps. The publication years in the reference list are bibliographic information and are kept separately from the project log.
The PTB-XL metadata audit is now complete. The uploaded v1.0.3 files reproduce the published superclass counts and show that all patients remain within one stratified fold. The candidate HYP versus NORM and MI versus NORM cohorts are now defined from the actual multilabel structure rather than from assumed mutually exclusive classes.

The audit also showed that likelihood scores materially change cohort size, so I do not want to introduce a hidden certainty threshold. The main candidate uses superclass presence, while a 50 percent likelihood threshold is kept as a possible sensitivity definition. Recent PTB-XL work provides examples of both approaches.

The major scientific design is now frozen. I selected the native 100 Hz, 12-lead waveform after the targeted waveform integrity audit. The remaining work is implementation verification and formal protocol writing.


The waveform representation question is now substantially resolved. I audited representative PTB-XL v1.0.3 waveform files directly and confirmed that the paired records100 files decode as 12-lead, 1,000-sample, 100 Hz WFDB records with the documented signal scaling and lead structure. The binary dimensions and header checksums were consistent in the paired files checked.

The literature search also showed that version 1.0.3 has already been used in studies using 100 Hz, 10-second, 12-lead inputs, including recent neural-network work. Earlier PTB-XL benchmark implementations should still be read with their dataset version in mind because some used pre-1.0.3 releases.

I therefore selected the native 100 Hz, 12-lead waveform as the primary input representation. I am not adding an independent resampling step and I am no longer treating logistic regression or random forest as necessary baselines for the main representation question.

The primary normalized condition is now a global record-wise z-score across all leads and time points within each record. Per-lead record-wise z-score is the main sensitivity condition. The remaining major design work is the exact CNN training configuration and the statistical estimand, after which I can write the formal protocol and statistical analysis plan.


The frozen design was then implemented as a testable pipeline. The label rule, global and per-lead standardization functions, input-shape checks and compact CNN forward/backward pass were exercised with a synthetic label fixture and a supplied PTB-XL waveform record. The checks confirmed the expected transformations and the 12 by 1,000 model input. No held-out test performance was used.


The full design audit found one implementation-level issue in the unthresholded label-definition sensitivity. A numeric threshold of zero would incorrectly treat an absent superclass as present because the helper used zero as the default maximum likelihood. I replaced that shortcut with an explicit superclass-presence mode and added a unit test for the sensitivity rule.

The protocol, statistical analysis plan and preregistration draft are now aligned with the corrected implementation. The next work is environment verification, preregistration submission, full records100 ingestion and the primary analysis.
