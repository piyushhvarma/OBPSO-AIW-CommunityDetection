import numpy as np

# Define NMI values FIRST
pso = [0.55, 0.67, 0.46, 0.39, 0.46, 0.51, 0.42, 0.32, 0.49]
obpso = [1.00, 1.00, 0.89, 0.88, 0.99, 0.93, 0.91, 0.85, 0.90]
sga = [0.60, 0.79, 0.80, 0.82, 0.30, 0.43, 0.68, 0.59, 0.74]
ssobga = [0.60, 0.82, 0.80, 0.83, 0.34, 0.88, 0.75, 0.62, 0.78]
mcobga = [0.81, 0.81, 0.83, 0.83, 0.87, 0.88, 0.80, 0.70, 0.83]

# Pairwise dominance check (no scipy)
algorithms = {
    "PSO": pso,
    "SGA": sga,
    "SSOBGA": ssobga,
    "MCOBGA": mcobga
}

print("OBPSO-AIW dominance check:\n")

for name, values in algorithms.items():
    better = sum(o > v for o, v in zip(obpso, values))
    print(f"OBPSO-AIW outperforms {name} on {better}/9 datasets")
    if better == 9:
        print(f"-> OBPSO-AIW strictly dominates {name}\n")
    else:
        print()