# Reproducibility and Computational Environment

## 1. Purpose

The reproducibility record defines the computational and provenance information that must be preserved for the biomedical reference analysis and for every LLM workflow run.

The study separates three objects.

1. The scientific specification, which defines the biomedical task, cohort, model, training procedure, evaluation and interpretation boundaries.
2. The execution environment, which provides the fixed software and hardware substrate used to run generated analysis code.
3. The LLM workflow, which determines how an eligible consumer LLM receives the scientific specification, generates or modifies artifacts, receives execution evidence, and reaches a terminal state.

Reproducibility requires all three to be traceable.

The objective is not to claim that a consumer LLM interface can be reproduced indefinitely. Consumer model identity, interface behavior and free-tier capabilities may change. The objective is to make each experimental configuration and each completed analysis sufficiently documented that another investigator can reconstruct the study conditions and independently inspect the resulting computation.[1-3]

## 2. Reproducibility layers

The study uses five reproducibility layers.

### Layer 1. Scientific specification

The following must be versioned before primary data collection:

- research question;
- dataset and version;
- cohort and label rules;
- patient-aware split;
- waveform representation;
- preprocessing;
- model architecture;
- training configuration;
- evaluation metrics;
- primary estimand;
- uncertainty procedure;
- sensitivity analyses;
- interpretation boundaries.

The formal scientific specification is maintained in the reference protocol and associated analysis documents.[4]

### Layer 2. Computational environment

The reference implementation and standardized execution substrate must record:

- operating system;
- Python version;
- package manager;
- package versions;
- machine-learning framework version;
- numerical-library versions;
- data-loading and signal-processing library versions;
- execution command;
- environment manifest;
- hardware relevant to execution;
- available CPU, RAM and GPU where applicable.

The environment record should be generated from the environment actually used for execution rather than reconstructed after the analysis.

### Layer 3. Source and artifact provenance

Every study-produced computational artifact must be attributable to:

- repository commit;
- file path;
- source file version;
- execution input;
- execution command;
- environment version;
- run identifier;
- parent artifact where applicable.

Generated code is treated as an experimental artifact. It is not overwritten in place when a later repair or revision occurs.

### Layer 4. LLM configuration

Each LLM run must preserve the configuration needed to identify the consumer system:

- configuration ID;
- provider;
- consumer product;
- access plan;
- displayed model identity;
- model version if exposed;
- access epoch;
- region;
- tool availability;
- information-isolation state;
- relevant interface settings;
- prompt version;
- context condition;
- allowed execution substrate.

This follows the reporting emphasis of TRIPOD-LLM on model identity, prompting, evaluation setting, human oversight and reproducibility, while recognizing that consumer LLM configurations may change over time.[1]

### Layer 5. Run-level execution record

Each run must preserve a machine-readable record linking the LLM interaction to the actual computational execution.

The minimum chain is:

$$
\text{configuration}
\rightarrow
\text{prompt/context}
\rightarrow
\text{generated artifact}
\rightarrow
\text{execution}
\rightarrow
\text{stdout/stderr/files}
\rightarrow
\text{evaluation}
\rightarrow
\text{fidelity adjudication}
$$

A final report without this provenance chain is not sufficient evidence of reproducibility.

## 3. Standardized execution substrate

The LLM conditions must use the same logical execution environment.

The execution substrate should expose a controlled workspace containing, as applicable:

```text
study_package/
data/
environment/
run/
outputs/
```

The exact directory names may change during implementation, but the logical separation must remain.

The LLM is permitted to generate or modify files within the designated run area according to the workflow rules.

A fixed launcher or equivalent execution procedure should:

- invoke the designated command;
- capture exit status;
- capture standard output;
- capture standard error;
- preserve generated files;
- record runtime duration;
- record the environment identifier;
- identify the repository or study package version.

Provider-specific code-execution environments are not used as a hidden second execution substrate when they would differ across LLM configurations.

The purpose of the standardized substrate is to isolate workflow architecture from differences in proprietary execution environments.

## 4. Human interface boundary

The human operator acts as a mechanical interface between the consumer LLM and the standardized execution substrate.

Permitted actions include:

- creating the designated consumer context;
- entering the frozen prompt;
- uploading prescribed files;
- transferring generated artifacts;
- launching the frozen execution command;
- returning permitted execution evidence to the LLM;
- opening the next designated context;
- recording operational metadata.

