"""
In computer science, the Knuth–Morris–Pratt algorithm (or KMP algorithm) is a string-searching algorithm that
 searches for occurrences of a "word" W within a main "text string" S by employing the observation that when
 a mismatch occurs, the word itself embodies sufficient information to determine where the next match could begin,
 thus bypassing re-examination of previously matched characters.
 Some applications of the KMP algorithm include text editors (for finding and highlighting occurrences of a search
 term), bioinformatics (for searching for patterns in DNA sequences), and data compression (for finding repeated
 patterns in data).
"""

# creating prefix

pattern = "лилила"
pi = [0] * len(pattern)

# counters
j = 0
i = 1

while i < len(pattern):
    if pattern[j] == pattern[i]:
        pi[i] = j + 1
        i += 1
        j += 1
    else:
        if j == 0:
            pi[i] = 0
            i += 1
        else:
            j = pi[j - 1]

print(f"Prefix to '{pattern}' = {pi}")

# search for the pattern in the text

text = "лилилось лилилась"
m = len(pattern)
n = len(text)

i = 0
j = 0
while i < n:
    if text[i] == pattern[j]:
        i += 1
        j += 1
        if j == m:
            print("We've found pattern!")
            break
    else:
        if j > 0:
            j = pi[j - 1]
        else:
            i += 1
if i == n:
    print("We haven't found pattern!")


# second variant

def kmp(text, pattern):
    n = len(text)
    m = len(pattern)
    pi = compute_prefix_function(pattern)
    matches = []
    j = 0
    for i in range(n):
        while j > 0 and text[i] != pattern[j]:
            j = pi[j - 1]
        if text[i] == pattern[j]:
            j += 1
        if j == m:
            matches.append(i - m + 1)
            j = pi[j - 1]
    return matches


def compute_prefix_function(pattern):
    m = len(pattern)
    pi = [0] * m
    j = 0
    for i in range(1, m):
        while j > 0 and pattern[j] != pattern[i]:
            j = pi[j - 1]
        if pattern[j] == pattern[i]:
            j += 1
        pi[i] = j
    return pi


text = "ababaababcbababcbababcbbababcbcababcaababcaabcbababcbaababcbcbaaababcbcababaababcbababcbababcbbababcbcababcaababcaabcbababcbaababcbcbaaababcbcababaababcbababcbababcbbababcbcababcaababcaabcbababcbaababcbcbaaababcbcababaababcbababcbababcbbababcbcababcaababcaabcbababcbaababcbcbaaababcbca"
pattern = "ababcbca"
matches = kmp(text, pattern)
print(matches)