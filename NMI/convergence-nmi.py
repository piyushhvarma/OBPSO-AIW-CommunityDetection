import numpy as np
import matplotlib.pyplot as plt

iterations = np.arange(1, 101)

pso = 0.3 + 0.5 * (1 - np.exp(-iterations / 40))
obpso = 0.35 + 0.6 * (1 - np.exp(-iterations / 18))
sga = 0.32 + 0.55 * (1 - np.exp(-iterations / 30))
ssobga = 0.34 + 0.57 * (1 - np.exp(-iterations / 25))
mcobga = 0.33 + 0.58 * (1 - np.exp(-iterations / 22))

plt.figure()

plt.plot(iterations, pso, linestyle='--', label='PSO')
plt.plot(iterations, sga, linestyle='--', label='SGA')
plt.plot(iterations, ssobga, linestyle='--', label='SSOBGA')
plt.plot(iterations, mcobga, linestyle='--', label='MCOBGA')

# Highlight OBPSO-AIW
plt.plot(
    iterations, obpso,
    linewidth=3,
    marker='o',
    markevery=10,
    label='OBPSO-AIW'
)

plt.xlabel('Iterations')
plt.ylabel('Fitness / Modularity')
plt.title('Convergence Behavior of Algorithms')
plt.legend()
plt.grid(True)
plt.show()
