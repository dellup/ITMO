def find_subarray(arr, target):
    start = 0
    end = 0
    current_sum = arr[0]
    min_sum = float('inf')
    result = []
    while end < len(arr):
        if current_sum <= target:
            end += 1
            if end < len(arr):
                current_sum += arr[end]
        else:
            if current_sum - arr[start] <= target:
                if current_sum - target < min_sum:
                    min_sum = current_sum - target
                    result = [start, end]
                current_sum -= arr[start]
                start += 1
            else:
                current_sum -= arr[start]
                start += 1
    return arr[result[0]:result[1]+1]
arr = [5,7,2,3,1,5,2,5,4,3,2,3,4,5,3]
target = 10
print(find_subarray(arr, target))