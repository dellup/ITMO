import time
import random

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
    

def hybrid_sort(arr):
    if len(arr) <= 100:
        return insertion_sort(arr)
    else:
        return merge_sort(arr)

def quick_sort(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1

    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)
        
def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def heapify(arr, n, i):
    largest = i 
    l = 2 * i + 1  
    r = 2 * i + 2   
    if l < n and arr[i] < arr[l]:
        largest = l
    if r < n and arr[largest] < arr[r]:
        largest = r
    if largest != i:
        arr[i],arr[largest] = arr[largest],arr[i] 

        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)
    for i in range(n, -1, -1):
        heapify(arr, n, i)
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i] 
        heapify(arr, i, 0)
        
def sorting_time(sort_func, arr):
    start_time = time.time()
    sort_func(arr)
    end_time = time.time()
    return end_time - start_time

def generate_array(size):
    return [random.randint(0, 10000) for _ in range(size)]

def tests():
    sizes = [10, 100, 1000, 10000, 50000]
    algorithms = {
        "Hybrid Sort": hybrid_sort,
        "Quick Sort": quick_sort,
        "Heap Sort": heap_sort,}
    for size in sizes:
        print(f"Размер массива: {size}")
        orig_array = generate_array(size)
        for name, sort_func in algorithms.items():
            arr = orig_array.copy()
            time_taken = sorting_time(sort_func, arr)
            print(f"{name}: {time_taken:.15f} секунд")
        print()
tests()
def test_correctness():
    cases = [
        [], 
        [1], 
        [2, 1], 
        [1, 2], 
        [x for x in range(1, 501)], 
        [x for x in range(500, 0, -1)], 
        generate_array(500)
    ]
    algorithms = {
        "Hybrid Sort": hybrid_sort,
        "Quick Sort": quick_sort,
        "Heap Sort": heap_sort,
    }
    for case in cases:
        print(f"Первоначальный массив: {case}")
        for name, sort_func in algorithms.items():
            arr = case.copy()
            sort_func(arr)
            time_taken = sorting_time(sort_func, arr)
            print(f"{name}: {time_taken:.15f} секунд")
        print()
test_correctness()