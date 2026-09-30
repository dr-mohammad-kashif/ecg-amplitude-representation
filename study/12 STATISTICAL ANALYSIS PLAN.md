# Statistical Analysis Plan

## 1. Purpose

This plan specifies the statistical analysis for the LLM workflow experiment.

The biomedical reference analysis is defined in [08 REFERENCE BIOMEDICAL ANALYSIS PROTOCOL.md](08%20REFERENCE%20BIOMEDICAL%20ANALYSIS%20PROTOCOL.md). The workflow conditions are defined in [09 LLM WORKFLOW EXPERIMENTAL PROTOCOL.md](09%20LLM%20WORKFLOW%20EXPERIMENTAL%20PROTOCOL.md) and [10 WORKFLOW CONDITIONS AND ABLATION PLAN.md](10%20WORKFLOW%20CONDITIONS%20AND%20ABLATION%20PLAN.md). The scientific fidelity adjudication rules are defined in [11 SCIENTIFIC FIDELITY EVALUATION FRAMEWORK.md](11%20SCIENTIFIC%20FIDELITY%20EVALUATION%20FRAMEWORK.md).

This plan is written before primary LLM collection. The primary block allocation is fixed at 25 randomized W1/W2 blocks per eligible configuration on the basis of the completed sample-size simulation. Primary numerical reference-agreement criteria are frozen only after the reference execution gate has passed. The independent R3 implementation is retained as a reference diagnostic and does not widen the primary criterion.

## 2. Primary objective

The primary objective is to estimate the difference in end-to-end reference-faithful completion between:

- W1, fully specified monolithic workflow;
- W2, structured fresh-context workflow.

The comparison is conditional on the prespecified eligible consumer LLM configurations and the zero cost access envelope.

The study does not treat eligible LLM configurations as a random sample from all possible LLM systems.

## 3. Primary estimand

Let $m$ index the prespecified eligible LLM configurations and let $w$ denote workflow condition.

For each configuration, let

$$
p_{m,w} = P(Y=1 \mid m,w),
$$

where $Y=1$ denotes reference-faithful completion according to the frozen fidelity framework.

The primary workflow contrast for configuration $m$ is

$$
\theta_m = p_{m,W2} - p_{m,W1}.
$$

The primary study estimand is the equally weighted contrast across the prespecified eligible configurations:

$$
\theta =
\frac{1}{M}
\sum_{m=1}^{M}
\left(
p_{m,W2} - p_{m,W1}
\right).
$$

This estimand describes the observed eligible consumer LLM configuration set. It is not an estimate of a population-level effect across all current or future LLMs.

## 4. Primary endpoint

The primary endpoint is a binary run-level indicator of reference-faithful completion.

A run is successful only when all required primary conditions are satisfied:

1. all critical fidelity gates PASS;
2. the required biomedical analysis executes to terminal state;
3. the primary numerical outputs satisfy the frozen reference-agreement criteria;
4. the interpretation gate PASSes;
5. required reproducibility evidence is present;
6. no unauthorized human scientific intervention occurred.

A run that terminates because of a qualifying resource or access limitation is a primary noncompletion.

A run that fails because of an execution or scientific error is also a primary noncompletion.

The failure mechanism is recorded separately and is not collapsed into the binary endpoint.

## 5. Experimental blocking and condition assignment

Primary W1 and W2 runs should be organized into randomized blocks within each eligible LLM configuration.

A block contains one scheduled W1 attempt and one scheduled W2 attempt.

The order of the two workflow assignments is randomized within the block before the run begins.

This block structure is intended to reduce confounding from temporal changes in provider access, consumer limits, browser state, and other short-range operational conditions.

The two runs in a block are not treated as paired biomedical measurements. The block is an experimental scheduling unit created for workflow comparison.

The final number of blocks per configuration is determined by the prespecified simulation study.

Equal numbers of W1 and W2 blocks are planned within each configuration unless an access or infrastructure event makes the planned allocation impossible.

