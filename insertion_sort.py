"""
Insertion sort is a simple sorting algorithm that builds the final sorted array (or list) one item at a time by
comparisons. It is much less efficient on large lists than more advanced algorithms such as quicksort, heapsort,
 or merge sort.
"""

a = [-3, 5, 0, -8, 1, 10]
N = len(a)

for i in range(1, N):
    for j in range(i, 0, -1):
        if a[j] < a[j - 1]:
            a[j], a[j - 1] = a[j - 1], a[j]
        else:
            break


print(a)


# Insertion sort in Python


def insertionSort(array):
    for step in range(1, len(array)):
        key = array[step]
        j = step - 1

        # Compare key with each element on the left of it until an element smaller than it is found
        # For descending order, change key<array[j] to key>array[j].
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1

        # Place key at after the element just smaller than it.
        array[j + 1] = key


data = [9, 5, 1, 4, 3]
insertionSort(data)
print('Sorted Array in Ascending Order:')
print(data)