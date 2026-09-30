# Machine Learning Methods Review

Status: Working review
Version: 0.1
Date: 30 September 2026
Study phase: Preprotocol

## Scope

This review examines the methodological literature relevant to the fixed biomedical machine learning analysis used as the reference task for the active workflow study.

The purpose is not to select a competitive ECG architecture. The reference model is deliberately fixed so that workflow architecture, rather than model selection, remains the experimental object.

The review therefore focuses on direct waveform modelling, patient-level separation, preprocessing control, model specification, optimization, discrimination, precision-recall performance, calibration, uncertainty estimation, repeated patient structure, reproducibility, and sensitivity analysis.

Where the existing reference design contains an investigator-defined choice, that choice is identified as such. The literature is used to establish methodological considerations and known risks, not to retroactively claim that every numerical setting was prescribed by prior work.

## 1. Direct waveform modelling on PTB XL

PTB XL was introduced with benchmarking procedures intended to improve comparability of automated ECG analysis.[1] Strodthoff and colleagues evaluated several deep learning approaches on the dataset and found strong performance from convolutional architectures, including residual and inception-style networks. They also examined model uncertainty and interpretability, reinforcing the point that ECG model evaluation should extend beyond a single discrimination statistic.[2]

The active reference analysis uses a direct waveform input rather than a manually engineered feature table.

This choice has two methodological consequences.

First, the model receives the multichannel ECG representation directly. This avoids inserting a separate feature-engineering step between the biomedical measurement and the predictive model.

Second, the direct-waveform choice makes the model architecture part of the locked scientific protocol. A workflow that changes the representation before modelling has changed more than the intended workflow condition.

Earlier development considered logistic regression and random forest models. The problem with applying those models directly to the full waveform was not that classical models are inherently unsuitable. A 12-lead by 1,000-sample waveform would need to be flattened or otherwise transformed, introducing an additional representation decision. The reference design therefore moved to a compact one-dimensional CNN.

This transition is treated as a study-specific methodological decision. It is not presented as evidence that CNNs are universally preferable to classical models.

## 2. The reference CNN is a controlled probe, not an architecture search

The current reference architecture is:

- Conv1D, 32 filters, kernel size 15, ReLU
- max pooling by 2
- dropout 0.10
- Conv1D, 64 filters, kernel size 11, ReLU
- max pooling by 2
- dropout 0.10
- Conv1D, 128 filters, kernel size 7, ReLU
- max pooling by 2
- dropout 0.10
- global average pooling
- one linear output logit

The architecture contains no BatchNorm or LayerNorm.

These settings are investigator-defined. They were selected during the earlier ECG study to provide a compact direct-waveform model while avoiding a model-selection exercise.

The absence of normalization layers is also an investigator-defined control. It prevents the network from containing an additional learned or batch-dependent normalization mechanism that could complicate interpretation of the external waveform transformation being carried by the reference task.

The scientific requirement is therefore not that the architecture be optimal. It is that it be fixed before the LLM workflow experiment and reproduced exactly.

This distinction is important for the later workflow study. If an LLM changes the number of layers, kernel sizes, pooling operations, normalization layers, or output structure, that is a protocol violation even if the resulting classifier performs better.

## 3. Preprocessing is part of the model specification

Preprocessing is not a neutral implementation detail in ECG machine learning.

Bickmann and colleagues evaluated 24 combinations of signal cleaning, trend removal, and normalization across six deep learning architectures using PTB XL. They found substantial architecture-dependent sensitivity and reported that the convolutional models in their experiments performed best on raw, unnormalized ECGs.[3]

The result does not imply that raw ECG is universally optimal. It demonstrates that preprocessing choices interact with the model architecture and therefore should not be introduced or changed casually.

This is directly relevant to the active workflow experiment.

The reference waveform specification is fixed at the native PTB XL 100 Hz records100 representation, with 12 leads, 1,000 samples, 10 seconds, and physical millivolt units. No independent resampling is performed.

The primary transformation in the archived ECG analysis is a record-wise global z-score over all 12 leads and 1,000 samples, with the raw waveform retained as the comparator. The sensitivity analysis includes per-lead z-score normalization.

The current LLM workflow experiment is not intended to re-evaluate whether that normalization is clinically or algorithmically optimal. The transformation is part of the frozen scientific package that the workflow must reproduce.

The broader methodological point is that an LLM should not be allowed to insert filtering, denoising, resampling, clipping, augmentation, normalization, or feature extraction because those operations are conventional in another ECG pipeline.

A plausible preprocessing step can still constitute a scientific change.