Any deviation from the randomized condition order is recorded before the outcome is interpreted.

## 6. Analysis populations

### 6.1 Eligible configuration population

A configuration enters the primary analysis population only after it passes the Consumer LLM Eligibility Specification and the direct feasibility check for the complete prespecified workflow.

Eligibility is configuration-specific and includes provider, consumer product, plan, displayed model, region, access epoch, capabilities, limits, and information-isolation state.

### 6.2 Primary run population

The primary run population consists of scheduled W1 and W2 attempts initiated under an eligible configuration and primary access epoch.

A scheduled attempt is treated as part of the primary endpoint once the prescribed run allocation has been issued and the consumer interaction is initiated.

A resource or access failure during an initiated attempt is recorded as noncompletion rather than removed from the primary analysis.

### 6.3 Numerically evaluable population

The numerical-fidelity analyses include runs that produce the required valid biomedical outputs needed to calculate the relevant numerical estimand.

Runs without valid numerical outputs remain in the primary binary endpoint but have undefined values for the affected numerical secondary outcome.

No numerical value is imputed for a failed or non-evaluable run.

## 7. Primary estimator

For configuration $m$, let $B_m$ be the number of completed W1/W2 blocks in the primary allocation and let $Y_{m,b,w}$ be the binary completion outcome for workflow $w$ in block $b$.

The configuration-specific estimator is

$$
\hat{\theta}_m =
\frac{1}{B_m}
\sum_{b=1}^{B_m}
\left(
Y_{m,b,W2} - Y_{m,b,W1}
\right).
$$

The primary estimator is

$$
\hat{\theta} =
\frac{1}{M}
\sum_{m=1}^{M}
\hat{\theta}_m.
$$

This estimator gives each prespecified eligible configuration equal weight rather than allowing configurations with more runs to dominate the primary estimand.

The primary run count will be equalized across configurations where feasible.

## 8. Primary inferential procedure

The planned primary inferential procedure is a model-stratified randomization test based on the randomized workflow assignment within blocks.

Under the null hypothesis that the workflow assignment has no effect on the run-level completion outcome, the W1 and W2 labels within each randomized block are exchangeable.

For each randomization replicate, the W1 and W2 labels are independently swapped or retained within each block, while the observed outcomes remain fixed.

The test statistic is the same equally weighted across-configuration contrast used for the primary estimator.

The primary p-value is two-sided and is calculated from the randomization distribution.

The primary randomization test uses 100,000 within-block randomization draws and a fixed random-number seed of 314159. The two-sided p-value uses a plus-one correction.

The primary analysis uses an alpha level of 0.05.

The randomization procedure is conditional on the prespecified eligible LLM configuration set. It does not support population-level generalization beyond that set.

## 9. Primary confidence interval

The primary interval will describe uncertainty arising from repeated workflow runs within the fixed eligible configuration set.

The planned procedure is a stratified block bootstrap that resamples blocks with replacement within each LLM configuration and recomputes the equally weighted across-configuration contrast.

LLM configurations are not resampled because they are fixed experimental strata rather than a random sample from a larger model population.

The default interval will be a 95 percent percentile bootstrap interval.

The simulation work may motivate a more appropriate interval construction if the number of eligible configurations or primary blocks makes the percentile procedure poorly behaved. Any such change will be made before primary collection and recorded as a protocol decision.

## 10. Secondary numerical fidelity endpoint

The key quantitative biomedical ML secondary endpoint is the absolute error in the primary cross-task AUROC estimand.

For an LLM run with numerically evaluable outputs, define

$$
E_{\Delta} =
\left|
(\hat{\Delta}_{HYP}-\hat{\Delta}_{MI})
-
(\Delta_{HYP}^{ref}-\Delta_{MI}^{ref})
\right|.
$$

The reference values and numerical agreement criteria are not available for primary LLM collection until the reference execution chain has passed its required gates.

The distribution of $E_{\Delta}$ will be summarized by median, interquartile range, and prespecified quantiles.

