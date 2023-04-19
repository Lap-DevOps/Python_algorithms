import math


def get_max_vertex(k, V, S):
    m = 0  # наименьшее допустимое значение
    v = -1
    for i, w in enumerate(V[k]):
        if i in S:
            continue

        if w[2] == 1:  # движение по стрелке
            if m < w[0]:
                m = w[0]
                v = i
        else:  # движение против стрелки
            if m < w[1]:
                m = w[1]
                v = i

    return v


def get_max_flow(T):
    w = [x[0] for x in T]
    return min(*w)


def updateV(V, T, f):
    for t in T:
        if t[1] == -1:  # это исток
            continue

        sgn = V[t[2]][t[1]][2]  # направление движения

        # меняем веса в таблице для (i,j) и (j,i)
        V[t[1]][t[2]][0] -= f * sgn
        V[t[1]][t[2]][1] += f * sgn

        V[t[2]][t[1]][0] -= f * sgn
        V[t[2]][t[1]][1] += f * sgn


V = [[[0, 0, 1], [20, 0, 1], [30, 0, 1], [10, 0, 1], [0, 0, 1]],
     [[20, 0, -1], [0, 0, 1], [40, 0, 1], [0, 0, 1], [30, 0, 1]],
     [[30, 0, -1], [40, 0, -1], [0, 0, 1], [10, 0, 1], [20, 0, 1]],
     [[10, 0, -1], [0, 0, 1], [10, 0, -1], [0, 0, 1], [20, 0, 1]],
     [[0, 0, 1], [30, 0, -1], [20, 0, -1], [20, 0, -1], [0, 0, 1]],
     ]

N = len(V)  # число вершин в графе
init = 0  # вершина истока (нумерация с нуля)
end = 4  # вершина стока
Tinit = (math.inf, -1, init)  # первая метка маршруто (a, from, vertex)
f = []  # максимальные потоки найденных маршрутов

j = init
while j != -1:
    k = init  # стартовая вершина (нумерация с нуля)
    T = [Tinit]  # метки маршрута
    S = {init}  # множество просмотренных вершин

    while k != end:  # пока не дошли до стока
        j = get_max_vertex(k, V, S)  # выбираем вершину с наибольшей пропускной способностью
        if j == -1:  # если следующих вершин нет
            if k == init:  # и мы на истоке, то
                break  # завершаем поиск маршрутов
            else:  # иначе, переходим к предыдущей вершине
                k = T.pop()[2]
                continue

        c = V[k][j][0] if V[k][j][2] == 1 else V[k][j][1]  # определяем текущий поток
        T.append((c, j, k))  # добавляем метку маршрута
        S.add(j)  # запоминаем вершину как просмотренную

        if j == end:  # если дошди до стока
            f.append(get_max_flow(T))  # находим максимальную пропускную способность маршрута
            updateV(V, T, f[-1])  # обновляем веса дуг
            break

        k = j

F = sum(f)
print(f"Максимальный поток равен: {F}")


# second version

# Define a function to implement the Ford-Fulkerson algorithm
def ford_fulkerson(graph, source, sink):
    # Initialize the maximum flow to zero
    max_flow = 0

    # Create a residual graph with capacities initialized to the original graph
    residual_graph = [[graph[i][j] for j in range(len(graph[0]))] for i in range(len(graph))]

    # Define a function to find the augmenting path in the residual graph
    def bfs(residual_graph, source, sink, parent):
        # Create a visited array to keep track of visited nodes
        visited = [False] * len(residual_graph)

        # Mark the source node as visited and add it to the queue
        queue = []
        queue.append(source)
        visited[source] = True

        # While the queue is not empty
        while queue:
            # Dequeue a node from the queue and mark it as visited
            u = queue.pop(0)
            visited[u] = True

            # Check all adjacent nodes of the dequeued node
            for v in range(len(residual_graph)):
                # If a node is not visited, and there is capacity in the residual graph, add it to the queue and mark its parent
                if visited[v] == False and residual_graph[u][v] > 0:
                    queue.append(v)
                    parent[v] = u

        # If we can reach the sink node, return True, else False
        return True if visited[sink] else False

    # Find the augmenting path in the residual graph and add its flow to the maximum flow
    while bfs(residual_graph, source, sink, parent := [-1] * len(graph)):
        # Initialize the path flow to infinity
        path_flow = float('inf')

        # Traverse the augmenting path and find the minimum capacity
        v = sink
        while v != source:
            u = parent[v]
            path_flow = min(path_flow, residual_graph[u][v])
            v = u

        # Update the capacities of the edges and reverse edges along the augmenting path
        v = sink
        while v != source:
            u = parent[v]
            residual_graph[u][v] -= path_flow
            residual_graph[v][u] += path_flow
            v = u

        # Add the path flow to the maximum flow
        max_flow += path_flow

    # Return the maximum flow
    return max_flow


# Sample graph
graph = [[0, 16, 13, 0, 0, 0],
         [0, 0, 10, 12, 0, 0],
         [0, 4, 0, 0, 14, 0],
         [0, 0, 9, 0, 0, 20],
         [0, 0, 0, 7, 0, 4],
         [0, 0, 0, 0, 0, 0]]

# Source node
source = 0

# Sink node
sink = 5

# Call the ford_fulkerson function with the sample graph, source, and sink
max_flow = ford_fulkerson(graph, source, sink)

# Print the maximum flow
print("Maximum flow:", max_flow)
