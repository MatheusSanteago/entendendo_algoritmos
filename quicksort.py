import random

arr = random.sample(range(1, 1001), 100)


def quicksort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        low = [i for i in arr[1:] if i <= pivot]
        high = [i for i in arr[1:] if i > pivot]
    return quicksort(low) + [pivot] + quicksort(high)


print(quicksort(arr))