## 4. Patient-level separation and leakage

PTB XL contains multiple recordings from some patients. The dataset provides patient-aware folds, with records from the same patient assigned to the same fold.[1]

The reference analysis follows the recommended split structure used in the archived protocol.

The planned allocation is:

- folds 1 through 8 for training
- fold 9 for validation
- fold 10 for testing

The patient identifier is not used as a predictive feature. It is used to preserve the independence of the evaluation boundary.

This is a central scientific control.

If records from one patient appear in both training and test data, the analysis no longer represents the same generalization problem. Repeated measurements can allow patient-specific characteristics to cross the nominal evaluation boundary, producing an estimate that is not comparable with the intended patient-aware reference analysis.

A workflow that creates a random record-level split therefore fails the protocol even when the class proportions look reasonable and the resulting AUROC is plausible.

Patient leakage is consequently treated as a structural protocol error rather than as a small numerical discrepancy.

## 5. Cohort definition and label construction

The PTB XL diagnostic system is multi-label, and the dataset supplies diagnostic statements with likelihood information.[1]

The reference analysis uses HYP versus NORM and MI versus NORM as two binary tasks.

The primary label construction from the archived protocol is:

1. the target superclass must reach a likelihood of at least 50 percent;
2. NORM must reach at least 50 percent for the negative category;
3. target plus NORM is retained as a target-positive record;
4. records for which neither relevant category reaches the threshold are excluded.

The unthresholded superclass-presence rule is retained as a sensitivity analysis.

The 50 percent threshold is an investigator-defined operational rule. It should not be interpreted as a clinical diagnostic threshold.

Similarly, NORM is a dataset-defined ECG classification label and must not be rewritten as a claim that the individual is clinically healthy.

The workflow experiment depends on keeping this label construction fixed. A system that substitutes any nonzero diagnostic likelihood, ignores likelihood values, changes the threshold, or converts the multi-label hierarchy into an unrelated binary rule has changed the scientific task.

## 6. Training procedure

The current reference training configuration is:

- binary cross-entropy with logits;
- AdamW optimizer;
- learning rate 0.001;
- weight decay 0.0001;
- batch size 128;
- maximum of 50 epochs;
- early stopping patience of 8 epochs;
- model checkpoint selected by validation AUROC;
- primary seed 1;
- sensitivity runs using seeds 1, 2, and 3;
- no class weighting.

These settings are investigator-defined components of the reference analysis.

The important methodological principle is separation between training and evaluation.

The held-out test set must not be used for architecture choice, hyperparameter tuning, checkpoint selection, threshold selection, or any other adaptive development decision. The validation set is the designated source for model selection under the current reference protocol.

TRIPOD+AI recommends explicit reporting of model development and evaluation procedures, including data partitioning, model specification, and performance assessment.[4] The reference analysis therefore treats the training configuration as part of the reproducible computational object rather than as an implementation detail that can be changed while preserving the study identity.

## 7. Random seeds and model repeatability

The primary reference run uses seed 1. Sensitivity analysis uses seeds 1, 2, and 3.

This does not turn three seeds into a statistically independent sample of biological observations. They are computational repetitions of the same data and model specification.

Seed sensitivity has a narrower purpose. It shows how much the reference output changes under the stochastic elements of model training.

This distinction becomes important when interpreting LLM runs. A change across LLM workflows should not be attributed to workflow architecture if the underlying reference analysis itself has large computational variability.

The reference-equivalence work must therefore be completed before the numerical tolerance used for the LLM experiment is frozen.

Seed values, software versions, hardware information where relevant, and training configuration should be recorded with the run outputs. Reproducible computational research guidance similarly emphasizes preservation of software, parameters, input data, and execution context rather than reporting only the final numerical result.[5]

## 8. Discrimination

AUROC is the primary discrimination statistic in the reference analysis.

For a binary classifier, AUROC summarizes ranking discrimination across decision thresholds. It is appropriate for comparing the ability of the model to rank positive and negative observations in the held-out test set.

AUROC should not be interpreted as calibration or as a measure of clinical usefulness. Modern prediction-model guidance distinguishes discrimination from calibration because a model can discriminate well while producing poorly calibrated probabilities.[4,6]

The reference analysis therefore retains AUROC as an important output but does not use it alone to determine whether an LLM reproduced the experiment.

For the two phenotype tasks, the archived primary estimand is:

$$
Delta_t = AUROC_{normalized,t} - AUROC_{raw,t}
$$

for phenotype $t$, with the primary cross-task contrast:

$$
Delta_{HYP} - Delta_{MI}
$$

This transforms two separate model comparisons into a task-specific contrast.

The same estimand must be preserved by every LLM workflow condition. Replacing it with a different comparison, a different ordering of the subtraction, or a different averaging procedure constitutes a statistical protocol change.

## 9. Average precision and class distribution

Average precision and the associated precision-recall representation are retained as secondary performance outputs.

Precision-recall analysis can be particularly informative when positive and negative classes are imbalanced because precision depends directly on the prevalence of positive predictions and the class distribution.[7]

This is relevant for PTB XL because the two binary cohorts are not expected to have identical prevalence, and the binary exclusion rules can change the composition of the held-out task.

A workflow that reports accuracy as its main secondary metric, or that replaces average precision with an arbitrary threshold-based F1 score, may still produce a reasonable classifier but would no longer reproduce the reference evaluation.

Average precision is therefore part of the fixed analysis output rather than a model-selection target.

## 10. Calibration and probability quality

The reference analysis also retains Brier score and calibration assessment.

The Brier score measures the mean squared difference between predicted probabilities and observed binary outcomes and therefore evaluates a different aspect of performance from ranking discrimination.[6]

Calibration is concerned with agreement between predicted probabilities and observed outcome frequencies. Current clinical prediction guidance recommends evaluating calibration rather than assuming that good discrimination implies well-calibrated probabilities. Calibration plots and measures such as calibration-in-the-large and calibration slope provide complementary information.[6]

The archived ECG analysis uses fixed 0.10 probability bins for its calibration display. That rule is an investigator-defined descriptive choice.

This creates a methodological point that should remain open for the formal reference protocol. Grouped calibration plots can be affected by the number and definition of bins. Current prediction-model guidance recommends flexible calibration curves and quantitative measures such as calibration-in-the-large and calibration slope rather than relying on a grouped plot alone.[6]

The existing 0.10-bin output should therefore not be silently treated as the complete calibration assessment. Before the reference protocol is frozen, the study should decide whether to retain the fixed-bin display as the prespecified output, supplement it with calibration-in-the-large and slope, or both.

Any such change must occur before LLM results are inspected.

## 11. Patient-level uncertainty estimation

The candidate reference analysis uses a patient-level paired percentile bootstrap with 5,000 resamples.

The choice of patient-level resampling follows from the data structure rather than treating every ECG record as an independent biological sampling unit. Cluster bootstrap methods preserve observations within the sampled cluster and are used to account for correlation among repeated observations from the same unit.[8,9]

Rutter specifically examined bootstrap estimation of diagnostic accuracy with patient-clustered data and found that bootstrap methods can provide useful confidence intervals for diagnostic accuracy measures when outcomes are correlated within patient.[8]

The archived design therefore resamples patient identifiers rather than individual ECG records.

The same patient resample is carried through the paired HYP and MI analysis structure so that the cross-task contrast is generated from a common resampling unit.

The current implementation uses percentile intervals with 5,000 bootstrap repetitions. The number of repetitions is an investigator-defined precision and reproducibility choice, not a literature-prescribed requirement.

One-class bootstrap draws are rejected because AUROC is undefined when a resampled task contains only one class. The rejection rule is part of the statistical implementation and must be fixed before LLM execution.

The workflow evaluation must distinguish a correct patient-level bootstrap from an ordinary record-level bootstrap even if both produce numerically similar intervals in a particular run.

## 12. Reference equivalence and numerical tolerances

The LLM experiment requires numerical agreement criteria, but the review does not support choosing an arbitrary universal tolerance.

For example, a rule such as AUROC within plus or minus 0.02 would be a design choice unless justified by the reference-analysis variability and the purpose of the study.

The reference-analysis chain therefore precedes primary LLM collection.

The planned sequence is:

1. freeze the reference protocol;
2. verify the original implementation;
3. execute the reference analysis;
4. independently reimplement the locked analysis;
5. compare the implementations;
6. establish the empirical reference equivalence envelope;
7. freeze the numerical agreement criteria;
8. begin primary LLM collection.

The reference envelope should characterize differences in implementation outputs arising without changing the scientific protocol. The exact tolerance construction remains an open statistical decision.

Confidence-interval overlap is not proposed as an equivalence rule. Agreement should instead be judged using prespecified structural and numerical criteria defined before the primary LLM results are seen.

## 13. Structural versus numerical correctness

The machine learning literature supports evaluating several dimensions of prediction-model quality rather than reducing performance to one number.[4,6]

For the workflow study, this leads to a distinction between structural correctness and numerical agreement.

