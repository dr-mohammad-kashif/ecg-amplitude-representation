# Research question

## What I am asking

Does ECG amplitude normalization remove or alter information relevant to some diagnostic tasks, and is that effect different across tasks?

## Why I am asking it

Normalization is easy to think of as a harmless preparation step. I am less interested in whether it is commonly used than in whether the assumption behind it holds for the task I am studying.

If amplitude contains information that is useful for one diagnosis and less useful for another, changing amplitude relationships could affect those tasks differently.

## Working hypothesis

My working hypothesis is that the effect of normalization will not be identical across diagnostic tasks.

I am treating that as a hypothesis rather than a conclusion. The effect could be small, could depend more on the model than the task, or could disappear under a reasonable change in the analysis.

## The first comparison

I am starting with two candidate binary tasks from PTB-XL

- hypertrophy versus normal
- myocardial infarction versus normal

I chose these because they are established PTB-XL diagnostic superclasses and because there is a clear clinical reason to pay attention to amplitude when thinking about hypertrophy.

I will freeze the exact label construction and exclusions after the data audit.

## What this will not show

This study will not establish clinical utility or clinical superiority. It will not show a causal effect in patients. It will only tell me what happens within the PTB-XL data and the analysis I actually run.
