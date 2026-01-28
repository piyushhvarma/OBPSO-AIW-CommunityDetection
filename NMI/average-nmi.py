import matplotlib.pyplot as plt
import numpy as np

algorithms = ['PSO', 'OBPSO-AIW', 'SGA', 'SSOBGA', 'MCOBGA']
avg_nmi = [0.48, 0.93, 0.67, 0.72, 0.77]

plt.figure()

bars = plt.bar(algorithms, avg_nmi)

# Highlight OBPSO-AIW
bars[1].set_hatch('//')
bars[1].set_edgecolor('black')
bars[1].set_linewidth(2)

for i, v in enumerate(avg_nmi):
    plt.text(i, v + 0.01, f"{v:.2f}", ha='center')

plt.xlabel('Algorithms')
plt.ylabel('Average NMI')
plt.title('Average NMI Comparison Across All Networks')
plt.ylim(0, 1)
plt.show()