Task-specific AUROC discrepancies and the corresponding average precision, Brier score, and calibration discrepancies are secondary numerical outcomes.

A run that cannot produce a valid numerical estimate is not assigned a numerical error of zero and is not assigned an arbitrary penalty value.

The proportion of primary runs that are numerically evaluable is reported separately.

## 11. Secondary workflow contrasts

The following contrasts are prespecified secondary analyses:

- W1 versus W0;
- W3 versus W2;
- W4 versus W2;
- W5 versus W2.

The W2A/W2B information-exposure experiment remains deferred.

The secondary contrasts use the same run-level fidelity endpoint where sufficient replication exists.

The configuration-specific effects are reported separately before any across-configuration summary.

These analyses are not used to redefine the primary W1 versus W2 conclusion.

## 12. Configuration-specific effects

For each eligible configuration, report:

- number of completed scheduled runs by workflow;
- reference-faithful completion proportion;
- difference in completion proportions;
- numerical-fidelity outcomes where evaluable;
- principal failure classes;
- resource and access failures.

The study reports configuration-specific estimates because a workflow effect may vary across consumer LLM configurations.

The primary equally weighted aggregate does not imply that all configurations behaved identically.

Because the expected number of eligible configurations is small, a formal random-effects distribution across LLMs is not planned.

## 13. Secondary model heterogeneity

Workflow effects by LLM configuration are considered an important secondary descriptive outcome.

The analysis reports the configuration-specific workflow differences and their uncertainty.

A formal workflow-by-model interaction test will be considered only if the final number of eligible configurations and run counts make such a test informative under the prespecified simulation.

It will not be introduced solely because a particular interaction appears interesting in the primary results.

## 14. Secondary biomedical metrics

For the reference analysis itself and for numerically evaluable LLM runs, report:

- AUROC;
- average precision;
- positive-class prevalence;
- Brier score;
- calibration outputs;
- task-specific representation effects;
- primary cross-task representation-effect contrast.

AUROC remains the principal discrimination statistic for the biomedical component.

Average precision is interpreted as a precision-recall measure and is not treated as interchangeable with AUROC.[1]

Brier score and calibration outputs describe probability quality.

No held-out test threshold is optimized for the primary endpoint.

## 15. Reference-analysis uncertainty

The biomedical reference analysis uses the patient-level paired percentile bootstrap defined in the Reference Biomedical Analysis Protocol.

Patients are sampled with replacement.

All eligible test records belonging to sampled patients are retained.

Raw and normalized predictions for the same record remain paired.

The same patient resample is used for HYP and MI.

A bootstrap draw with only one outcome class for a task is rejected and resampled.

The reference analysis uses 5,000 bootstrap resamples.

This procedure is inherited from the archived ECG analysis after methodological review and is retained because the prediction data are clustered within patients.[2]

## 16. Technical exclusions in the biomedical analysis

Technical waveform failures are handled before model fitting according to the reference protocol.

Eligible technical exclusions include missing waveform files, unreadable files, incorrect dimensions, incorrect sampling structure, non-finite waveform values, and infeasible primary normalization.

Technical exclusions are reported by task and fold.

No waveform imputation is performed.

Technical exclusions must not be selected on the basis of model performance.

The same primary technical-eligibility decision applies to raw and normalized representation conditions.

## 17. Missing and noncompleted LLM runs

No statistical imputation is performed for the binary primary endpoint.

For a scheduled and initiated primary attempt:

- successful reference-faithful completion is coded 1;
- any terminal noncompletion is coded 0.

Terminal noncompletion includes scientific or protocol failure, execution failure, resource or access failure, and unauthorized human scientific intervention.

A prespecified study-infrastructure failure occurring before the LLM receives the run assignment may be recorded as non-evaluable at the run level, but it must remain in the operational log and be included in a sensitivity analysis that treats the affected scheduled attempt as noncompletion.

Runs are not removed because their outcome is inconvenient or because their failure mechanism is uncommon.

