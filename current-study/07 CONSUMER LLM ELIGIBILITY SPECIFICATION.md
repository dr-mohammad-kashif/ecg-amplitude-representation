# Consumer LLM Eligibility Specification

Status: Working specification
Version: 0.1
Date: 30 September 2026
Study phase: Preprotocol

## Scope

This document defines the population of large language model configurations that can enter the primary experiment.

The study does not define its population as all LLMs, all open models, all small language models, or all systems with a nominally free option.

The intended population is narrower.

> General purpose LLM systems that an ordinary individual can access through a public consumer-facing online interface at zero monetary cost, with every capability required for the prespecified workflow available within that free configuration.

This is an investigator-defined study boundary. It is not a claim that free consumer access is scientifically superior to paid, local, API, or institutional access.

The purpose of the boundary is to make the resource-access population explicit and reproducible.

## 1. Free access is a property of a configuration

The unit of eligibility is not simply the underlying model.

A system is represented as:

$$
\text{provider}
+
\text{consumer interface}
+
\text{plan}
+
\text{model presentation}
+
\text{available capabilities}
+
\text{region}
+
\text{access date}
$$

A provider can expose the same model through several routes with different tools, limits, or payment requirements. Those routes cannot be treated as interchangeable.

Current provider documentation illustrates this distinction. OpenAI documents a Free tier with file uploads and data analysis subject to separate limits.[1] Google documents file upload and analysis in Gemini without an AI plan, with a smaller context window and lower limits than paid plans.[2,3] Anthropic lists a $0 Free consumer plan and separately lists additional capabilities and higher usage on paid plans; its current documentation also states that code execution and file creation are available to Free users.[4,5] Mistral lists a Free consumer plan with limited messages, web searches, and coding sessions and separately describes paid and API services.[6]

These provider facts are time-sensitive. The experimental record must therefore preserve the exact access state rather than treating the provider name as the experimental condition.

## 2. Eligibility domains

A candidate configuration must pass every mandatory domain before it can enter the primary model pool.

### E1. Public consumer accessibility

The system must be directly obtainable through an ordinary public consumer-facing web or mobile interface.

It must not require:

- institutional deployment;
- enterprise access;
- university access;
- researcher enrollment;
- developer approval;
- special invitation;
- provider-granted research access.

A normal consumer account is permitted.

### E2. Zero monetary cost

The specific configuration used in the experiment must cost the study user $0.

The following do not qualify:

- paid subscriptions;
- one-time purchases;
- mandatory add-ons;
- paid seats;
- hidden minimum spending requirements;
- required purchases of external services.

A free tier with usage limits does qualify under the monetary criterion.

The study defines "free" as zero monetary payment, not unlimited access.

### E3. No API route

The primary interaction must occur through the public consumer interface.

The following are excluded from the primary population:

- provider APIs;
- cloud-hosted model APIs;
- third-party API aggregators;
- free promotional API credits;
- pay-as-you-go developer access.

This is an investigator-defined boundary. It is intended to study what an ordinary user can obtain through the ordinary consumer product rather than what a technically sophisticated user can programmatically obtain through a developer platform.

### E4. No institutional or special entitlement

Access obtained through an organization, university, employer, hospital, laboratory, government program, enterprise account, student entitlement, or researcher allocation is excluded.

A provider-sponsored scientist program is not equivalent to ordinary consumer access.

The study therefore separates public availability from personally available access.

### E5. No free trial or promotional pathway

Temporary access that depends on a trial, promotional campaign, launch offer, gifted subscription, or free introductory credit does not qualify.

The configuration must be available as an ordinary $0 consumer route without requiring entry into a paid access pathway.

This also excludes a temporary free API credit balance.

### E6. General purpose model

The system must be a general purpose conversational LLM.

It must not be selected because it is a specialized biomedical model, medical agent, diagnostic model, or domain-specific system created specifically for the study task.

A general purpose model may still perform biomedical analysis. The exclusion concerns the intended model population, not the subject matter of a particular prompt.

### E7. No local deployment or SLM substitution

The primary population excludes:

- locally hosted open-weight models;
- downloaded model weights;
- small language models selected for local execution;
- edge-optimized models;
- local medical language models;
- self-hosted inference servers.

This is an investigator-defined boundary.

The study is not asking for the smallest model that can perform the analysis. It is asking what an ordinary user can obtain from a mainstream general purpose online consumer service without payment.

### E8. Essential capabilities must themselves be free

A free chat interface is not sufficient.

Every capability required by the final prespecified workflow must be available without payment.

Depending on the frozen protocol, required capabilities may include:

- file upload;
- handling of the study files;
- code generation;
- code execution or another approved execution route;
- sufficient context for the assigned stage;
- repeated interaction;
- access to generated analysis artifacts;
- ability to inspect execution outputs;
- ability to continue the workflow without a paid upgrade.

If any essential capability requires a paid tier, the configuration is excluded from the primary population even when the underlying model is also accessible through a free chat route.

This rule is central to the study.

The population is therefore not "models with free chat access."

It is "consumer configurations through which the complete prespecified analytical workflow can be carried out at zero monetary cost."

Current provider documentation demonstrates why this distinction is necessary. OpenAI documents data analysis and file uploads within the Free tier while applying separate usage limits.[1] Google documents file upload and analysis without an AI plan and higher capabilities on paid plans.[2,3] Anthropic documents code execution and file creation for Free users while reserving some additional products and higher usage for paid plans.[4,5] Mistral describes limited coding sessions and document upload on its Free consumer plan while separately listing paid plans and API pricing.[6]

### E9. Account requirement and payment instrument

A normal consumer account is permitted.

The study does not require anonymous access because requiring anonymity would introduce an artificial restriction that is not central to the research question.

However, creation of the qualifying account must not require:

- a paid subscription;
- a credit-card or debit-card payment instrument as a condition of entering the free configuration;
- a bundled paid service;
- an institutional payment relationship.

The relevant criterion is ordinary account creation followed by ordinary $0 access.

### E10. Independent public obtainability

The same qualifying configuration must be obtainable by a new ordinary user who meets the provider's ordinary consumer requirements.

Personal access is not sufficient evidence.

A configuration does not qualify merely because the investigator happens to have access to it through a private invitation, previous purchase, special promotion, or individual exception.

This criterion protects the distinction between personal accessibility and public accessibility.

### E11. Region and date

Availability must be documented for the actual study region and access date.

Each access record must include:

- country or region;
- verification date;
- consumer product URL;
- account type;
- plan;
- displayed model name;
- available tools;
- relevant usage limits;
- any regional restrictions.

The study must not generalize from a configuration that is free in one jurisdiction to global free availability.

### E12. Model identity and access epoch

The exact model identity should be recorded whenever the interface exposes it.

When a consumer interface presents only a default, automatic, or otherwise dynamic model selection, the configuration remains eligible only if that dynamic behavior can be documented sufficiently for the run to remain interpretable.

The access record must therefore retain:

- provider;
- interface;
- displayed model identity;
- model family if visible;
- model or system version if visible;
- access tier;
- access date;
- relevant configuration settings.

A provider or configuration change that alters model identity, tool availability, context capacity, or another feature relevant to the primary experiment creates a new access epoch unless equivalence can be justified before pooling runs.

This requirement follows from the reproducibility concerns addressed by TRIPOD-LLM, which emphasizes transparent reporting of LLM identity, version, prompting, evaluation settings, and the temporal context of LLM evaluation.[7]

### E13. No hidden persistence or uncontrolled information exposure

Primary runs must not receive information from outside the prespecified study package.

The intended primary configuration should therefore have, where technically possible:

- memory disabled;
- personalization disabled;
- connected applications disabled;
- external retrieval disabled;
- web search disabled;
- uncontrolled connectors disabled;
- a new conversation or context for each designated fresh-context stage;
- no previous study artifacts available to the model.

The purpose is not to characterize these features as unsafe or undesirable.

The purpose is to prevent information exposure from differing between workflow conditions.

A provider that cannot disable a relevant persistence or retrieval mechanism must be excluded from the primary comparison or assigned to a separately defined configuration in which the exposure is identical and explicitly recorded.

### E14. No paid external agent or orchestration dependency

The primary workflow cannot depend on a paid agent product, paid orchestration service, paid external research framework, or other infrastructure that is not part of the qualifying $0 consumer route.

A free model wrapped inside a paid agent system does not qualify.

The consumer LLM may interact with the study's standardized execution substrate because that substrate is part of the experimental design rather than a provider-specific paid agent product.

The distinction is:

1. the underlying LLM;
2. the consumer interface used to access it;
3. the standardized study workflow and execution substrate.

Only the first two are part of the consumer access eligibility determination.

### E15. Primary-run feasibility under free limits

A candidate must expose all essential capabilities required by the prespecified primary run.

After the workflow protocol and interaction budget are frozen, the study must verify that the qualifying free configuration can execute a complete primary run without requiring a paid upgrade.

This is separate from the existence of a nominal free feature.

For example, a provider may expose code execution for free but impose a usage limit that prevents completion of the prespecified workflow. In that case the configuration does not satisfy the primary-run feasibility criterion for that protocol.

The distinction is therefore:

$$
\text{capability available at }\$0
\neq
\text{complete primary run feasible at }\$0
$$

A quota-induced termination is recorded as a resource or access failure, not silently reclassified as a scientific failure.

## 3. Free limits are part of the resource envelope

The study does not require unlimited free use.

Free configurations may impose:

- message limits;
- rolling limits;
- file upload limits;
- context limits;
- execution limits;
- temporary throttling;
- rate limits;
- storage limits.

These limitations are part of the observable resource environment.

They must be recorded rather than bypassed through paid upgrades.

For example, OpenAI currently documents separate limits for file uploads and data analysis for Free users.[1] Google documents lower context capacity and lower usage limits without an AI plan than on paid plans.[2,3] Anthropic's Free plan is explicitly limited in usage.[4,5] Mistral likewise describes limited messages, web searches, and coding sessions on its Free plan.[6]

A free-tier limit is therefore not an inconvenience to work around. It is part of the study condition.

## 4. Capability audit versus model selection

The eligibility specification does not itself decide the final model set.

Candidate systems are first screened against the eligibility domains.

Eligible candidates then undergo a direct interface audit at the intended study date and region.

The final model pool is frozen only after:

1. provider documentation has been checked;
2. the consumer interface has been inspected;
3. required capabilities have been demonstrated;
4. relevant limits have been recorded;
5. memory and external information exposure have been characterized;
6. the exact configuration has been assigned an access epoch;
7. primary-run feasibility has been checked after the workflow budget is frozen.

This prevents model selection from being driven by early performance observations.

No performance comparison may be used as an eligibility criterion.

## 5. Access registry

Every included configuration must receive an access record before primary data collection.

The minimum record is:

| Field | Required record |
|---|---|
| Configuration ID | Stable study identifier |
| Provider | Organization |
| Consumer product | Web or mobile product |
| Interface | Exact interface used |
| Region | Country or region |
| Access date | Date and time of verification |
| Account type | Ordinary consumer account |
| Plan | Free configuration name |
| Displayed model | Exact name shown by interface |
| Model version | Version if visible |
| Payment required | Yes or no |
| Payment instrument required | Yes or no |
| API required | Yes or no |
| Institutional entitlement | Yes or no |
| Researcher entitlement | Yes or no |
| Student entitlement | Yes or no |
| Trial or promotion | Yes or no |
| Required capabilities free | Pass or fail by capability |
| File limits | Observed or documented limit |
| Context limit | Observed or documented limit |
| Execution capability | Available, unavailable, or uncertain |
| Memory state | On, off, unavailable, or uncertain |
| Personalization state | On, off, unavailable, or uncertain |
| Retrieval/web state | On, off, unavailable, or uncertain |
| Connectors | Present, absent, or unavailable |
| Usage limits | Documented and observed limits |
| Primary-run feasibility | Pass, fail, or uncertain |
| Evidence URLs | Official supporting sources |
| Configuration notes | Relevant observations |

An access record is incomplete when an essential field remains unknown.

Unknown should not be silently converted to "no."

## 6. Eligibility decision states

Each candidate receives one of four states.

### Eligible

All mandatory domains pass and primary-run feasibility is confirmed for the frozen workflow.

### Provisionally eligible

All currently testable domains pass, but one or more dynamic properties require confirmation after the final workflow budget or at the first primary access check.

### Ineligible

At least one mandatory domain fails.

### Indeterminate

A mandatory domain cannot be established from provider documentation or direct observation.

Indeterminate configurations do not enter the primary comparison.

## 7. Handling provider changes

Consumer AI services can change model identity, tools, limits, and interfaces without preserving the same experimental configuration.

The study therefore uses access epochs.

If a relevant change occurs, the configuration receives a new epoch identifier.

The change record must state:

- what changed;
- when it changed;
- which runs are affected;
- whether previous and new configurations can be considered equivalent;
- whether runs should be analyzed separately.

The study must never silently pool runs across a known material configuration change.

## 8. Failure and termination rules

A primary run can terminate for several distinct reasons.

### Scientific or protocol failure

The workflow violates the locked biomedical analysis.

### Execution failure

Required code or analysis cannot be executed because of an implementation or runtime problem.

### Resource or access failure

The free configuration reaches a quota, file, context, service, or other access limitation.

### Unauthorized human scientific intervention

A human changes the scientific analysis outside the prespecified permitted actions.

These outcomes remain separately classified even though only some can produce a completed analysis.

A resource-limited run is therefore not "rescued" by upgrading the account or switching to a paid feature.

## 9. Why the free-access population matters

The strict free-access boundary is scientifically useful because it defines the population of systems available to an ordinary user without payment, institutional affiliation, researcher access, local deployment, or developer infrastructure.

