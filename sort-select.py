"""
In computer science, selection sort is an in-place comparison sorting algorithm. It has an O(n2) time complexity,
which makes it inefficient on large lists, and generally performs worse than the similar insertion sort.
Selection sort is noted for its simplicity and has performance advantages over more complicated algorithms in
certain situations, particularly where auxiliary memory is limited.
"""
import time

def calculate_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function '{func.__name__}' took {end_time - start_time:.6f} seconds to run.")
        return result
    return wrapper


a = [-3, 5, 0, -8, 10, 13, 13, 54, 23, -23]
N = len(a)

for i in range(N - 1):
    m = a[i]
    p = i
    for j in range(i + 1, N):
        if m > a[j]:
            m = a[j]
            p = j

    if p != i:
        t = a[i]
        a[i] = a[p]
        a[p] = t

print(a)


# second
@ calculate_time
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        # Find the minimum element in the unsorted portion of the array
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        # Swap the minimum element with the first element in the unsorted portion of the array
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr

print(selection_sort(a))