from random import randint
n = int(input("Введите количество чисел в массиве: "))
N = []
for i in range(n):
    num = randint(-100, 100)
    N.append(num)
maxim = -1000000
count = 0
for i in range(n-1):
    if N[i] < N[i+1]:
        count+=1
        maxim = max(maxim, count)
    else:
        count = 0
print(f"Длина наибольшей непрерывной возрастающей последовательности из чисел внутри массива равна {maxim}")
