import matplotlib.pyplot as plt

algorithms = ['PSO', 'SGA', 'SSOBGA', 'MCOBGA', 'OBPSO-AIW']
runtime = [18, 25, 28, 30, 22]        # seconds (example)
accuracy = [0.48, 0.67, 0.72, 0.77, 0.93]  # NMI / modularity

plt.figure()

for i, algo in enumerate(algorithms):
    if algo == 'OBPSO-AIW':
        plt.scatter(runtime[i], accuracy[i], s=200, marker='*', label=algo)
        plt.annotate(algo, (runtime[i]+0.3, accuracy[i]))
    else:
        plt.scatter(runtime[i], accuracy[i], s=80)
        plt.annotate(algo, (runtime[i]+0.3, accuracy[i]))

plt.xlabel('Execution Time (seconds)')
plt.ylabel('Accuracy (NMI / Modularity)')
plt.title('Runtime vs Accuracy Trade-off')
plt.grid(True)
plt.legend()
plt.show()