The human operator may not:

- edit scientific code;
- alter parameters;
- change labels or cohort rules;
- choose the preferred implementation;
- select a favorable result;
- diagnose a scientific error for the LLM;
- supply an unprescribed methodological correction;
- suppress an execution failure.

Any scientific intervention is recorded separately and handled according to the fidelity and primary endpoint rules.[5,6]

## 5. Environment specification

The reproducibility record must identify the environment at the level needed to reconstruct the reference and LLM-generated computation.

### Operating system

Record:

- operating-system family;
- major version;
- architecture;
- relevant kernel or runtime information where needed for reproducibility.

### Programming language and runtime

Record:

- Python version;
- shell or command interpreter where relevant;
- notebook or script execution system if used.

### Core packages

Record exact versions for packages that can affect results, including:

- PyTorch or the selected machine-learning framework;
- NumPy;
- SciPy;
- pandas;
- scikit-learn;
- signal-processing libraries;
- file-format readers;
- plotting or metric libraries used by the reference analysis.

The final list is determined from the actual dependency graph rather than a manually copied generic list.

### Dependency environment

The preferred record is a machine-readable environment specification such as a lock file or fully resolved package manifest.

A simple requirements list is acceptable only when it is sufficient to reconstruct the actual environment.

Both the human-readable dependency summary and the machine-readable environment record should be retained when practical.

## 6. Randomness and stochastic execution

All investigator-controlled pseudorandom operations must have an identifiable seed.

The final reproducibility record should separately identify seeds for, when applicable:

- model initialization;
- data-loader shuffling;
- training;
- reference bootstrap resampling;
- statistical randomization testing;
- sample-size simulation;
- other stochastic analyses.

The model-training protocol specifies the primary and sensitivity seeds for the biomedical reference analysis.[4]

Consumer LLM stochasticity may not be fully controllable through the interface.

If a consumer interface does not expose a sampling seed or equivalent setting, the study records that limitation rather than inventing a seed value.

Where an interface exposes settings such as temperature or another sampling control, the setting is recorded for the experimental configuration.

Repeated LLM runs are therefore treated as independent experimental attempts rather than as deterministic replicas unless the interface explicitly provides sufficient controls to justify deterministic execution.

## 7. Hardware and local execution

The execution record should identify the local hardware relevant to computational burden and result generation.

Record where applicable:

- processor;
- processor architecture;
- RAM;
- GPU model and available memory;
- storage medium relevant to execution;
- operating-system architecture.

The study does not require specialized hardware unless the frozen reference implementation demonstrates that it is necessary.

The hardware record is used to interpret execution time and resource burden. It is not used to alter the scientific endpoint.

Provider-side inference hardware remains outside the reproducibility record unless the provider exposes it.

## 8. Dataset provenance

The computational environment must be linked to the exact biomedical dataset version used for the reference analysis.

For the PTB-XL task, preserve:

- dataset name;
- dataset version;
- provider;
- access route;
- expected directory or file structure;
- metadata version;
- waveform file format;
- sampling representation;
- dataset manifest;
- integrity checks or file hashes where practical.

The study does not rely on a statement that the data were downloaded "from PhysioNet" without identifying the version and expected structure.[7]

Raw data need not be duplicated in the repository when redistribution is restricted or unnecessary.

Instead, the provenance manifest should state how an independent investigator obtains the permitted dataset version and verifies that the expected inputs are present.

## 9. Repository and source control

Every substantive computational state must be tied to a repository commit.

The reproducibility record should preserve:

- repository name;
- branch where relevant;
- commit SHA;
- relevant file paths;
- uncommitted-change status at execution;
- release or tag identifier when used.

An execution that depends on uncommitted changes should not be represented as if it came from a clean commit.

Generated analysis files should be retained with the run identifier rather than replacing the source artifact used in an earlier attempt.

The commit identifier is therefore part of the provenance record, not merely a convenience for repository browsing.

## 10. Execution logging

Each execution should produce a machine-readable or otherwise structured log containing, at minimum:

