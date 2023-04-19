"""
In computer science, Prim's algorithm (also known as Jarník's algorithm) is a greedy algorithm that finds a minimum
spanning tree for a weighted undirected graph. This means it finds a subset of the edges that forms a tree that
includes every vertex, where the total weight of all the edges in the tree is minimized. The algorithm operates by
building this tree one vertex at a time, from an arbitrary starting vertex, at each step adding the cheapest possible
connection from the tree to another vertex.
"""

#-------------------------------------------------
# Алгоритм Прима поиска минимального остова графа
#-------------------------------------------------
import math


def get_min(R, U):
    rm = (math.inf, -1, -1)
    for v in U:
        rr = min(R, key=lambda x: x[0] if (x[1] == v or x[2] == v) and (x[1] not in U or x[2] not in U) else math.inf)
        if rm[0] > rr[0]:
            rm = rr

    return rm


# список ребер графа (длина, вершина 1, вершина 2)
# первое значение возвращается, если нет минимальных ребер
R = [(math.inf, -1, -1), (13, 1, 2), (18, 1, 3), (17, 1, 4), (14, 1, 5), (22, 1, 6),
     (26, 2, 3), (19, 2, 5), (30, 3, 4), (22, 4, 6)]

N = 6     # число вершин в графе
U = {1}   # множество соединенных вершин
T = []    # список ребер остова

while len(U) < N:
    r = get_min(R, U)       # ребро с минимальным весом
    if r[0] == math.inf:    # если ребер нет, то остов построен
        break

    T.append(r)             # добавляем ребро в остов
    U.add(r[1])             # добавляем вершины в множество U
    U.add(r[2])

print(T)


# second variant

import heapq


def prim(graph, start):
    # Initialize an empty set to store the MST
    mst = set()

    # Initialize a set to store the nodes visited by the algorithm
    visited = set([start])

    # Initialize a priority queue to store the edges of the graph
    edges = [(weight, start, dest) for dest, weight in graph[start].items()]
    heapq.heapify(edges)

    # Traverse the edges of the graph until all nodes are visited
    while edges:
        # Get the edge with the minimum weight from the priority queue
        weight, source, dest = heapq.heappop(edges)

        # If the destination node has not been visited yet, add the edge to the MST and mark the destination node as visited
        if dest not in visited:
            visited.add(dest)
            mst.add((source, dest, weight))

            # Add the edges of the destination node to the priority queue
            for next_dest, next_weight in graph[dest].items():
                if next_dest not in visited:
                    heapq.heappush(edges, (next_weight, dest, next_dest))

    # Return the MST as a list
    return list(mst)

# Sample graph represented as a dictionary of dictionaries
graph = {
    'A': {'B': 2, 'D': 3},
    'B': {'A': 2, 'C': 1, 'D': 4},
    'C': {'B': 1, 'D': 2},
    'D': {'A': 3, 'B': 4, 'C': 2}
}

# Call the prim() function with the starting node 'A'
mst = prim(graph, 'A')

# Print the MST
print(mst)

