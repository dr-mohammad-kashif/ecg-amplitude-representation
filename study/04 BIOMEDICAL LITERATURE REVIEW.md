# Biomedical Literature Review

## Scope

This review describes the biomedical object that will serve as the experimental testbed for the active study. It is separate from the LLM and workflow literature.

The purpose is to establish what an ECG measurement represents, what the PTB XL dataset contains, what its diagnostic labels mean, what limitations follow from those labels, and why the dataset can support a controlled biomedical machine learning workflow experiment.

The review does not attempt to establish a new clinical finding. It also does not decide the final machine learning implementation. Detailed treatment of preprocessing, model architecture, optimization, performance metrics, uncertainty estimation, and statistical analysis will be recorded in the machine learning methods review.

## 1. The electrocardiogram as a biomedical measurement

An electrocardiogram is a recorded representation of cardiac electrical activity obtained through an electrode and lead system. The modern 12 lead ECG combines limb and precordial leads that observe the electrical field from different orientations. Standardization guidance from the American Heart Association, American College of Cardiology, and Heart Rhythm Society treats lead placement, recording methods, waveform presentation, digital acquisition, and computer processing as integral parts of ECG measurement rather than as incidental implementation details.[1]

The physical interpretation of a lead is therefore tied to the observation geometry. Vector descriptions of the 12 lead ECG distinguish the cardiac electrical vector, the lead vector, and the volume conductor through which electrical activity is observed.[2] A waveform sample should consequently not be regarded as an isolated scalar measurement whose meaning is independent of lead identity or acquisition context.

This matters for a machine learning study because the model receives the recorded representation rather than the underlying electrophysiological state. Changes in scaling, filtering, sampling, lead handling, or other transformations can change the numerical representation presented to the model without necessarily corresponding to an equivalent change in the biological state.

The active study therefore treats the ECG representation as part of the scientific protocol. The waveform representation must remain fixed across workflow conditions if differences in LLM workflow are to be interpreted without simultaneously changing the biomedical input.

## 2. The 12 lead representation

A standard clinical 12 lead ECG contains leads I, II, III, aVR, aVL, aVF, and V1 through V6.[1] The limb leads and precordial leads provide complementary views of cardiac electrical activity. The AHA statement emphasizes that lead labels should retain their standard nomenclature and that anatomical interpretation is derived from the pattern across leads rather than from treating an individual lead as a direct map of one cardiac region.[3]

This has a direct methodological consequence for the reference analysis.

The complete 12 lead waveform must be preserved as an ordered multichannel object. Treating the ECG as an unordered collection of twelve independent traces would remove part of the representation being evaluated. Likewise, changing the lead ordering between workflow conditions would change the computational problem even if the same recordings were supplied.

The candidate reference analysis therefore uses the direct 12 lead waveform representation at a fixed sampling frequency rather than converting the signal into an alternative feature representation before the LLM workflow begins.

The choice to retain the waveform rather than a manually engineered feature table also keeps the biomedical testbed close to the original measurement while allowing the reference model to operate on a high dimensional but well defined input.

## 3. Clinical meaning of the selected diagnostic categories

The candidate reference analysis uses two binary tasks derived from the PTB XL diagnostic superclasses.

### 3.1 Hypertrophy

PTB XL defines HYP as the hypertrophy diagnostic superclass. The associated hierarchy contains several distinct diagnostic subclasses, including left ventricular hypertrophy, right ventricular hypertrophy, left or right atrial overload or enlargement, and septal hypertrophy.[4]

This is clinically important because HYP is not a single pathophysiological phenotype. It is a superclass that aggregates several related but distinguishable ECG diagnostic statements.

The reference task therefore should not be described as a pure test for left ventricular hypertrophy. It is a machine learning classification task using the PTB XL HYP superclass as defined by the dataset annotation system.

This distinction prevents a common interpretive error. A model that predicts the PTB XL HYP label is reproducing the dataset-defined classification target. It is not necessarily demonstrating that the patient has one specific anatomical form of cardiac hypertrophy.

### 3.2 Myocardial infarction

PTB XL defines MI as a diagnostic superclass whose subclasses include anterior, inferior, lateral, and posterior myocardial infarction statements.[4]

As with HYP, the MI superclass aggregates several diagnostic categories. It should therefore be treated as the dataset-defined diagnostic target rather than as a single homogeneous clinical event.

The active study does not attempt to infer infarct timing, culprit vessel, infarct size, or prognosis. Those questions are outside the reference task.

### 3.3 Normal ECG

NORM is defined by PTB XL as the normal ECG diagnostic superclass.[4] It is used in the candidate binary tasks as the negative category.

