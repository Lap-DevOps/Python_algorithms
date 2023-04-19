"""
n computer science, merge sort (also commonly spelled as mergesort) is an efficient, general-purpose, and
comparison-based sorting algorithm. Most implementations produce a stable sort, which means that the order of
equal elements is the same in the input and output. Merge sort is a divide-and-conquer algorithm that was invented
by John von Neumann in 1945.[2] A detailed description and analysis of bottom-up merge sort appeared in a report
by Goldstine and von Neumann as early as 1948.[3]
"""

a = [1, 4, 10, 11]
b = [2, 3, 3, 4, 8]
c = []

N = len(a)
M = len(b)

i = 0
j = 0
while i < N and j < M:
    if a[i] <= b[j]:
        c.append(a[i])
        i += 1
    else:
        c.append(b[j])
        j += 1

c += a[i:] + b[j:]
print(c)

print(sorted(a + b))


# fast sorting

def merge_list(a, b):
    c = []
    N = len(a)
    M = len(b)

    i = 0
    j = 0
    while i < N and j < M:
        if a[i] < b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
    c += a[i:] + b[j:]
    return c


def split_and_merge(a):
    N1 = len(a) // 2
    a1 = a[:N1]
    a2 = a[N1:]

    if len(a1) > 1:
        a1 = split_and_merge(a1)
    if len(a2) > 1:
        a2 = split_and_merge(a2)

    return merge_list(a1, a2)


a = [9, 5, -3, 4, 7, 8, -8, 4]
a = split_and_merge(a)
print(a)
