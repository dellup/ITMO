import matplotlib.pyplot as plt
import numpy as np

intervals = ['[0, 1)', '[1, 2)', '[2, 3)', '[3, 4)', '[4, 5)', '[5, 6)', '[6, 7)', '[7, 8)', '[8, 9)', '[9, +∞)']
cumulative_frequencies = [1, 12, 25, 39, 58, 71, 76, 82, 85, 86, 86]

total_samples = 86
empirical_function = [f / total_samples for f in cumulative_frequencies]

x_values = [0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5]

plt.figure(figsize=(10, 6))
plt.step(x_values, empirical_function, where='post', linestyle='-', color='b', linewidth=2)
plt.xlabel('$x_i$')
plt.ylabel('$F_n(x)$')
plt.title('Эмпирическая функция распределения')
plt.grid(True)
plt.xticks(np.arange(0, 10, 1))
plt.yticks(np.arange(0, 1.1, 0.1))
plt.show()