Recent research has already evaluated free public consumer LLMs, so free access by itself is not a novelty claim.

The contribution must instead depend on what is tested within that population.

The active study therefore distinguishes:

> free consumer access as a population boundary

from:

> workflow architecture as the experimental intervention.

This prevents the paper from claiming that free LLM evaluation has never been studied while preserving the accessibility question as a real methodological constraint.

## 10. Provider status at the current audit

Current official documentation identifies several plausible candidates for direct eligibility testing.

| Provider | Current official evidence | Initial status |
|---|---|---|
| OpenAI | Free tier with data analysis and file uploads; separate tool limits[1] | Candidate |
| Google | Gemini without an AI plan supports file upload and analysis; lower context and usage limits than paid tiers[2,3] | Candidate |
| Anthropic | Claude Free at $0; current documentation lists code execution and file creation for Free users[4,5] | Candidate |
| Mistral | Free consumer plan with limited messages, web searches, coding sessions, and document upload[6] | Candidate |

These are candidate configurations, not a frozen inclusion list.

The final status requires direct access testing in the study region and under the exact workflow configuration.

No provider is included or excluded on performance grounds.

## 11. Evidence classification

The following are direct evidence facts.

1. Current provider plans, capabilities, and documented limits come from official provider documentation.[1-6]
2. LLM research reporting standards call for transparent recording of model identity, prompting, evaluation setting, and temporal configuration.[7]

The following are investigator-defined study boundaries.

1. Excluding API access.
2. Excluding local models and small language models.
3. Excluding institutional, researcher, student, and special-access routes.
4. Excluding trials and promotional access.
5. Requiring every essential capability to be free.
6. Requiring independent public obtainability.
7. Requiring no payment instrument for the qualifying free configuration.
8. Requiring controlled persistence, retrieval, and connector state.
9. Treating access-epoch changes as configuration changes.
10. Requiring primary-run feasibility under the frozen free resource envelope.

These choices are not presented as universal definitions of "free AI." They define the population needed for this experiment.

## 12. Required checks before primary collection

Before any primary LLM run is counted, the study must have:

1. a completed access registry entry;
2. provider documentation supporting the free configuration;
3. direct interface verification;
4. confirmation of every essential free capability;
5. confirmation of region and access date;
6. confirmation that no payment instrument or special entitlement is required;
7. a recorded model identity or dynamic-configuration designation;
8. controlled memory, personalization, retrieval, and connector state;
9. a frozen interaction and resource budget;
10. confirmed primary-run feasibility at $0;
11. an access epoch identifier;
12. an archived copy or stable reference to the evidence used for eligibility.

Primary collection must not begin for a configuration whose eligibility remains indeterminate.

## References

1. OpenAI. ChatGPT Free Tier FAQ [Internet]. San Francisco: OpenAI; 2026 [cited 2026 Sep 30]. Available from: https://help.openai.com/en/articles/9275245-chatgpt-free-tier-faq

2. Google. Gemini Apps limits & upgrades for Google AI subscribers [Internet]. Mountain View: Google; 2026 [cited 2026 Sep 30]. Available from: https://support.google.com/gemini/answer/16275805

3. Google. Upload and analyse files in Gemini Apps [Internet]. Mountain View: Google; 2026 [cited 2026 Sep 30]. Available from: https://support.google.com/gemini/answer/14903178

4. Anthropic. Plans & pricing: Claude [Internet]. San Francisco: Anthropic; 2026 [cited 2026 Sep 30]. Available from: https://claude.com/pricing

5. Anthropic. Create and edit files with Claude [Internet]. San Francisco: Anthropic; 2026 [cited 2026 Sep 30]. Available from: https://support.claude.com/en/articles/12111783-create-and-edit-files-with-claude

6. Mistral AI. Pricing [Internet]. Paris: Mistral AI; 2026 [cited 2026 Sep 30]. Available from: https://mistral.ai/pricing/

7. Gallifant J, Afshar M, Ameen S, Aphinyanaphongs Y, Chen S, Cacciamani G, et al. The TRIPOD-LLM reporting guideline for studies using large language models. Nat Med. 2025;31(1):60-69. doi:10.1038/s41591-024-03425-5.

## Evidence status

References 1 through 7 were checked against current official provider documentation or the publisher record during the 30 September 2026 access audit.

The candidate provider table is not a final model selection. Direct testing and primary-run feasibility remain required before any configuration is entered into the experimental model pool.

The eligibility specification is intentionally strict. Its purpose is to prevent a nominally free model, paid agent wrapper, research allocation, or partially free workflow from being counted as ordinary zero-cost consumer access.