For numerical secondary outcomes, missing values remain missing. Denominators are reported.

## 18. Provider or access changes during the study

LLM configurations are defined by provider, consumer product, displayed model identity, access epoch, region, and relevant capabilities.

If a change materially alters model identity, free-tier capabilities, context capacity, persistence behaviour, or another feature relevant to the primary experiment, the configuration enters a new access epoch.

Primary runs from distinct epochs are not pooled automatically.

A change during primary collection triggers an access audit and protocol decision before subsequent runs continue.

No new paid capability is introduced to preserve a failing free configuration.

## 19. Multiple comparisons

The W1 versus W2 completion contrast is the single primary confirmatory comparison.

W0 versus W1 and W3 through W5 versus W2 are prespecified secondary contrasts.

Secondary p-values, if reported, are interpreted as supporting analyses and do not determine the primary conclusion.

Secondary analyses will report effect estimates and confidence intervals with the denominator and analysis population made explicit.

No unplanned secondary analysis will be promoted to confirmatory status because of its observed result.

## 20. Multiplicity of numerical outcomes

The primary numerical biomedical outcome remains the cross-task AUROC estimand and its absolute error relative to the reference.

Average precision, Brier score, calibration, task-specific AUROC effects, and other metrics are secondary.

The study will not select the most favorable metric after results are observed.

All prespecified secondary numerical outcomes are reported where evaluable.

No composite numerical endpoint will be constructed after collection.

## 21. Resource and accessibility outcomes

Observable resource variables are analyzed as secondary outcomes.

These include:

- user turns;
- assistant turns;
- context resets;
- execution attempts;
- audit attempts;
- repair attempts;
- file transfers;
- elapsed wall-clock time;
- free-tier limit encounters;
- quota-induced interruptions;
- resource-limited noncompletion;
- human mechanical time;
- human scientific intervention count.

For continuous resource measures, report median, interquartile range, range or other distributional summaries appropriate to the observed data.

For binary resource events, report counts and proportions.

Provider-side token usage or infrastructure compute is reported only when exposed reliably by the consumer interface.

## 22. Failure and recovery outcomes

The fidelity framework provides the failure classes and gate states.

Secondary analyses summarize:

- critical, major and minor findings;
- scientific or protocol failures;
- execution failures;
- resource or access failures;
- unauthorized human scientific interventions;
- self-audit findings;
- deterministic validator findings;
- independent audit findings;
- repair success;
- post-repair regression;
- unresolved terminal failures.

Repair is not treated as erasing the initial error.

For W3 through W5, the study reports both the pre-repair state and final terminal state.

## 23. Sensitivity analyses

Prespecified statistical sensitivity analyses include:

1. alternative treatment of scheduled infrastructure failures as noncompletion;
2. configuration-specific rather than equally weighted aggregate reporting;
3. alternative confidence-interval construction if the reference or simulation work shows poor small-sample behaviour;
4. exclusion of runs occurring in a materially changed access epoch if that epoch cannot be demonstrated equivalent before pooling;
5. descriptive restriction to runs without resource/access interruption.

The fifth analysis is explicitly sensitivity analysis because excluding resource failures would no longer represent the complete zero cost access envelope.

No sensitivity analysis will replace the primary analysis.

## 24. Sample-size simulation

The number of primary W1/W2 blocks per eligible configuration is fixed at 25 by the completed simulation recorded in [SAMPLE SIZE SIMULATION.md](SAMPLE%20SIZE%20SIMULATION.md).

The simulation will model:

- the number of eligible LLM configurations;
- number of randomized W1/W2 blocks per configuration;
- baseline W1 completion probabilities by configuration;
- plausible W2 minus W1 completion effects;
- possible configuration heterogeneity;
- within-block dependence scenarios;
- resource or access failure scenarios;
- the planned model-stratified randomization test;
- the planned confidence-interval procedure.

The scenario values will be classified as either:

- evidence-supported inputs;
- investigator-defined sensitivity scenarios;
- computed quantities from the simulation.

The simulation will report operating characteristics such as type I error, power across plausible workflow effects, interval precision, and sensitivity to unequal configuration-specific completion probabilities.

The simulation record, source code, scenario grid, seeds, and decision rule are retained with the study. The previous 12 to 15 block proposal and earlier six-block heuristic are retired.

## 25. Stopping rules

The number of primary runs is fixed by the completed simulation plan.

There is no early stopping for favorable or unfavorable primary results.

Additional primary runs are not added because the observed effect is borderline, unexpectedly large, or unexpectedly small.

A workflow configuration may be stopped for an operational reason such as loss of qualifying access, provider configuration change, or infrastructure failure.

Such a stop is recorded and is not silently replaced with another configuration.

If a configuration becomes ineligible before its planned primary allocation is complete, the remaining planned attempts are recorded as unrealized and the effect of the incomplete stratum is addressed in the prespecified analysis and sensitivity analysis.

## 26. Exploratory analyses

Analyses not listed in this plan are exploratory.

Exploratory analyses may include detailed error subgrouping, alternative prompt analyses, new workflow combinations, post hoc numerical thresholds, or additional biomedical subgroup analyses.

Exploratory analyses are reported separately and cannot alter the primary endpoint, primary estimand, sample-size decision, or reference-agreement criteria retrospectively.

## 27. Reporting

The primary statistical report will contain:

- eligible LLM configuration count and access epochs;
- primary run allocation;
- completed and failed runs;
- reference-faithful completion proportions by configuration and workflow;
- equally weighted primary workflow contrast;
- randomization-test result;
- 95% confidence interval;
- failure classification;
- resource/access events;
- primary numerical fidelity outcome;
- configuration-specific results;
- prespecified secondary contrasts;
- deviations and access changes.

For the biomedical component, the report will also contain the reference-analysis results required by the reference protocol, including AUROC, average precision, prevalence, Brier score, calibration, primary cross-task contrast, bootstrap intervals, and sensitivity analyses.

The denominator for every proportion and the analysis population for every numerical outcome will be explicit.

## 28. Reproducibility requirements

The statistical release must retain:

- analysis code;
- simulation code;
- simulation seed;
- final sample-size decision;
- randomization seeds where stochastic enumeration is used;
- bootstrap seeds;
- primary run manifests;
- model configuration records;
- access epochs;
- fidelity adjudication records;
- numerical reference criteria;
- repository commit;
- software environment.

This follows the broader reproducibility principle that the workflow and analytical settings required to produce a result should themselves be preserved.[3,4]

## 29. Protocol changes

Any substantive change to this plan before primary collection will be documented with:

- the month of change;
- the affected section;
- the reason;
- supporting evidence or investigator rationale;
- whether any outcome from the primary experiment had already been observed.

After primary collection begins, changes to primary analysis will not be silently incorporated into the original analysis.

The protocol change record will distinguish amendments made before primary outcome observation from deviations made after primary outcome observation.

## References

1. Saito T, Rehmsmeier M. The precision-recall plot is more informative than the ROC plot when evaluating binary classifiers on imbalanced datasets. PLoS One. 2015;10(3):e0118432. doi:10.1371/journal.pone.0118432.

2. Rutter CM. Bootstrap estimation of diagnostic accuracy with patient-clustered data. Acad Radiol. 2000;7(6):413-419. doi:10.1016/S1076-6332(00)80381-5.

3. Sandve GK, Nekrutenko A, Taylor J, Hovig E. Ten simple rules for reproducible computational research. PLoS Comput Biol. 2013;9(10):e1003285. doi:10.1371/journal.pcbi.1003285.

4. Papin JA, Mac Gabhann F, Sauro HM, Nickerson D, Rampadarath A. Improving reproducibility in computational biology research. PLoS Comput Biol. 2020;16(5):e1007881. doi:10.1371/journal.pcbi.1007881.


