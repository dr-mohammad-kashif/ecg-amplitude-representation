# Research log

I am using this file to keep the project history visible across research phases. The important record here is why the scientific object changed.

## Phase 1. The ECG question

I began with a focused question about amplitude normalization in ECG machine learning.

The original study used PTB-XL version 1.0.3 and compared the native 100 Hz, 12-lead waveform with a global record-wise z-score representation. I chose HYP versus NORM and MI versus NORM as two prespecified phenotype tasks and fixed the model and evaluation procedure so that the representation change was the intended difference.

I spent substantial time on the data and methods before any primary model result was generated. The PTB-XL metadata were audited, the label rules were made explicit, representative waveform files were checked, the model input and architecture were fixed, and the uncertainty analysis was specified at the patient level because patients can contribute more than one ECG record.

The implementation was also tested. A real issue was found in the unthresholded label sensitivity and corrected before any primary test result was interpreted.

At that stage I was still treating the study as a live ECG research question.

## Phase 2. A deeper literature review changed the question

I then went back to the literature more deeply to check whether the central contrast was actually open.

That review found recent work that was much closer to my question than the earlier literature pass had suggested. XAND-ECG reports PTB-XL experiments using HYP and MI, a global z-score across all leads and time points within each ECG, and direct comparisons of normalization choices. Its findings also report different normalization behaviour across disease families. The project documents use PTB-XL version 1.0.3 and a 100 Hz, 12-lead representation.

A separate 2026 study by Bickmann et al. examined 24 preprocessing combinations across six ECG architectures on PTB-XL and found architecture-dependent effects of preprocessing. That made it difficult to defend a broad representation question as new.

ACL-ECG also uses a global normalization calculated across all leads and time points and explicitly contrasts that with per-lead normalization in a PTB-XL setting.

The result of this review was not a new analysis. It was a change in my understanding of the gap. The question I had frozen was no longer cleanly distinct from work that already existed.

## Phase 3. I tested whether the question could be made more specific

I did not want to abandon the project after finding overlap, so I tested whether the scientific question could be narrowed without simply adding more arbitrary ablations.

I examined several possibilities, including separating centering from scaling, comparing input normalization with internal normalization, using external validation, reinjecting normalization statistics, and asking a broader question about which signal invariances a biomedical representation should preserve.

I then checked those ideas against the literature.

That second pass also showed substantial precedent. Work on normalization and representation learning already covers normalization decomposition, internal and reversible normalization, restoration or reinjection of normalization statistics, and related representation-invariance questions.

I therefore did not turn any of those ideas into a standalone novelty claim.

## Phase 4. I went back to the earlier projects

At that point I returned to PHLOME and Asclepius, not to reuse them as finished methods but to understand which research problems had actually changed how those systems were built.

The recurring ideas were explicit state and context, provenance, uncertainty, validation before handoff, controlled model context, deterministic checks, reconciliation, explicit unresolved states and separate evidence for completion.

I treated these as candidate research questions rather than assuming that a design principle was automatically a scientific contribution.

## Phase 5. I checked those ideas against current ECG research

The same literature test was then applied to the ideas coming from PHLOME and Asclepius.

I considered combinations such as signal quality with model uncertainty, label provenance with model behaviour, clinically grounded metamorphic tests, deterministic ECG validators, evidence-grounded failure analysis, and the interaction between preprocessing and label quality.

Again, the deeper literature showed that most of these areas already had substantial precedent. Recent ECG work addresses label certainty, signal quality, preprocessing effects, and validation or perturbation-based analysis. Broader machine-learning literature also covers several of the proposed methodological patterns.

The useful outcome was not to force a paper out of a weakly differentiated idea. The outcome was a clearer boundary around what I could no longer claim as a new scientific object.

## Phase 6. The research object itself needed to change

After the second round of literature checking, I stopped trying to rescue the original ECG question by adding another comparison.

The important change was conceptual. I was no longer asking how one ECG preprocessing operation behaves. I was asking a different kind of question about how a scientific analysis can be carried out under constrained resources and how the reliability of that workflow can be evaluated.

That meant the unit of research would need to move from an ECG preprocessing intervention to the analysis workflow itself.

## Phase 7. The new direction

The direction that emerged is a controlled study of whether a general-purpose online LLM can reproduce a conventional biomedical machine-learning analysis under constrained, explicitly specified workflow conditions.

The idea is not to ask the broad question of whether an LLM can do data science. That literature is already crowded.

The more specific question is whether workflow constraints such as staged data access, smaller data chunks, fresh context, multi-gate checking and independent audit change the scientific fidelity of an LLM-assisted analysis relative to a conventional reference analysis.

The intended comparison is also important. The LLM is not being treated as a replacement for the ECG classifier. It would be compared with the analyst or workflow that assembles and executes the analysis, while the raw data, frozen protocol and evaluation target are held constant.

For the first implementation, the candidate models must be general-purpose models that an ordinary user can access directly online for free. Local models and small language models are outside the scope of this study.

This is still a research direction, not a frozen protocol. The next step is another literature and benchmark review to identify exactly what has already been tested, then define the experimental object, comparison conditions, fidelity measures, cost measures and failure criteria.

## Writing standard for the research history

I record what I was investigating, what I found, and why that changed the next decision.

I do not present the later LLM direction as if it existed from the beginning.

I do not describe literature discovery as if a separate system performed the scientific reasoning. The research record is written from the decisions and checks that actually shaped the project.

The archive remains available so that the original ECG study can be inspected without rewriting its earlier reasoning.
