#O(3n)
n = 4
a = 0
for i in range(n):
    a+=1
for i in range(n):
    a+=1
for i in range(n):
    a+=1
print("Макс. количество итераций алгоритма 1 = " + str(a))
#O(n^3)
a = 0
for i in range(n):
    for j in range(n):
        for k in range(n):
            a+=1
print("Макс. количество итераций алгоритма 2 = " + str(a))
#O(3(log(n)))
num = 1 #берем число, чтобы длительность исполнения алгоритма была максимально возможной
a = 0
n = [x for x in range(1, 33)]
while len(n) > 0:
    middle = len(n) // 2
    if n[middle] == num:
        break
    elif n[middle] < num:
        n = n[middle+1:]
    else:
        n = n[:middle]
    a+=1
n = [x for x in range(1, 33)]
while len(n) > 0:
    middle = len(n) // 2
    if n[middle] == num:
        break
    elif n[middle] < num:
        n = n[middle+1:]
    else:
        n = n[:middle]
    a+=1
n = [x for x in range(1, 33)]
while len(n) > 0:
    middle = len(n) // 2
    if n[middle] == num:
        break
    elif n[middle] < num:
        n = n[middle+1:]
    else:
        n = n[:middle]
        a+=1
print("Макс. количество итераций алгоритма 3 = " + str(a))
#O(nlog(n))
n = 32
a=0
for i in range(n):
    n = [x for x in range(1, 33)]
    while len(n) > 0:
        middle = len(n) // 2
        if n[middle] == num:
            break
        elif n[middle] < num:
            n = n[middle+1:]
        else:
            n = n[:middle]
        a+=1
print("Макс. количество итераций алгоритма 4 = " + str(a))
#O(n!)
n = 5
a = 0
def generate_permutations(li):
    n = len(li)
    if n == 0:
        return [[]]
    else:
        permutations = []
        for i in range(n):
            rest = li[:i] + li[i+1:]
            for j in generate_permutations(rest):
                permutations.append([li[i]] + j)
        return permutations

li = [x for x in range(1, n+1)]
permutations = generate_permutations(li)
for p in permutations:
    a+=1
print("Макс. количество итераций алгоритма 5 = " + str(a))