Structural properties include:

- dataset version;
- cohort membership;
- label definition;
- patient fold assignment;
- waveform dimensions and units;
- preprocessing operation;
- model architecture;
- optimizer and hyperparameters;
- checkpoint rule;
- seed;
- metric definitions;
- bootstrap unit and configuration.

These can often be checked directly from manifests, source code, execution logs, or deterministic validators.

Numerical properties include:

- AUROC;
- average precision;
- Brier score;
- calibration outputs;
- delta values;
- the cross-task primary contrast;
- bootstrap interval limits.

A run can therefore be numerically close to the reference while being scientifically incorrect.

For example, using a record-level split instead of patient-level folds could yield an AUROC close to the reference by chance. That would not constitute successful reproduction.

This distinction is central to the later scientific fidelity framework.

## 14. Reproducibility of the computational reference

The reference analysis must be reproducible as an executable object.

The minimum record should include:

- dataset name and version;
- data file manifest;
- label specification;
- fold assignments;
- waveform shape and units;
- preprocessing definition;
- model architecture;
- optimizer and hyperparameters;
- random seed;
- software versions;
- hardware information where it can affect execution;
- generated code;
- model checkpoints;
- predictions;
- metrics;
- bootstrap configuration;
- execution logs.

Reproducible computational biology guidance emphasizes that reproducibility requires more than sharing a final script. Inputs, software, parameters, and the sequence of computational operations must be recoverable.[5]

This becomes particularly important in the LLM experiment because the reference analysis is also the object against which workflow fidelity is measured.

## 15. Sensitivity analyses

The archived reference design includes several planned sensitivity analyses.

### Seed sensitivity

Seeds 1, 2, and 3 are used to assess computational variation under the same analysis.

### Normalization sensitivity

The primary comparison uses global record-wise z-score normalization, with per-lead z-score normalization as a sensitivity analysis.

### Label sensitivity

The primary label rule uses the 50 percent likelihood threshold. Unthresholded superclass presence is retained as a sensitivity analysis.

These sensitivity analyses are not interchangeable with the primary analysis.

They are designed to examine whether conclusions about the fixed reference task are dependent on a specific methodological choice.

The LLM workflow study must not permit individual systems to select among these sensitivity definitions. The reference protocol must state which analysis is primary and which outputs are secondary.

## 16. Failed or rejected methodological approaches

The development record preserves several approaches that were considered and then rejected.

Logistic regression and random forest were initially considered as simple classifiers. They were not retained because direct application to the full waveform would require flattening or feature engineering, creating an additional representation choice that would weaken the control of the waveform experiment.

DeLong-style correlated ROC inference was considered for uncertainty estimation. The reference design instead moved to patient-level paired bootstrap because the dataset contains multiple records per patient and the primary estimand spans two related tasks.

These decisions do not imply that the rejected methods are invalid. They were rejected because they did not match the specific structure and estimand of the reference experiment.

Retaining the rejected alternatives in the research record is important because it shows that the final method was selected through explicit methodological reasoning rather than presented as inevitable.

## 17. Methodological risks that the LLM workflow can introduce

The machine learning reference defines several failure modes that can be detected independently of final performance.

### Data and cohort errors

A workflow may use the wrong dataset version, wrong files, wrong folds, or wrong cohort.

### Label errors

A workflow may misinterpret the PTB XL hierarchy, likelihood values, positive and negative definitions, or exclusion rules.

### Representation errors

A workflow may change sampling frequency, lead order, waveform units, signal length, or preprocessing.

### Model errors

A workflow may change layers, filter counts, kernel sizes, pooling, dropout, activation, normalization layers, or output structure.

### Training errors

A workflow may change loss, optimizer, learning rate, weight decay, batch size, early stopping, checkpoint selection, class weighting, or seed handling.

### Evaluation errors

A workflow may use the wrong test set, calculate the wrong metric, alter the estimand, or evaluate with thresholded predictions when continuous scores are required.

### Statistical errors

A workflow may resample records rather than patients, use the wrong bootstrap unit, change the interval construction, or fail to handle one-class bootstrap samples.

### Interpretation errors

A workflow may treat a dataset-defined label as clinical ground truth, interpret an AUROC change as causal biological information loss, or report a secondary finding as the primary result.

These categories provide the methodological basis for the later fidelity gates and error taxonomy.

## 18. Implications for the workflow experiment

The machine learning literature supports a clear separation between the biomedical task and the workflow used to execute it.

The reference task must remain fixed.

The LLM workflow can vary.

