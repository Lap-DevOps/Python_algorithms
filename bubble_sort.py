"""
Bubble sort, sometimes referred to as sinking sort, is a simple sorting algorithm that repeatedly steps through
the input list element by element, comparing the current element with the one after it, swapping their values if
needed. These passes through the list are repeated until no swaps had to be performed during a pass, meaning that
the list has become fully sorted. The algorithm, which is a comparison sort, is named for the way the larger elements
"bubble" up to the top of the list.
"""

a = [7, 5, -8, 0, 10, 1]
N = len(a)

for i in range(N - 1):
    for x in range(N - i - 1):
        if a[x] < a[x + 1]:
            a[x], a[x + 1] = a[x + 1], a[x]
print(a)


# Bubble sort in Python

def bubbleSort(array):
    # loop to access each array element
    for i in range(len(array)):

        # loop to compare array elements
        for j in range(0, len(array) - i - 1):

            # compare two adjacent elements
            # change > to < to sort in descending order
            if array[j] > array[j + 1]:
                # swapping elements if elements
                # are not in the intended order
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp


data = [-2, 45, 0, 11, -9]

bubbleSort(data)

print('Sorted Array in Ascending Order:')
print(data)