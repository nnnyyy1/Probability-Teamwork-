"""
Central Limit Theorem (CLT) Simulation

This script performs verification to the Central Limit
Theorem using Uniform(0,1) random variables. Standardized sums are generated
for different sample sizes, and convergence in distribution is analyzed
using histograms and Q-Q plots.
"""


import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
import os

# ========================
# Distribution definitions
# ========================
distributions = {
    "uniform": {
        "sampler": lambda size: np.random.uniform(0, 1, size=size),
        "mu": 0.5,
        "sigma": np.sqrt(1/12)
    },
    "exponential": {
        "sampler": lambda size: np.random.exponential(scale=1, size=size),
        "mu": 1.0,
        "sigma": 1.0
    },
    "pareto_alpha3": {
        "sampler": lambda size: (np.random.pareto(a=3, size=size) + 1),
        "mu": 1.5,
        "sigma": np.sqrt(3/4)
    },
    "pareto_alpha1_5": {
        "sampler": lambda size: (np.random.pareto(a=1.5, size=size) + 1),
        "mu": 3.0,
        "sigma": None   # variance is infinite
    },
    "cauchy": {
        "sampler": lambda size: np.random.standard_cauchy(size=size),
        "mu": None,
        "sigma": None
    }
}

m = 1000 
n_values = [2, 5, 10, 30, 50, 100]
m = 1000                 # Number of experiments
n_values = [2, 5, 10, 30, 50]

# Create output directory if not exists
output_dir = "results/figures"
os.makedirs(output_dir, exist_ok=True)

# ========================
# CLT Simulation
# ========================
for dist_name, dist in distributions.items():
    # Optional: Create subfolders so files don't overwrite
    dist_folder = os.path.join(output_dir, dist_name)
    os.makedirs(dist_folder, exist_ok=True)
    
    for n in n_values:
        samples = dist["sampler"]((m, n)) # Uses the dictionary sampler
        sums = samples.sum(axis=1)

        if dist["mu"] is None or dist["sigma"] is None:
            Z = sums
        else:
            Z = (sums - n * dist["mu"]) / (dist["sigma"] * np.sqrt(n))

    # --------------------
    # Histogram + Normal PDF
    # --------------------
    plt.figure(figsize=(8, 5))
    plt.hist(Z, bins=30, density=True, alpha=0.6, label="Standardized sums")

        # Overlay the theoretical Standard Normal Distribution N(0,1)
    x = np.linspace(-4, 4, 400)
    plt.plot(x, stats.norm.pdf(x), 'r', lw=2, label="N(0,1)")

    plt.title(f"{dist_name.replace('_', ' ').capitalize()} (n = {n})")
    plt.xlabel("Z")
    plt.ylabel("Density")
    plt.legend()
    plt.grid(True, alpha=0.3)

    # Save the histogram
    plt.savefig(f"{dist_folder}/clt_hist_n{n}.png")
    plt.close()

    # --------------------
    # Q-Q Plot
    # --------------------
    plt.figure(figsize=(6, 6))
    stats.probplot(Z, dist="norm", plot=plt)
    plt.title(f"Q-Q Plot (n = {n})")
    plt.grid(True)

    plt.savefig(f"{output_dir}/clt_qqplot_n{n}.png")
    plt.close()

print("CLT simulation completed. Figures saved in results/figures/")