| Field | Description |
|---|---|
| Run ID | Unique experimental identifier |
| Configuration ID | LLM configuration |
| Workflow condition | W0 through W5 |
| Access epoch | Consumer configuration state |
| Environment ID | Computational environment version |
| Repository commit | Source state used |
| Dataset version | Biomedical input version |
| Input manifest | Files supplied to execution |
| Command | Exact prescribed command |
| Exit status | Process completion state |
| Runtime | Elapsed execution duration |
| Standard output | Captured execution output |
| Standard error | Captured execution errors |
| Output manifest | Files generated by execution |
| Artifact hashes | Integrity identifiers where practical |
| Seed records | Investigator-controlled stochastic settings |
| Intervention flag | Scientific intervention indicator |
| Terminal state | Outcome classification |

The log must be generated from the execution process whenever possible.

Manual transcription should be minimized because it creates another source of discrepancy between what happened and what was recorded.[3]

## 11. Artifact integrity

Important study artifacts should have stable integrity identifiers when practical.

Suitable artifacts include:

- frozen protocol files;
- prompt files;
- handoff templates;
- validator code;
- reference implementation;
- environment manifests;
- run manifests;
- generated analysis scripts;
- result files;
- machine-readable evaluation records.

Cryptographic hashes may be used to establish that a file inspected during adjudication is the same file produced during execution.

Hashing is an integrity mechanism, not a substitute for semantic versioning or provenance.

## 12. LLM interaction provenance

The prompt and interaction registry will hold the detailed conversational provenance.

This reproducibility document should therefore link to, rather than duplicate, the following:

- prompt version;
- condition;
- context sequence;
- files exposed;
- handoff artifacts;
- model identity;
- access epoch;
- execution evidence returned to the LLM;
- repair events;
- terminal response.

Full conversational transcripts are retained only where they are necessary for audit and reporting.

The registry should distinguish the frozen experimental prompt from the resulting transcript.

A generated response cannot retroactively become part of the prespecified prompt.

## 13. Information-isolation controls

The reproducibility record must document whether the LLM had access to information outside the prescribed study package.

For primary runs, record the state of:

- web access;
- retrieval;
- memory;
- personalization;
- connected applications;
- external connectors;
- other persistent study-relevant state.

A configuration that cannot provide the required isolation should be excluded or separately defined before pooling, consistent with the consumer eligibility specification.[8]

This record is essential because an identical prompt does not imply an identical information environment.

## 14. Version drift and access epochs

Consumer LLM services can change during the study.

A new access epoch is required when a material change affects:

- model identity;
- model family;
- available tools;
- context capacity;
- free-tier limits;
- memory or persistence;
- retrieval;
- code execution;
- file handling;
- another feature capable of affecting the experimental workflow.

Each epoch record should state:

- configuration ID;
- access month;
- previous epoch if applicable;
- observed change;
- evidence source;
- affected capabilities;
- pooling decision.

Runs from distinct epochs are not silently combined.

This is especially important for LLM studies because model configurations are temporal experimental objects rather than permanently fixed products.[1]

## 15. Reproducibility levels

The study distinguishes three levels of reproducibility.

### Computational reproduction

The same source files, environment, inputs and execution procedure produce the same or appropriately consistent computational outputs.

### Workflow reproduction

A second investigator can reconstruct the LLM configuration, prompts, context structure, execution substrate and terminal workflow from the archived study package.

### Independent replication

A new execution performed independently using the preserved specification and environment reaches the defined evaluation state without relying on the original investigator's scientific intervention.

The independent replication is a later study component.

It is not claimed merely because the repository contains source code.

## 16. Environment validation before primary collection

Before primary LLM collection, the standardized execution environment must pass a reference validation sequence.

The validation should establish that:

1. the reference dataset can be located and loaded;
2. the prescribed preprocessing executes;
3. the reference model can be initialized;
4. training can be completed under the frozen configuration;
5. evaluation metrics can be calculated;
6. the primary estimand can be reproduced;
7. bootstrap and other statistical procedures execute;
8. the execution log captures the required provenance;
9. rerunning the reference workflow under the same environment produces results within the empirically established reference variability.

The final numerical reference-agreement criteria are determined only after the reference execution and independent reimplementation sequence described in the reference protocol.[4]

## 17. Reproducibility and reference agreement

Reproducibility should not be confused with numerical identity.

A rerun can reproduce the workflow while differing numerically because of stochastic optimization, hardware, library behavior, or other controlled sources of variation.

The reference analysis therefore uses the empirical variability observed during its own repeat and independent implementations to establish the final numerical comparison envelope.[4]

This avoids treating an arbitrary decimal difference as evidence of failed reproducibility.

