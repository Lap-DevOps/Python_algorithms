"""
the Floyd–Warshall algorithm (also known as Floyd's algorithm, the Roy–Warshall algorithm, the Roy–Floyd algorithm,
or the WFI algorithm) is an algorithm for finding shortest paths in a directed weighted graph with positive
or negative edge weights (but with no negative cycles).
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


@ calculate_time
def get_path(P, u, v):
    """
    Finds a path between two vertices using the predecessor matrix P.
    :param P: the predecessor matrix
    :param u: the starting vertex
    :param v: the ending vertex
    :return: a list representing the path from u to v
    """
    path = [u]
    while u != v:
        u = P[u][v]
        path.append(u)
    return path


# Example graph represented as an adjacency matrix
V = [[0, 2, math.inf, 3, 1, math.inf, math.inf, 10],
     [2, 0, 4, math.inf, math.inf, math.inf, math.inf, math.inf],
     [math.inf, 4, 0, math.inf, math.inf, math.inf, math.inf, 3],
     [3, math.inf, math.inf, 0, math.inf, math.inf, math.inf, 8],
     [1, math.inf, math.inf, math.inf, 0, 2, math.inf, math.inf],
     [math.inf, math.inf, math.inf, math.inf, 2, 0, 3, math.inf],
     [math.inf, math.inf, math.inf, math.inf, math.inf, 3, 0, 1],
     [10, math.inf, 3, 8, math.inf, math.inf, 1, 0]]

N = len(V)
P = [[v for v in range(N)] for u in range(N)]

# Floyd-Warshall algorithm
for k in range(N):
    for i in range(N):
        for j in range(N):
            d = V[i][k] + V[k][j]
            if V[i][j] > d:
                V[i][j] = d
                P[i][j] = k

# Find path from vertex 0 to vertex 5
start = 0
end = 5
print(get_path(P, end, start))


# second way

@ calculate_time
def floyd_warshall(graph):
    """
    Finds the shortest path between all pairs of vertices in a graph using the Floyd-Warshall algorithm.
    :param graph: a square matrix representing the weighted edges between vertices, where a value of infinity
    represents no edge between vertices
    :return: a matrix of the shortest distances between all pairs of vertices
    """
    n = len(graph)
    dist = graph

    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist

print (floyd_warshall(V))