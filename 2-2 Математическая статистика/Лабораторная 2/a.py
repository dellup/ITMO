s = "3 5 6 8 4 5 4 7 2 7 7 3 7 4 4 5 4 4 5 2 4 8 8 4 6 5 9 4 0 4 4 4 9 3 3 2 1 5 2 5 5 3 4 4 7 8 9 11 4 5 2 5 7 6 1 2 5 6 3 1 2 6 7 3 3 2 5 4 8 2 6 5 9 5 5 2 8 3 6 4 6 6 8 7 3 3 7 3"
data = list(map(int, s.split()))

n = len(data)
print(sum(data))

x_bar = sum(data) / n

s2_mle = sum((x - x_bar) ** 2 for x in data) / n

print("Размер выборки:", n)
print("Выборочное среднее:", x_bar)
print("Оценка sigma^2:", s2_mle)

n = 0
for x in data:
    n += 1

sum_x = 0
for x in data:
    sum_x += x
m1 = sum_x / n 

sum_sq = 0
for x in data:
    sum_sq += x * x
m2 = sum_sq / n

mu_mm = m1
sigma2_mm = m2 - (m1 * m1)

print("Размер выборки, n =", n)
print("Первый эмпирический момент=", mu_mm)
print("Второй эмпирический момент", m2)
print("Оценка параметра sigma^2", sigma2_mm)

import math

# Вычисляем размер выборки
n = 0
for x in data:
    n += 1

# Заданная оценка параметра для пуассоновского распределения (полученная ранее)
lambda_est = 4.7954

mu_est = 4.7954

# Оценка дисперсии:
sigma2_est = 4.9127
sigma_est = math.sqrt(sigma2_est)

# Функция для вычисления кумулятивной функции распределения стандартного нормального распределения
def normal_cdf(z):
    return 0.5 * (1 + math.erf(z / math.sqrt(2)))

print("Теоретические частоты для пуассоновского распределения:")
for x in range(0, 8):
    # Вычисляем вероятность P(X=x) по формуле пуассоновского распределения
    p = (lambda_est ** x * math.exp(-lambda_est)) / math.factorial(x)
    freq = n * p
    print(f"x = {x:2d}  Frequency = {freq:.2f}")

for x in range(0, 8):
    # Определяем границы интервала
    lower_bound = x - 0.5
    upper_bound = x + 0.5
    
    # Приводим границы к шкале стандартного нормального распределения
    z_lower = (lower_bound - mu_est) / sigma_est
    z_upper = (upper_bound - mu_est) / sigma_est
    
    # Вычисляем вероятность попадания в интервал
    probability = normal_cdf(z_upper) - normal_cdf(z_lower)
    
    print(f"Интервал [{lower_bound}, {upper_bound}): вероятность = {probability:.4f}")


import matplotlib.pyplot as plt

# Размер выборки
n = 0
for x in data:
    n += 1

# Определяем диапазон значений x (от 0 до 7)
x_values = list(range(0, 8))

# 1. Эмпирические частоты: считаем, сколько раз встречается каждое значение x
empirical_freq = []
for x in x_values:
    count = 0
    for d in data:
        if d == x:
            count += 1
    empirical_freq.append(count)

# 2. Теоретические частоты для пуассоновского распределения:
# Оценка параметра (получена ранее)
lambda_est = 4.7954
poisson_freq = []
for x in x_values:
    p = (lambda_est ** x * math.exp(-lambda_est)) / math.factorial(x)
    poisson_freq.append(n * p)

# Функция кумулятивной функции стандартного нормального распределения через erf
def normal_cdf(z):
    return 0.5 * (1 + math.erf(z / math.sqrt(2)))

normal_freq = []
for x in x_values:
    # Интервал [x-0.5, x+0.5)
    lower = (x - 0.5 - mu_est) / sigma_est
    upper = (x + 0.5 - mu_est) / sigma_est
    p = normal_cdf(upper) - normal_cdf(lower)
    normal_freq.append(n * p)

# Построение графика
plt.figure(figsize=(8, 6))
plt.plot(x_values, empirical_freq, 'o-', label='Эмпирическое распределение')
plt.plot(x_values, poisson_freq, 's-', label='Пуассоновское распределение')
plt.xlabel('Значение x')
plt.ylabel('Частота')
plt.title('Полигоны эмпирического и теоретического распределения')
plt.legend()
plt.grid(True)
plt.show()