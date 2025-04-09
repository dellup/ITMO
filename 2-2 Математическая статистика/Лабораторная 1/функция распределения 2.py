import numpy as np
import matplotlib.pyplot as plt

intervals = [(114, 119), (119, 124), (124, 129), (129, 134), (134, 139), 
             (139, 144), (144, 149), (149, 154), (154, 159)]
N_i = [3, 14, 51, 110, 157, 181, 188, 189, 190]

x_values = [interval[1] for interval in intervals]
y_values = [N / max(N_i) for N in N_i]

plt.figure(figsize=(8, 5))
plt.plot(x_values, y_values, marker='o', linestyle='-', color='b', label=r'$F_n(x)$')


#mode = 136
#plt.axvline(mode, color='r', linestyle='--', label=f'Мода = {mode}')


#plt.text(mode + 0.5, 0.7, f'Мода = {mode}', color='red', fontsize=12)

plt.xlabel(r'$x_i$', fontsize=12)
plt.ylabel(r'$F_n(x_i)$', fontsize=12)
plt.title('Функция распределения', fontsize=14)
plt.grid(True)
plt.legend()
plt.show()
