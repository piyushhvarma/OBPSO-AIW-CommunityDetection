import matplotlib.pyplot as plt

algorithms = ['PSO', 'SGA', 'SSOBGA', 'MCOBGA', 'OBPSO-AIW']
mcdm_score = [0.42, 0.63, 0.69, 0.73, 0.81]

plt.figure()

bars = plt.barh(algorithms, mcdm_score)

# Highlight OBPSO-AIW
bars[-1].set_hatch('//')
bars[-1].set_edgecolor('black')
bars[-1].set_linewidth(2)

plt.xlabel('MCDM Score')
plt.title('Overall Algorithm Ranking Using MCDM')
plt.xlim(0, 1)

for i, v in enumerate(mcdm_score):
    plt.text(v + 0.01, i, f"{v:.2f}", va='center')

plt.show()
