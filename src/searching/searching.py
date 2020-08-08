import math

def linear_search(arr, target):
    for i, v in enumerate(arr):
        if v == target:
            return i
    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    start = 0
    end = arr.__len__() - 1
    while start <= end:
        mid = math.ceil((start + (end - 1)) / 2)
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

    return -1  # not found