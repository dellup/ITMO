from random import *
from timeit import timeit
def quicksort(li):
    if len(li) <= 1:
        return li
    else:
        fst = li[0]
        less = [x for x in li[1:] if x <= fst]
        greater = [x for x in li[1:] if x > fst]
        return quicksort(less) + [fst] + quicksort(greater)

a = [randint(1, 10000) for i in range(50)]
b=a.copy()

test="""
def quicksort(li):
    if len(li) <= 1:
        return li
    else:
        fst = li[0]
        less = [x for x in li[1:] if x <= fst]
        greater = [x for x in li[1:] if x > fst]
        return quicksort(less) + [fst] + quicksort(greater)
"""

print("Массив до сортировки: ",  b)
print("Массив после сортировки: ", quicksort(b))
timre = timeit(test, number=1)
print("Время выполнения = ", timre)