NORM should not be silently converted into the broader clinical claim that the corresponding individual is healthy. The target is a diagnostic statement about the ECG within the dataset annotation scheme.

This distinction is particularly important when the study compares an abnormal superclass against NORM. The resulting classification task is a distinction between dataset-defined ECG categories, not a population-level definition of disease versus health.

## 4. PTB XL as the biomedical testbed

PTB XL was introduced as a large publicly accessible clinical 12 lead ECG dataset intended in part to address the limited availability of public data and the lack of standardized evaluation procedures for automated ECG analysis.[5]

The current version relevant to the proposed study is PTB XL v1.0.3. The official PhysioNet record describes 21,799 clinical 12 lead ECG recordings from 18,869 patients, with each recording lasting 10 seconds. The dataset provides waveform data at 500 Hz and a downsampled version at 100 Hz.[6]

The dataset contains substantial annotation and metadata in addition to the waveform. The database includes patient and recording identifiers, demographic variables, acquisition metadata, ECG statements, diagnosis likelihoods, and signal quality information. Diagnostic statements are organized into five broad superclasses and 24 subclasses.[5,6]

This combination makes PTB XL suitable for the active study for a reason that is different from simply having many records. It provides a biomedical prediction problem with a defined annotation system, a known recording structure, patient identifiers, recommended patient-aware folds, and an established machine learning benchmark history.[5,6,7]

The task can therefore be held fixed while the analytical workflow around it is changed.

## 5. Dataset version and provenance

The original PTB XL publication describes 21,837 records from 18,885 patients for the initial release. Later versions contain fewer records because duplicate waveform records were removed and the dataset was revised.[5,6]

The active study uses version 1.0.3 rather than mixing counts or files from different releases.

The official version record identifies version 1.0.3 as the release dated 9 November 2022 and assigns it a persistent dataset DOI.[6] This version contains 21,799 recordings from 18,869 patients.[6]

The difference between the original publication counts and the current version is methodologically relevant. A literature paper using the original release and an analysis using v1.0.3 are not automatically based on identical records. The reference implementation must therefore identify the dataset version explicitly and use the corresponding files, metadata, and fold assignments.

This is also relevant to LLM reproduction. A workflow can appear correct while silently using a different release of the same dataset. Dataset version is therefore part of scientific fidelity rather than administrative metadata.

## 6. Diagnostic annotation and uncertainty

PTB XL uses SCP ECG diagnostic statements and assigns likelihood information to diagnostic statements. The dataset documentation states that the likelihood values are stored with the statements and can be zero when no likelihood information is available.[6] The original dataset paper describes likelihood weights derived from report terminology, ranging from lower-confidence statements such as those corresponding to "cannot be excluded" through stronger diagnostic language.[5]

This structure means that the annotation is not inherently binary at the source level.

The candidate binary task therefore requires an explicit rule that converts the source annotations into the analysis labels. The archived reference protocol defines a threshold-based construction using a 50 percent likelihood threshold. That threshold is a study-defined operational rule, not a claim that 50 percent is a universal clinical decision threshold.

The distinction matters for the LLM workflow experiment. A workflow that changes the threshold, substitutes a different interpretation of the diagnostic hierarchy, or treats any nonzero likelihood as a positive label has changed the scientific task.

The dataset labels also do not constitute an independent clinical ground truth. They are diagnostic statements associated with the ECG record and produced through the dataset's annotation process. The PTB XL benchmark literature itself notes that the dataset contains cardiologist annotations and associated likelihood information rather than an independently adjudicated outcome standard.[7]

## 7. Multi-label structure and the meaning of the binary tasks

PTB XL is intrinsically multi-label. A single ECG may receive more than one diagnostic superclass.[5,6] The published superclass counts therefore exceed the total number of ECG recordings when summed.

This creates an important constraint on interpretation.

The HYP versus NORM and MI versus NORM tasks are not mutually exclusive diagnostic states in the source dataset. An ECG may contain multiple diagnostic statements, and the binary task must therefore specify how records with co-occurring categories are treated.

The archived reference protocol defines the candidate binary labels explicitly rather than assuming that the dataset can be converted into a single five-class target without loss. The protocol also applies an exclusion rule for records that do not resolve cleanly into the selected positive and negative categories.

This is a deliberate simplification for experimental control. It should not be described as a faithful representation of the full clinical diagnostic space.

For workflow evaluation, that simplification is useful because the LLM is given a fixed, reproducible cohort definition. The scientific cost is that the experiment addresses a controlled classification problem rather than the full multi-label clinical interpretation task.

## 8. Patient structure and repeated recordings

The 21,799 recordings come from 18,869 patients.[6] The record-to-patient ratio means that the dataset contains patients with more than one ECG.

This structure matters for machine learning evaluation because records from the same patient are not equivalent to independent biological observations.

