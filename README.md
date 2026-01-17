# IE221 – Teamwork 3–4–5 | Group 11

Nil Belinay Akkoyun – 2211021005  
Mina Soyçeri – 2311021014  
Gönül Hülya Atik – 2211021057  

This repository is created for the **IE221 – Probability** course, and contains our work for **Teamwork 3**, **Teamwork 4**, and **Teamwork 5**.


##  Project Overview

The project consists of three phases:

1. **Teamwork 3**: Initial implementation of SLLN, CLT, and Monte Carlo π estimation.
2. **Teamwork 4**: Technical reporting and evaluation of convergence behaviors.
3. **Teamwork 5**: Extended analysis on multiple distributions, testing the limits of SLLN and CLT.

We experimentally verify:
- The **Strong Law of Large Numbers (SLLN)**
- The **Central Limit Theorem (CLT)**
- And explore where these theorems do *not* apply

##  Methodology

- Simulations are performed using Python and Monte Carlo techniques
- We generate random samples from multiple distributions:
  - Uniform, Exponential, Pareto(α=3), Pareto(α=1.5), and Cauchy
- We visualize convergence and compare it to theoretical expectations


##  Repository Structure

- `src/`: All Python source code
- `results/figures_slln/`: Cumulative mean plots for SLLN
- `results/figures_clt/`: Histograms and Q-Q plots for CLT
- `reports/`: PDF reports submitted for TW2 and TW3
- `README.md`: Project overview and team information


##  Results

- SLLN: Stabilization of means is observed for most distributions with finite expected value
- CLT: Normal convergence behavior is observed where assumptions are satisfied
- Cauchy and Pareto(α=1.5) exhibit divergence due to undefined or infinite moments

All plots are saved in the appropriate subfolders under `results/`.

##  Technical Report

- `TW2_Report.pdf` and `TW3_Report.pdf` are located in the `reports/` folder
- Each report includes theoretical background, code structure, simulation outputs, and detailed interpretation
