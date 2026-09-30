# Study Index

**Status:** Preprotocol study design  
**Revision:** 0.1  
**Date:** 30 September 2026

## 1. Study object

The active study examines a fixed biomedical machine learning analysis conducted through general purpose LLM systems that are accessible to an ordinary user through a zero cost consumer interface.

The scientific object is the analytical workflow. The LLM is treated as the analytical operator. The underlying biomedical prediction task, dataset, task definitions, model specification, training procedure, evaluation metrics, statistical estimand, and interpretation boundaries are held constant across workflow conditions.

The working comparison is between a fully specified monolithic workflow and a structured fresh context workflow. Additional conditions examine specific verification mechanisms.

The study is not framed as a general test of whether LLMs can perform data science, as a comparison of commercial models, or as a benchmark of autonomous research agents.

## 2. Working scientific question

> Under a locked biomedical machine learning protocol, does moving from a fully specified monolithic LLM workflow to a structured fresh context workflow change end to end reference faithful completion when both operate under the same zero cost consumer access constraints?

This wording is a working formulation. It is not frozen as the final protocol wording until the remaining design checks are complete.

## 3. Biomedical machine learning testbed

The first candidate testbed is the archived PTB XL ECG analysis.

The reference study uses two phenotype tasks, HYP versus NORM and MI versus NORM, a fixed direct waveform representation, a fixed one dimensional convolutional model, patient aware train, validation, and test folds, AUROC, average precision, Brier score, calibration assessment, a prespecified contrast between phenotype specific normalization effects, and patient level bootstrap uncertainty.

The archived study is not being revived as its original scientific question. It is being considered as a frozen biomedical machine learning task against which the analytical workflow can be evaluated.

The reference analysis must be executed and independently reproduced before it is used as the numerical reference.

## 4. Experimental workflow conditions

### W0. Minimal monolithic

One concise instruction directs the system to perform the analysis specified in the supplied study package. The complete locked scientific information remains available outside the prompt so that the condition tests interaction scaffolding rather than information withholding.

### W1. Fully specified monolithic

The complete analytical workflow is specified explicitly, but the analysis remains within one context and has no separate external verifier.

### W2. Structured fresh context

The workflow is divided into predefined stages with fresh contexts and structured handoff artifacts.

The current stage sequence is:

1. Data and provenance audit
2. Cohort and label construction
3. Analysis implementation
4. Execution and evaluation
5. Interpretation and reporting

### W3. Structured fresh context with self audit

W3 follows W2 through completion and then performs one explicit adversarial audit in a fresh context. A single bounded repair cycle is permitted.

### W4. Structured fresh context with deterministic validation

W4 follows W2 and applies read only deterministic validators to machine checkable properties of the analysis. A predefined failure may trigger one bounded repair cycle followed by revalidation.

### W5. Structured fresh context with independent LLM audit

W5 follows W2 and adds an independently initiated audit context that evaluates the completed analysis against the locked protocol. One audit cycle and one bounded repair cycle are permitted.

These conditions are derived from recurring control structures developed in PHLOME and Asclepius. Their inclusion is an experimental use of established design principles and is not itself a novelty claim.

## 5. Study wide access envelope

The resource boundary applies to every eligible LLM configuration.

Eligibility requires:

1. Public consumer facing online access.
2. Zero monetary cost for the specific configuration used.
3. No paid subscription.
4. No API access or API billing.
5. No promotional API credit.
6. No institutional, enterprise, university, student, or researcher entitlement.
7. No provider granted research seat.
8. No temporary promotional access.
9. No local model deployment.
10. No small language model selected for local execution.
11. General purpose rather than task specific biomedical specialization.
12. Every capability essential to the study must be available in the zero cost consumer route.
13. The exact interface, model presentation, region, access date, limits, and relevant tool capabilities must be recorded.

Free tier usage limits do not disqualify a system. Zero cost is the criterion; unlimited use is not.

A configuration is excluded if an essential experimental capability requires a paid product, paid agent, paid subscription, API access, or special entitlement even when the underlying model is also available through a nominal free interface.

## 6. Primary outcome candidate

The current primary outcome candidate is end to end reference faithful completion.

A run is successful only when all prespecified critical scientific requirements are satisfied, the required analysis executes, the primary numerical outputs fall within the frozen reference equivalence criteria, and the final interpretation passes the prespecified interpretation audit.

Numerical agreement alone does not define success.

## 7. Biomedical outputs

AUROC, average precision, Brier score, calibration, the primary phenotype contrast, and bootstrap uncertainty remain central outputs of the reference task.

Secondary workflow outcomes will include protocol violation severity, execution failure, resource or access failure, unauthorized human scientific intervention, wall clock time, interaction count, repair attempts, repair success, regression after repair, and reproducibility across repeated runs.

## 8. Reference hierarchy

The evidence hierarchy is:

1. Locked protocol facts
2. Dataset and cohort facts
3. Implementation facts
4. Execution outputs
5. Scientific interpretation

The study distinguishes reference analysis from clinical ground truth.

## 9. Reference analysis gate

The following must be completed before primary LLM collection:

1. Freeze the reference protocol.
2. Verify the original implementation.
3. Execute the reference analysis.
4. Independently reimplement the same locked analysis.
5. Compare the two implementations.
6. Establish the empirical reference equivalence envelope.
7. Freeze numerical agreement criteria.
8. Begin primary LLM collection only after these criteria are fixed.

No primary result may be used to define the equivalence envelope.

## 10. Statistical gate

The primary run count is not yet frozen.

A simulation study will examine operating characteristics across plausible baseline completion rates and workflow effects before the primary sample size is set.

With only a small prespecified set of eligible LLM configurations, model or provider will be treated as a fixed replication stratum rather than as a random sample of all possible models.

## 11. Current open decisions

The following remain open:

* final wording of the research question;
* final eligible LLM set;
* final reference execution;
* numerical equivalence tolerances;
* final primary run count;
* exact information exposure experiment;
* final statistical test implementation.

## 12. Evidence classification

Each substantive decision is assigned one class.

**Evidence fact**  
Directly supported by a peer reviewed paper, formal standard, official dataset source, or current official provider documentation.

**Evidence supported inference**  
A design conclusion derived from more than one relevant source.

**Investigator defined choice**  
A deliberate design choice made to isolate the research question where the literature does not prescribe one unique solution.

**Computed result**  
A result generated by execution, simulation, or another analysis.