PTB XL provides a recommended ten-fold split in which patient assignments are respected, meaning that records from the same patient are placed in the same fold. The official documentation recommends folds 1 through 8 for training, fold 9 for validation, and fold 10 for testing.[6]

The candidate reference analysis follows this patient-aware structure.

This is not merely a procedural preference. Allowing the same patient to contribute records to both training and test data would change the estimand by permitting patient-specific information to cross the evaluation boundary.

The patient identifier is therefore part of the data structure even when it is not supplied as a predictive feature.

## 9. Signal quality and acquisition context

PTB XL provides metadata describing signal quality, including static noise, burst noise, baseline drift, and electrode problems.[6] These fields make clear that the waveform is a measured clinical signal rather than a uniformly clean mathematical time series.

The original dataset was collected over several years using clinical ECG equipment, and the dataset documentation records acquisition and device metadata.[5,6]

This creates a useful tension for the active experiment.

The data are sufficiently structured to support reproducible computation, but they retain the irregularities of real clinical recordings. An LLM that ignores signal-quality information or silently alters preprocessing can therefore change the effective scientific problem.

At the same time, the active study does not attempt to model all sources of acquisition variation. It uses a fixed waveform representation and a locked reference analysis. The purpose is to evaluate workflow fidelity, not to produce a comprehensive robustness study of ECG acquisition.

## 10. Existing machine learning evidence on PTB XL

PTB XL has an established benchmark literature. Strodthoff and colleagues evaluated multiple deep learning architectures and used PTB XL to provide benchmark results for ECG statement prediction and other tasks. Their analysis found strong performance from convolutional neural networks, including residual and inception-style architectures, and emphasized that evaluation should extend beyond a single accuracy value to uncertainty and interpretability considerations.[7]

This establishes that direct waveform-based deep learning on PTB XL is a mature research setting.

The active study therefore does not introduce the use of convolutional networks on PTB XL as a methodological novelty. The network in the reference analysis is deliberately modest and fixed because the model is an experimental control rather than the main scientific object.

The reference model should be interpreted as a deterministic part of the biomedical task specification. The question is whether an LLM can reproduce the locked computational analysis through different workflow structures, not whether the chosen CNN is a competitive state of the art classifier.

## 11. Representation and preprocessing are scientifically consequential

The distinction between biomedical signal and numerical representation is also relevant to preprocessing.

Recent work on PTB XL has shown that signal cleaning, trend removal, and normalization can affect different ECG model architectures differently. A 2026 study evaluating 24 preprocessing combinations across six architectures reported architecture-dependent changes in performance and found that convolutional models in that study performed best with raw, unnormalized ECG inputs.[7]

The finding is relevant to the current project even though preprocessing is not the primary scientific question.

It supports a strict methodological principle.

Once the reference preprocessing is locked, an LLM workflow should not be permitted to replace it with a superficially plausible alternative simply because the alternative is common in machine learning practice.

Normalization, filtering, resampling, clipping, lead-wise transformations, and other preprocessing operations can alter the information presented to a model. The correct operation is therefore defined by the study protocol rather than by generic coding conventions.

The detailed literature and methodological comparison of these choices will be handled in the machine learning methods review.

## 12. Why HYP and MI provide a useful paired biomedical target

The candidate reference analysis uses HYP versus NORM and MI versus NORM rather than one disease classification task.

This choice does not imply that HYP and MI are clinically equivalent categories. They are not. They differ in clinical substrate, ECG manifestations, label composition, and likely signal characteristics.

Their value in the experiment is methodological.

A workflow that produces a systematic change in the primary estimand for one task but not another provides a more informative test of scientific fidelity than a single binary classification endpoint. The archived analysis therefore defines a contrast between the task-specific changes under the two phenotypes.

This contrast should be interpreted as a property of the locked computational analysis. It is not a clinical comparison of hypertrophy and myocardial infarction.

Using two tasks also creates an internal check against accidental task-specific simplification. An LLM could reproduce one binary task correctly while implementing the other with a different cohort, label rule, or evaluation procedure.

## 13. What the biomedical testbed can establish

A successful experiment using this testbed could provide evidence about whether different LLM workflow structures can reproduce a prespecified biomedical machine learning analysis while maintaining its dataset version, cohort definition, signal representation, model, evaluation, statistical estimand, and interpretation boundaries.

It could also reveal distinct failure modes.

A workflow might use the wrong PTB XL release, misread the diagnostic hierarchy, mishandle multi-label records, split patients incorrectly, alter waveform preprocessing, change the CNN specification, compute a different metric, or interpret a dataset-defined label as a clinical ground truth.

These are scientifically different failures even when the final AUROC happens to be close to the reference.

