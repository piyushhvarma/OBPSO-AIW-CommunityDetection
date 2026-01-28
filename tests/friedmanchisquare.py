import numpy as np
from scipy.stats import friedmanchisquare

# NMI values across datasets (example)
pso = [0.55, 0.67, 0.46, 0.39, 0.45, 0.51, 0.42, 0.32, 0.48]
obpso = [1.00, 1.00, 0.88, 0.88, 0.99, 0.93, 0.91, 0.85, 0.90]
sga = [0.60, 0.79, 0.80, 0.82, 0.30, 0.43, 0.68, 0.59, 0.74]
ssobga = [0.60, 0.82, 0.80, 0.83, 0.34, 0.88, 0.75, 0.62, 0.78]
mcobga = [0.51, 0.71, 0.71, 0.78, 0.87, 0.88, 0.80, 0.70, 0.83]

stat, p = friedmanchisquare(pso, obpso, sga, ssobga, mcobga)

print("Friedman statistic:", stat)
print("p-value:", p)