## 18. Evidence preservation

The study retains evidence needed to reconstruct major decisions and executions.

The evidence set should include, as applicable:

- literature sources used to determine methodological choices;
- provider documentation used for access decisions;
- dataset documentation;
- frozen protocol versions;
- prompt and interaction versions;
- environment specifications;
- source code;
- run manifests;
- execution logs;
- output artifacts;
- fidelity adjudication records;
- protocol change records;
- analysis scripts;
- simulation code and outputs after the sample-size pass.

The repository literature layer remains the record of why methodological choices were made.

The execution archive remains the record of what was actually run.

These functions should not be merged.

## 19. FAIR and reproducible software principles

The computational archive should be organized so that software and associated metadata can be found, retrieved, understood, versioned and reused where permitted.

FAIR4RS is relevant to the research software created for this study, particularly provenance, versioning, identifiers, documentation and qualified references to dependencies.[2]

The FAIR principles are not treated as a claim that every repository artifact is automatically FAIR.

The study applies the principles that are practical for the research software and data objects actually generated.

Reproducible computational research guidance similarly emphasizes retaining the full analysis workflow and the program versions, parameters and inputs that materially affect a result.[3]

## 20. Reporting and release

The final reporting package should identify the computational environment sufficiently for a reader to understand how the results were produced.

At minimum, the release should include:

- study protocol version;
- reference implementation version;
- dataset version and provenance;
- environment manifest;
- hardware summary;
- software versions;
- repository commit;
- random seeds where controlled;
- LLM configuration and access epoch;
- prompt and interaction registry;
- execution logs;
- output manifests;
- fidelity evaluation records;
- resource records;
- protocol changes.

Where raw data, transcripts or provider outputs cannot be redistributed, the release should provide the strongest permitted provenance record and explain the access restriction.

## 21. Scope of claims

This reproducibility plan does not claim that:

- a consumer LLM can be frozen permanently;
- hidden provider-side computation can be reconstructed;
- every future investigator will receive the same consumer interface;
- the same numerical result must occur bit-for-bit across all hardware;
- repository publication alone proves reproducibility;
- a successful rerun establishes clinical validity.

The study instead defines a traceable computational and workflow record that makes the observed experiment inspectable and independently reproducible within the documented configuration.

## 22. Evidence basis and investigator-defined components

The use of explicit workflow provenance, software and dependency recording, input and parameter tracking, and preservation of execution context is supported by reproducible computational research guidance.[2,3]

TRIPOD-LLM provides the LLM-specific reporting basis for model identity, prompts, evaluation setting, human oversight and reproducibility.[1]

The distinction between research software and software used in research, together with provenance, versioning and reusability principles, is informed by FAIR4RS.[2]

The exact environment fields, run schema, artifact-hash policy, execution-substrate interface, access-epoch implementation and independent-reproduction procedure are investigator-defined components of this study.

## References

1. Gallifant J, Afshar M, Ameen S, et al. The TRIPOD-LLM reporting guideline for studies using large language models. Nat Med. 2025;31(1):60-69. doi:10.1038/s41591-024-03425-5.

2. Barker M, Chue Hong NP, Katz DS, et al. Introducing the FAIR Principles for research software. Sci Data. 2022;9:622. doi:10.1038/s41597-022-01710-x.

3. Sandve GK, Nekrutenko A, Taylor J, Hovig E. Ten Simple Rules for Reproducible Computational Research. PLoS Comput Biol. 2013;9(10):e1003285. doi:10.1371/journal.pcbi.1003285.

4. Reference Biomedical Analysis Protocol. study/08 REFERENCE BIOMEDICAL ANALYSIS PROTOCOL.md. Study repository.

5. LLM Workflow Experimental Protocol. study/09 LLM WORKFLOW EXPERIMENTAL PROTOCOL.md. Study repository.

6. Scientific Fidelity Evaluation Framework. study/11 SCIENTIFIC FIDELITY EVALUATION FRAMEWORK.md. Study repository.

7. Wagner P, Strodthoff N, Bärs R, et al. PTB-XL, a large publicly available electrocardiography dataset. Sci Data. 2020;7:154. doi:10.1038/s41597-020-0495-6.

8. Consumer LLM Eligibility Specification. study/07 CONSUMER LLM ELIGIBILITY SPECIFICATION.md. Study repository.
