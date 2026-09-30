# Sample Size Simulation

Status: Completed design-support simulation
Version: 0.1
Month: September 2026
Study phase: Preprotocol

## 1. Purpose

The primary endpoint is a binary run-level reference-faithful completion outcome. The primary comparison is W1 versus W2, with one scheduled W1 attempt and one scheduled W2 attempt per randomized block within each eligible LLM configuration.

The number of primary blocks per configuration was therefore determined by simulation rather than by a copied replication convention.

The simulation was designed to answer a specific question:

> How many W1/W2 blocks per configuration are required for reasonable power to detect a prespecified 25 percentage-point difference in completion probability under a minimum of three eligible LLM configurations?

The 25 percentage-point effect is an investigator-defined planning scenario. It is not presented as a clinically meaningful threshold or as an effect established by prior LLM workflow studies.

## 2. Primary decision rule

The smallest candidate block count was selected that satisfied both conditions:

1. Under the null scenarios, the simulated two-sided randomization test maintained a rejection rate no greater than 0.05 in the evaluated grid.
2. Under the alternative scenarios, the minimum simulated power was at least 0.80 for a 25 percentage-point W2 minus W1 completion effect.

The primary simulation assumes three eligible configurations because three is the minimum configuration count required for a confirmatory primary comparison in this study.

If more than three configurations qualify, the same block allocation is retained for each configuration. The additional configurations therefore contribute information without requiring the study to change its primary block rule after eligibility is observed.

## 3. Scenario grid

### Alternative scenarios

The simulations used:

- three eligible configurations;
- 20 or 25 randomized W1/W2 blocks per configuration;
- W1 completion probabilities of 0.35, 0.50 and 0.65;
- W2 minus W1 completion effect of 0.25;
- configuration-specific effect heterogeneity sampled uniformly within +/-0.05 around the target effect;
- within-block correlation values of 0 and 0.25;
- 3,000 simulation datasets for each scenario.

The completion probability is the marginal probability of reference-faithful completion. It therefore already includes all mechanisms that lead to terminal noncompletion, including scientific, execution, resource and unauthorized-intervention outcomes.

### Null scenarios

The null simulations used:

- three eligible configurations;
- 25 blocks per configuration;
- W1 completion probabilities of 0.35, 0.50, 0.65 and 0.80;
- zero workflow effect;
- within-block correlation values of 0 and 0.25;
- 3,000 simulation datasets for each scenario.

## 4. Test used in simulation

The primary inferential design uses randomized assignment of W1 and W2 within each block.

For the simulation, the null distribution was evaluated exactly by sign-flipping the nonzero within-block W2 minus W1 differences. Because the primary endpoint is binary, each block difference is -1, 0 or 1. Conditional on the observed number of nonzero block differences, the sign-flip distribution is binomial.

This avoids Monte Carlo approximation of the randomization p-value in the sample-size simulation.

The planned primary study analysis will use the corresponding block-randomization procedure with a fixed Monte Carlo implementation when unequal completed block counts or other operational deviations prevent the simple exact binomial representation.

## 5. Results

| Blocks per configuration | Minimum simulated power across alternative scenarios | Maximum simulated type I error across null scenarios |
|---:|---:|---:|
| 20 | 0.708 | Not evaluated in the null grid |
| 25 | 0.820 | 0.040 |

At 20 blocks per configuration, the minimum simulated power was below the prespecified 0.80 criterion.

At 25 blocks per configuration, the minimum simulated power was 0.820 across the evaluated alternative scenarios. The maximum simulated null rejection rate was 0.040 across the evaluated null scenarios.

The 25-block design therefore satisfies the prespecified selection rule in the evaluated scenario grid.

## 6. Primary allocation decision

The primary study will use:

> **25 randomized W1/W2 blocks per eligible LLM configuration.**

Each block contains exactly:

- one W1 attempt;
- one W2 attempt.

The order of W1 and W2 is randomized within the block before the run begins.

Thus, the minimum primary allocation is:

- 3 eligible configurations;
- 25 blocks per configuration;
- 50 W1/W2 runs per configuration;
- 150 primary W1/W2 runs in total.

The total increases linearly with the number of eligible configurations.

If fewer than three configurations pass the final consumer-eligibility and direct-feasibility audit, the confirmatory primary comparison will not proceed. The remaining observations may be reported descriptively rather than being used to support the prespecified primary estimand.

## 7. Interpretation of the simulation

The selected allocation is designed around a 25 percentage-point completion difference. Smaller effects will have lower power.

The simulation does not establish that a 25 percentage-point difference is likely to occur. It establishes the operating characteristics of the chosen block design under explicitly stated planning scenarios.

Completion probabilities, effect sizes, dependence values and effect heterogeneity in this simulation are investigator-defined scenarios. They are not empirical estimates of the forthcoming LLM experiment.

The primary sample-size decision must not be changed after primary outcomes are observed.

## 8. Reproducibility

The simulation is reproduced by:

- [sample_size_simulation.py](simulation/sample_size_simulation.py)

The simulation writes a machine-readable CSV containing the scenario grid and simulated operating characteristics.

The simulation uses deterministic random-number seeds defined in the source code.

## References

1. Statistical Analysis Plan. current-study/12 STATISTICAL ANALYSIS PLAN.md. Study repository; 2026.
2. LLM Workflow Experimental Protocol. current-study/09 LLM WORKFLOW EXPERIMENTAL PROTOCOL.md. Study repository; 2026.
3. Scientific Workflow and Statistical Analysis documents. current-study/09 LLM WORKFLOW EXPERIMENTAL PROTOCOL.md and current-study/12 STATISTICAL ANALYSIS PLAN.md. Study repository; 2026.

## Evidence status

The block-based simulation strategy follows the prespecified statistical architecture already established for the study.[1,2]

The baseline completion probabilities, target workflow effect, heterogeneity range, within-block dependence values, candidate block counts and selection criterion are investigator-defined simulation scenarios.

The simulated values are computed results from the supplied code.
