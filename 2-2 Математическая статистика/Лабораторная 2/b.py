import math
s = "71 62 43 80 70 44 42 25 48 55 58 44 74 55 56 49 54 63 60 57 70 52 74 65 61 60 72 69 68 47 30 62 81 56 55 38 68 55 74 50 29 35 55 52 27 58 50 62 80 49 68 68 81 66 64 41 45 48 68 79 56 82 76 84 47 44 72 58 58 80 61 55 66 36 69 44 88 88 73 39 70 70 35 51 69 50 59 35 43 71 54 65 85 63 59 52 88 64 60 61 31 64 48 49 50 41 62 42 76 81 76 70 76 75 53 66 87 74 61 68 73 44 61 53 46 69 71 58 63  73 56 65 53 77 39 83 45 55 77 61 42 72 49 52 67 62 68 72 46 76 67 53 70 76 56 62 38 59 53 50 76 52 73 34 51 60 61"
data = list(map(int, s.split()))

# Размер выборки
n = len(data)

# 1. Среднее
sum_x = 0
for x in data:
    sum_x += x

mean = sum_x / n

# 2. Дисперсия
sum_squared_diff = 0
for x in data:
    sum_squared_diff += (x - mean) ** 2

variance = sum_squared_diff / n

# 3. Стандартное отклонение
std_dev = math.sqrt(variance)

# Вывод
print("Метод моментов для нормального распределения:")
print(f"Размер выборки n = {n}")
print(f"Среднее (mu) = {mean:.5f}")
print(f"Дисперсия (sigma^2) = {variance:.5f}")
print(f"Ст. отклонение (sigma) = {std_dev:.5f}")

import matplotlib.pyplot as plt
mu = mean
sigma = std_dev
n = len(data)

# 2. Количество интервалов (Стерджесс)
k = round(1 + 3.322 * math.log10(n))

data_min = min(data)
data_max = max(data)
interval_width = (data_max - data_min) / k

intervals = []
for i in range(k):
    a_i = data_min + i * interval_width
    b_i = a_i + interval_width
    intervals.append((a_i, b_i))

def standard_normal_cdf(z):
    return 0.5 * (1 + math.erf(z / math.sqrt(2)))

theoretical_frequencies = []
for a_i, b_i in intervals:
    z1 = (a_i - mu) / sigma
    z2 = (b_i - mu) / sigma
    p = standard_normal_cdf(z2) - standard_normal_cdf(z1)
    expected_freq = n * p
    theoretical_frequencies.append((a_i, b_i, expected_freq))

empirical_frequencies = []
for a_i, b_i in intervals:
    count = 0
    for x in data:
        if a_i <= x < b_i or (b_i == data_max and x == data_max): 
            count += 1
    empirical_frequencies.append(count)

interval_centers = [(a + b) / 2 for a, b in intervals]
theoretical = [round(freq[2], 2) for freq in theoretical_frequencies]
print(theoretical_frequencies)
plt.figure(figsize=(10, 6))
plt.plot(interval_centers, empirical_frequencies, marker='o', linestyle='-', label='Эмпирическое распределение')
plt.plot(interval_centers, theoretical, marker='s', linestyle='--', label='Теоретическое (нормальное) распределение')

plt.title('Сравнение эмпирического и теоретического распределений')
plt.xlabel('Значение')
plt.ylabel('Частота')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()


n = len(data)
mean = sum(data) / n
var = sum((x - mean)**2 for x in data) / (n - 1)
std = math.sqrt(var)

# Квантиль t (ручная вставка t0.975 для df=209)
t_crit = 1.971
mu_margin = t_crit * std / math.sqrt(n)
mu_low = mean - mu_margin
mu_high = mean + mu_margin

# Квантили хи-квадрат (ручные значения для df=209, alpha=0.05)
chi2_low = 241.89
chi2_high = 178.67

var_low = (n - 1) * var / chi2_low
var_high = (n - 1) * var / chi2_high
std_low = math.sqrt(var_low)
std_high = math.sqrt(var_high)

# Вывод
print("Доверительный интервал для μ: [%.2f, %.2f]" % (mu_low, mu_high))
print("Доверительный интервал для σ²: [%.2f, %.2f]" % (var_low, var_high))
print("Доверительный интервал для σ: [%.2f, %.2f]" % (std_low, std_high))


n = len(data)

# Среднее
mean = sum(data) / n

# Дисперсия
variance = sum((x - mean)**2 for x in data) / n
std_dev = math.sqrt(variance)

# Медиана
sorted_data = sorted(data)
if n % 2 == 0:
    median = (sorted_data[n // 2 - 1] + sorted_data[n // 2]) / 2
else:
    median = sorted_data[n // 2]

# Мода
freqs = {}
for x in data:
    freqs[x] = freqs.get(x, 0) + 1
mode = max(freqs, key=freqs.get)

# Асимметрия (скошенность)
skew = sum((x - mean)**3 for x in data) / n / (std_dev**3)

# Эксцесс (минус 3 — нормализация)
kurtosis = sum((x - mean)**4 for x in data) / n / (std_dev**4) - 3

theor_mean = mean       # по определению
theor_median = mean
theor_mode = mean
theor_variance = variance
theor_std = std_dev
theor_skew = 0
theor_kurtosis = 0

# Вывод
print("Сравнение с нормальным распределением:")
print(f"{'Характеристика':<30}{'Эмпирическое':>20}{'Теоретическое':>20}")
print("-" * 70)
print(f"{'Математическое ожидание':<30}{mean:>20.4f}{theor_mean:>20.4f}")
print(f"{'Дисперсия':<30}{variance:>20.4f}{theor_variance:>20.4f}")
print(f"{'Ст. отклонение':<30}{std_dev:>20.4f}{theor_std:>20.4f}")
print(f"{'Медиана':<30}{median:>20.4f}{theor_median:>20.4f}")
print(f"{'Мода':<30}{mode:>20.4f}{theor_mode:>20.4f}")
print(f"{'Коэфф. асимметрии':<30}{skew:>20.4f}{theor_skew:>20.4f}")
print(f"{'Коэфф. эксцесса':<30}{kurtosis:>20.4f}{theor_kurtosis:>20.4f}")