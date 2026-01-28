import matplotlib.pyplot as plt

algos = ['PSO', 'SGA', 'SSOBGA', 'MCOBGA', 'OBPSO-AIW']
ranks = [5, 4, 3, 2, 1]  # 1 = best

plt.figure()
plt.plot(ranks, algos, marker='o')
plt.xlabel('Average Rank')
plt.title('Statistical Ranking of Algorithms')
plt.grid(True)
plt.show()
