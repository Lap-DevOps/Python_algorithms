"""
Dijkstra's algorithm (/ˈdaɪkstrəz/ DYKE-strəz) is an algorithm for finding the shortest paths between nodes in a
weighted graph, which may represent, for example, road networks. It was conceived by computer scientist
 Edsger W. Dijkstra in 1956 and published three years later.
"""

import math
import time

def calculate_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function '{func.__name__}' took {end_time - start_time:.6f} seconds to run.")
        return result
    return wrapper



def get_link_v(v, D):
    # This function returns the indexes of the non-zero elements
    # in the row of the matrix D corresponding to the vertex v.
    # These indexes represent the vertices that are connected to v.
    for i, weight in enumerate(D[v]):
        if weight > 0:
            yield i


def arg_min(T, S):
    # This function returns the index of the vertex with the
    # smallest tentative distance in T that is not already in S.
    # T is a list of tentative distances, and S is a set of
    # vertices that have been explored.
    amin = -1
    m = max(T)
    for i, t in enumerate(T):
        if t < m and i not in S:
            m = t
            amin = i
    return amin


# Define the adjacency matrix for the graph.
D = ((0, 3, 1, 3, 0, 0),
     (3, 0, 4, 0, 0, 0),
     (1, 4, 0, 0, 7, 5),
     (3, 0, 0, 0, 0, 2),
     (0, 0, 7, 0, 0, 4),
     (0, 0, 5, 2, 4, 0))

N = len(D)
T = [math.inf] * N

v = 0
S = {v}
T[v] = 0

while v != -1:
    # Update the tentative distances of the vertices
    # that are connected to v and not yet in S.
    for j in get_link_v(v, D):
        if j not in S:
            w = T[v] + D[v][j]
            if w < T[j]:
                T[j] = w

    # Choose the vertex with the smallest tentative distance
    # that is not yet in S and add it to S.
    v = arg_min(T, S)
    if v > 0:
        S.add(v)

# Print the final list of tentative distances.
print(T)


# second way
@ calculate_time
def dijkstra(graph, start):
    distances = {node: {} for node in graph}
    for node in graph:
        for neighbor in graph[node]:
            distances[node][neighbor] = graph[node][neighbor]
    unvisited = {node: None for node in graph}  # using None as +inf
    visited = {}
    current = start
    currentDistance = 0
    unvisited[current] = currentDistance
    while True:
        for neighbor, distance in graph[current].items():
            if neighbor not in unvisited: continue
            newDistance = currentDistance + distance
            if unvisited[neighbor] is None or unvisited[neighbor] > newDistance:
                unvisited[neighbor] = newDistance
        visited[current] = currentDistance
        del unvisited[current]
        if not unvisited: break
        candidates = [node for node in unvisited.items() if node[1]]
        if not candidates: break
        current, currentDistance = sorted(candidates, key = lambda x: x[1])[0]
    return visited


graph = {
    'A': {'B': 2, 'C': 4},
    'B': {'D': 3, 'E': 2},
    'C': {'F': 4},
    'D': {'G': 1},
    'E': {'G': 2},
    'F': {'G': 3},
    'G': {}
}

start = 'A'

distances = dijkstra(graph, start)

print(distances)


