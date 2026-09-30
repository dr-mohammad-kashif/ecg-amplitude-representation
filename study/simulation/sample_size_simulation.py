from __future__ import annotations

import argparse
import math
from pathlib import Path

import numpy as np
import pandas as pd
from scipy.stats import binom, norm


ALPHA = 0.05
MIN_CONFIGURATIONS = 3
EFFECT_TARGET = 0.25
HETEROGENEITY_HALF_RANGE = 0.05
BASELINE_ALTERNATIVE = (0.35, 0.50, 0.65)
BASELINE_NULL = (0.35, 0.50, 0.65, 0.80)
RHO_GRID = (0.0, 0.25)
BLOCK_CANDIDATES = (20, 25)
SIMULATIONS_PER_SCENARIO = 3000


def exact_signflip_pvalue(total_difference: int, nonzero_blocks: int) -> float:
    """Exact two-sided sign-flip p-value for binary block differences."""
    if nonzero_blocks == 0:
        return 1.0

    observed = abs(int(total_difference))
    lower_tail = math.ceil((observed + nonzero_blocks) / 2)
    upper_tail = math.floor((nonzero_blocks - observed) / 2)

    p = (
        binom.sf(lower_tail - 1, nonzero_blocks, 0.5)
        + binom.cdf(upper_tail, nonzero_blocks, 0.5)
    )
    return float(min(1.0, p))


def simulate_dataset(
    rng: np.random.Generator,
    configurations: int,
    blocks_per_configuration: int,
    baseline_w1: float,
    effect: float,
    rho: float,
    heterogeneity_half_range: float,
) -> float:
    """Simulate one study and return the exact randomization-test p-value."""
    total_difference = 0
    nonzero_blocks = 0

    for _ in range(configurations):
        configuration_effect = effect + rng.uniform(
            -heterogeneity_half_range,
            heterogeneity_half_range
        )
        configuration_effect = max(
            -baseline_w1 + 1e-6,
            min(configuration_effect, 1.0 - baseline_w1 - 1e-6),
        )

        common = rng.standard_normal(blocks_per_configuration)
        first = rng.standard_normal(blocks_per_configuration)
        second = rng.standard_normal(blocks_per_configuration)

        if rho > 0:
            w1_latent = np.sqrt(rho) * common + np.sqrt(1 - rho) * first
            w2_latent = np.sqrt(rho) * common + np.sqrt(1 - rho) * second
        else:
            w1_latent = first
            w2_latent = second

        w1 = w1_latent < norm.ppf(baseline_w1)
        w2 = w2_latent < norm.ppf(baseline_w1 + configuration_effect)

        difference = w2.astype(np.int8) - w1.astype(np.int8)
        total_difference += int(difference.sum())
        nonzero_blocks += int(np.count_nonzero(difference))

    return exact_signflip_pvalue(total_difference, nonzero_blocks)


def run_scenarios(
    blocks_per_configuration: int,
    *,
    null: bool,
    seed: int,
    simulations: int,
    configurations: int = MIN_CONFIGURATIONS,
) -> list[dict]:
    """Run the prespecified scenario grid."""
    rng = np.random.default_rng(seed)
    baselines = BASELINE_NULL if null else BASELINE_ALTERNATIVE
    effect = 0.0 if null else EFFECT_TARGET
    heterogeneity = 0.0 if null else HETEROGENEITY_HALF_RANGE
    rows: list[dict] = []

    for baseline in baselines:
        for rho in RHO_GRID:
            p_values = np.array(
                [
                    simulate_dataset(
                        rng,
                        configurations=configurations,
                        blocks_per_configuration=blocks_per_configuration,
                        baseline_w1=baseline,
                        effect=effect,
                        rho=rho,
                        heterogeneity_half_range=heterogeneity,
                    )
                    for _ in range(simulations)
                ],
                dtype=float,
            )

            rows.append(
                {
                    "blocks_per_configuration": blocks_per_configuration,
                    "scenario": "null" if null else "alternative",
                    "baseline_w1_completion": baseline,
                    "rho": rho,
                    "target_effect": effect,
                    "heterogeneity_half_range": heterogeneity,
                    "configurations": configurations,
                    "simulations": simulations,
                    "rejection_rate_alpha_0_05": float(
                        np.mean(p_values < ALPHA)
                    ),
                    "mean_p_value": float(np.mean(p_values)),
                }
            )

    return rows


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("sample_size_simulation_results.csv"),
    )
    args = parser.parse_args()

    rows: list[dict] = []

    for blocks, seed in ((20, 271828), (25, 314159)):
        rows.extend(
            run_scenarios(
                blocks,
                null=False,
                seed=seed,
                simulations=SIMULATIONS_PER_SCENARIO,
            )
        )

    rows.extend(
        run_scenarios(
            25,
            null=True,
            seed=271829,
            simulations=SIMULATIONS_PER_SCENARIO,
        )
    )

    result = pd.DataFrame(rows)
    result.to_csv(args.output, index=False)

    alternative = result[result["scenario"] == "alternative"]
    selected = alternative[
        alternative["blocks_per_configuration"] == 25
    ]

    min_power = selected["rejection_rate_alpha_0_05"].min()
    null25 = result[result["scenario"] == "null"][
        "rejection_rate_alpha_0_05"
    ].max()

    print(f"Minimum simulated power at 25 blocks/configuration: {min_power:.4f}")
    print(f"Maximum simulated type I error at 25 blocks/configuration: {null25:.4f}")


if __name__ == "__main__":
    main()
