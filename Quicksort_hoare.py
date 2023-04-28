"""
Quicksort is an efficient, general-purpose sorting algorithm. Quicksort was developed by British computer scientist
Tony Hoare in 1959[1] and published in 1961.[2] It is still a commonly used algorithm for sorting. Overall,
it is slightly faster than merge sort and heapsort for randomized data, particularly on larger distributions.
"""


def quick_sort(a):
    if len(a) > 1:
        # x = a[random.randint(0, len(a) - 1)]
        x = a[0]
        low = [u for u in a if u < x]
        eq = [u for u in a if u == x]
        hi = [u for u in a if u > x]
        a = quick_sort(low) + eq + quick_sort(hi)
    return a


a = [9, 5, -3, 4, 7, 8, -8, 4]
a = quick_sort(a)
print(a)
