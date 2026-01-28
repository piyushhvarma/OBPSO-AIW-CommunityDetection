import matplotlib.pyplot as plt
import numpy as np

np.random.seed(42)

pso = np.random.normal(0.48, 0.05, 20)
obpso = np.random.normal(0.93, 0.02, 20)
sga = np.random.normal(0.67, 0.04, 20)
ssobga = np.random.normal(0.72, 0.03, 20)
mcobga = np.random.normal(0.77, 0.03, 20)

data = [pso, obpso, sga, ssobga, mcobga]

plt.figure()
box = plt.boxplot(
    data,
    labels=['PSO', 'OBPSO-AIW', 'SGA', 'SSOBGA', 'MCOBGA'],
    patch_artist=True
)

# Highlight OBPSO-AIW box
box['boxes'][1].set_linewidth(3)
box['medians'][1].set_linewidth(3)

plt.ylabel('NMI Value')
plt.title('Stability Analysis Across Multiple Runs')
plt.grid(True)
plt.show()