The model architecture is therefore not a variable of interest in W1 versus W2.

The preprocessing definition is not a variable of interest.

The dataset version is not a variable of interest.

The labels are not a variable of interest.

The evaluation metrics are not a variable of interest.

The statistical estimand is not a variable of interest.

Changing any of these would create a different experiment.

The intended experimental factor is the analytical workflow through which the same computational target is reconstructed and executed.

This is why the compact CNN, the patient-aware split, the normalization definition, the diagnostic label rule, and the statistical estimand must be frozen before primary LLM runs.

## 19. Evidence status

The literature directly supports the following points.

1. PTB XL is an established benchmark dataset for deep-learning ECG analysis.[1,2]
2. Convolutional neural networks are established approaches for direct waveform ECG classification.[2]
3. Preprocessing can interact with ECG model architecture and materially affect performance.[3]
4. Patient-aware separation is relevant because PTB XL contains repeated recordings from patients.[1]
5. Discrimination and calibration represent different aspects of prediction-model performance.[4,6]
6. AUROC and precision-recall measures provide complementary information, especially when class distribution is uneven.[7]
7. Cluster-level bootstrap methods are appropriate methodological tools when repeated observations are correlated within patients or other sampling units.[8,9]
8. Reproducible computational research requires explicit preservation of computational inputs, parameters, software, and execution details.[5]

The following are investigator-defined components of the active reference analysis.

1. The compact CNN architecture.
2. The exclusion of BatchNorm and LayerNorm.
3. The optimizer and hyperparameter configuration.
4. The seed values.
5. The 50 percent PTB XL likelihood threshold.
6. The global record-wise normalization and per-lead normalization sensitivity analysis.
7. The 5,000-resample patient-level paired percentile bootstrap.
8. The primary estimand and cross-task contrast.
9. The decision to use the reference CNN as a fixed probe rather than an architecture-search exercise.

These choices are carried into the reference analysis protocol for operational freezing.

## References

1. Wagner P, Strodthoff N, Bousseljot RD, Kreiseler D, Lunze FI, Samek W, et al. PTB-XL, a large publicly available electrocardiography dataset. Sci Data. 2020;7:154. doi:10.1038/s41597-020-0495-6.

2. Strodthoff N, Wagner P, Schaeffter T, Samek W. Deep Learning for ECG Analysis: Benchmarks and Insights from PTB-XL. IEEE J Biomed Health Inform. 2021;25(5):1519-1528. doi:10.1109/JBHI.2020.3022989.

3. Bickmann L, Plagwitz L, Büscher A, Varghese J. Architecture-Specific Impact of Preprocessing on Machine Learning Models for ECG Classification. Stud Health Technol Inform. 2026;336:529-533. doi:10.3233/SHTI260227.

4. Collins GS, Moons KGM, Dhiman P, Riley RD, Beam AL, Van Calster B, et al. TRIPOD+AI statement: updated guidance for reporting clinical prediction models that use regression or machine learning methods. BMJ. 2024;385:e078378. doi:10.1136/bmj-2023-078378.

5. Papin JA, Mac Gabhann F, Sauro HM, Nickerson D, Rampadarath A. Improving reproducibility in computational biology research. PLoS Comput Biol. 2020;16(5):e1007881. doi:10.1371/journal.pcbi.1007881.

6. Collins GS, Archer L, Dhiman P, et al. Evaluation of clinical prediction models: from development to external validation. BMJ. 2024;384:e074819. doi:10.1136/bmj-2023-074819.

7. Saito T, Rehmsmeier M. The precision-recall plot is more informative than the ROC plot when evaluating binary classifiers on imbalanced datasets. PLoS One. 2015;10(3):e0118432. doi:10.1371/journal.pone.0118432.

8. Rutter CM. Bootstrap estimation of diagnostic accuracy with patient-clustered data. Acad Radiol. 2000;7(6):413-419. doi:10.1016/S1076-6332(00)80381-5.

9. Field CA, Welsh AH. Bootstrapping clustered data. J R Stat Soc Series B Stat Methodol. 2007;69(3):369-390. doi:10.1111/j.1467-9868.2007.00593.x.

## Evidence status

References 1 through 8 were verified against PubMed, publisher, or journal records during the current methods review. Reference 9 was added as supporting statistical methodology for clustered bootstrap reasoning and should be checked against the journal record during final bibliography normalization.

The review remains a methods evidence document. It does not freeze the final reference implementation or statistical analysis plan. Those documents will define the operational protocol after the reference-analysis audit and equivalence work are complete.