import numpy as np
import matplotlib.pyplot as plt

labels = ['Modularity', 'NMI', 'ARI', 'Stability', 'Conv. Speed']
angles = np.linspace(0, 2*np.pi, len(labels), endpoint=False).tolist()
angles += angles[:1]

data = {
    'PSO':        [0.55, 0.48, 0.46, 0.50, 0.52],
    'SGA':        [0.75, 0.67, 0.64, 0.68, 0.66],
    'SSOBGA':     [0.78, 0.72, 0.70, 0.73, 0.71],
    'MCOBGA':     [0.82, 0.87, 0.84, 0.86, 0.84],
    'OBPSO-AIW':  [0.92, 0.93, 0.91, 0.90, 0.89]
}

plt.figure(figsize=(6,6))
ax = plt.subplot(111, polar=True)

for algo, values in data.items():
    values += values[:1]
    if algo == 'OBPSO-AIW':
        ax.plot(angles, values, linewidth=3, marker='o', label=algo)
        ax.fill(angles, values, alpha=0.25)
    else:
        ax.plot(angles, values, linestyle='--', linewidth=1, label=algo)

ax.set_thetagrids(np.degrees(angles[:-1]), labels)
plt.title('Multi-Metric Performance Comparison')
plt.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1))
plt.show()
