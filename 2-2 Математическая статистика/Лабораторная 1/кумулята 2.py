import numpy as np
import matplotlib.pyplot as plt

intervals = [(114, 119), (119, 124), (124, 129), (129, 134), (134, 139), 
             (139, 144), (144, 149), (149, 154), (154, 159)]
n_i = [3, 11, 37, 59, 47, 24, 7, 1, 1]
N_i = np.cumsum(n_i)

x_values = [(interval[0] + interval[1]) / 2 for interval in intervals]  # Средние точки интервалов
y_values = list(N_i)


plt.figure(figsize=(8, 5))
plt.plot(x_values, y_values, marker='o', linestyle='-', color='r', label='Кумулята')

#median = 132
#plt.axvline(median, color='g', linestyle='--', label=f'Медиана = {median}')
#plt.text(median + 0.5, max(y_values) * 0.7, f'Медиана = {median}', color='green', fontsize=12)

plt.xlabel(r'$x_i$', fontsize=12)
plt.ylabel(r'$N_i$', fontsize=12)
plt.title('Кумулята', fontsize=14)
plt.grid(True)
plt.legend()
plt.show()

plt.figure(figsize=(8, 5))
plt.plot(y_values, x_values, marker='o', linestyle='-', color='b', label='Огива')


plt.xlabel(r'$N_i$', fontsize=12)
plt.ylabel(r'$x_i$', fontsize=12)
plt.title('Огива', fontsize=14)
plt.grid(True)
plt.legend()
plt.show()
