from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt


def generate_samples(distribution: str, n: int, rng: np.random.Generator) -> np.ndarray:
    if distribution == "uniform":
        return rng.uniform(0.0, 1.0, size=n)
    elif distribution == "exponential":
        return rng.exponential(scale=1.0, size=n)
    elif distribution == "pareto_a3":
        return rng.pareto(a=3.0, size=n) + 1  # scale xm = 1
    elif distribution == "pareto_a15":
        return rng.pareto(a=1.5, size=n) + 1  # scale xm = 1
    elif distribution == "cauchy":
        return rng.standard_cauchy(size=n)
    else:
        raise ValueError(f"Unsupported distribution: {distribution}")


def get_true_mean(distribution: str) -> float | None:
    return {
        "uniform": 0.5,
        "exponential": 1.0,
        "pareto_a3": 1.5,
        "pareto_a15": None,
        "cauchy": None
    }.get(distribution, None)


def run_slln(distribution: str, n: int = 10000, seed: int = 42) -> Path:
    rng = np.random.default_rng(seed)
    samples = generate_samples(distribution, n, rng)

    cumulative_sums = np.cumsum(samples)
    k_values = np.arange(1, n + 1)
    cumulative_means = cumulative_sums / k_values

    # Grafik klasörü oluştur
    output_dir = Path("results") / distribution
    output_dir.mkdir(parents=True, exist_ok=True)
    fig_path = output_dir / "slln_mean.png"

    # Grafik çiz
    plt.figure(figsize=(10, 5))
    plt.plot(k_values, cumulative_means, label="Cumulative Mean")

    true_mean = get_true_mean(distribution)
    if true_mean is not None:
        plt.axhline(y=true_mean, color="red", linestyle="--", label=f"E[X] = {true_mean}")
    else:
        plt.axhline(y=0, color="gray", linestyle="--", label="No defined E[X]")

    plt.title(f"SLLN Simulation – {distribution}")
    plt.xlabel("n (number of observations)")
    plt.ylabel("Cumulative Mean")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()

    plt.savefig(fig_path, dpi=300)
    plt.close()
    print(f"✅ {distribution}: {fig_path}")
    return fig_path


if __name__ == "__main__":
    distributions = ["uniform", "exponential", "pareto_a3", "pareto_a15", "cauchy"]
    for dist in distributions:
        run_slln(dist, n=10000)