The biomedical literature therefore supports evaluating the workflow at several levels rather than judging it from a single number.

## 14. What the biomedical testbed cannot establish

The reference analysis cannot establish clinical effectiveness.

The study is based on a retrospective public dataset collected in a historical acquisition environment. It does not provide prospective clinical validation, deployment performance, treatment outcomes, or evidence that an LLM workflow should be used for clinical decision making.

The study also cannot establish that PTB XL represents the current global ECG population. Its recordings were collected over a historical period with particular equipment and acquisition conditions.[5,6]

Likewise, agreement with the PTB XL diagnostic labels is not equivalent to agreement with an independent clinical adjudication process. The dataset annotations are the target of the reference analysis.

Finally, success on the fixed PTB XL task cannot by itself establish that the same workflow will reproduce arbitrary biomedical studies. Generalization beyond the study task remains an empirical question that would require additional datasets and tasks.

These boundaries are part of the scientific interpretation and should remain explicit in the final report.

## 15. Relationship to the workflow experiment

The biomedical and workflow components are deliberately separated.

The biomedical layer defines:

- the dataset and version;
- the waveform representation;
- the candidate cohorts;
- the label construction;
- the patient-aware split;
- the fixed predictive model;
- the performance measures;
- the primary estimand;
- the statistical uncertainty procedure;
- the interpretation boundaries.

The workflow layer defines how a general purpose LLM receives, implements, checks, executes, and reports that locked analysis.

The experimental question concerns the second layer while holding the first layer fixed.

This separation is the main reason the study can be interpreted as a workflow experiment rather than as another open-ended LLM benchmark.

## 16. Evidence and investigator-defined components

The core biomedical facts in this review come from the PTB XL dataset publication, official PhysioNet documentation, the AHA/ACC/HRS ECG standardization statements, and established PTB XL benchmark literature.[1-7]

The 2026 preprocessing study is used only to establish that representation and preprocessing can have architecture-dependent effects.[7]

The following statements are investigator-defined rather than directly prescribed by the biomedical literature.

1. Using PTB XL as the fixed testbed for the workflow experiment
2. Using the HYP versus NORM and MI versus NORM tasks
3. Applying the archived 50 percent likelihood threshold rule
4. Treating the reference CNN as a fixed scientific component rather than a model-selection target
5. Evaluating workflow fidelity against the locked reference analysis

These choices are carried forward to the reference analysis protocol, where they must be specified operationally.

## References

1. Kligfield P, Gettes LS, Bailey JJ, Childers R, Deal BJ, Hancock EW, et al. Recommendations for the standardization and interpretation of the electrocardiogram. Part I: The electrocardiogram and its technology. A scientific statement from the American Heart Association Electrocardiography and Arrhythmias Committee, Council on Clinical Cardiology; the American College of Cardiology Foundation; and the Heart Rhythm Society. Circulation. 2007;115(10):1306-1324. doi:10.1161/CIRCULATIONAHA.106.180200.

2. Man S, Maan AC, Schalij MJ, Swenne CA. Vectorcardiographic diagnostic & prognostic information derived from the 12-lead electrocardiogram: Historical review and clinical perspective. J Electrocardiol. 2015;48(4):463-475. doi:10.1016/j.jelectrocard.2015.05.002.

3. Wagner GS, Macfarlane P, Wellens H, Josephson M, Gorgels A, Mirvis DM, et al. AHA/ACCF/HRS recommendations for the standardization and interpretation of the electrocardiogram: part VI: acute ischemia/infarction. J Am Coll Cardiol. 2009;53(11):1003-1011. doi:10.1016/j.jacc.2008.12.016.

4. Wagner P, Strodthoff N, Bousseljot RD, Kreiseler D, Lunze FI, Samek W, et al. PTB-XL, a large publicly available electrocardiography dataset. Sci Data. 2020;7:154. doi:10.1038/s41597-020-0495-6.

5. PhysioNet. PTB-XL, a large publicly available electrocardiography dataset v1.0.3 [Internet]. Cambridge, MA: PhysioNet; 2022 [cited 2026 Sep 30]. Available from: https://physionet.org/content/ptb-xl/1.0.3/

6. Strodthoff N, Wagner P, Schaeffter T, Samek W. Deep Learning for ECG Analysis: Benchmarks and Insights from PTB-XL. IEEE J Biomed Health Inform. 2021;25(5):1519-1528. doi:10.1109/JBHI.2020.3022989.

7. Bickmann L, Plagwitz L, Büscher A, Varghese J. Architecture-Specific Impact of Preprocessing on Machine Learning Models for ECG Classification. Stud Health Technol Inform. 2026;336:529-533. doi:10.3233/SHTI260227.
