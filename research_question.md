# Research question

## Primary question

Does ECG amplitude normalization remove or alter information relevant to some diagnostic tasks, and is that effect different across tasks?

## Why this is worth testing

Amplitude normalization is often treated as a routine preprocessing choice. This study asks whether that choice can change the information available to a model in a way that matters differently for different diagnostic tasks.

The point is not to assume that normalization is harmful. The point is to test whether treating it as neutral is justified.

## Working hypothesis

If amplitude carries more useful information for some diagnostic tasks than others, a normalization procedure that changes amplitude relationships may affect those tasks differently.

The first candidate comparison uses hypertrophy and myocardial infarction because they are established PTB-XL diagnostic superclasses and because the clinical basis for hypertrophy includes voltage-related ECG criteria. The study will not assume that one task is independent of amplitude. That will be treated as an empirical question.

## Alternative possibilities

The observed effect may be small.

The effect may depend more on the model than on the diagnostic task.

The effect may disappear under a different but still defensible evaluation setup.

Any of these outcomes would narrow the claim that can be made about preprocessing.

## Scope

The first analysis will use PTB-XL version 1.0.3 and a small number of binary diagnostic tasks that can be defined clearly from the dataset labels. The final task definitions and inclusion rules will be frozen in analysis_plan.md before the primary comparison is run.

## What this study will not claim

It will not establish clinical utility, clinical superiority, causal effects in patients, or a universally correct ECG preprocessing method.
