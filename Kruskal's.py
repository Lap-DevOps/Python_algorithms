'''
Kruskal's algorithm[1] finds a minimum spanning forest of an undirected edge-weighted graph. If the graph is connected,
 it finds a minimum spanning tree. (A minimum spanning tree of a connected graph is a subset of the edges that forms
 a tree that includes every vertex, where the sum of the weights of all the edges in the tree is minimized.
 For a disconnected graph, a minimum spanning forest is composed of a minimum spanning tree for each connected
 component.) It is a greedy algorithm in graph theory as in each step it adds the next lowest-weight edge that
 will not form a cycle to the minimum spanning forest
'''

R = [(13, 1, 2), (18, 1, 3), (17, 1, 4), (14, 1, 5), (22, 1, 6),
     (26, 2, 3), (22, 2, 5), (3, 3, 4), (19, 4, 6)]

Rs = sorted(R, key=lambda x: x[0])
U = set()
D = {}
T = []


for r in Rs:
     if r[1] not in U or r[2] not in U:
          if r[1] not in U and r[2] not in U:
               D[r[1]]= [r[1],r[2]]
               D[r[2]]=D[r[1]]
          else:
               if not D.get(r[1]):
                    D[r[2]].append(r[1])
                    D[r[1]]= D[r[2]]

               else:
                    D[r[1]].append(r[2])
                    D[r[2]]= D[r[1]]
          T.append(r)
          U.add(r[1])
          U.add(r[2])


for r in Rs:
     if r[1] in D[r[1]] and r[2] not in D[r[1]]:
          T.append(r)
          gr1=D[r[1]]
          D[r[1]] += D[r[2]]
          D[r[2]] += gr1

print(T)

#  second variant

# Define a function to implement Kruskal's algorithm
def kruskal(graph):
     # Create a dictionary to store the parents of each node
     parent = {}

     # Create a dictionary to store the rank of each node
     rank = {}

     # Define a function to find the parent of a node
     def find(node):
          # If the node is not its own parent, recursively find its parent
          if parent[node] != node:
               parent[node] = find(parent[node])

          # Return the parent of the node
          return parent[node]

     # Define a function to merge two sets
     def union(node1, node2):
          # Find the parents of each node
          root1 = find(node1)
          root2 = find(node2)

          # If the sets are already merged, return False
          if root1 == root2:
               return False

          # Merge the sets with the lower rank under the set with the higher rank
          if rank[root1] > rank[root2]:
               parent[root2] = root1
          elif rank[root1] < rank[root2]:
               parent[root1] = root2
          else:
               parent[root2] = root1
               rank[root1] += 1

          # Return True to indicate that the sets were merged
          return True

     # Initialize the parents and ranks of all nodes
     for node in graph['vertices']:
          parent[node] = node
          rank[node] = 0

     # Sort the edges in increasing order of weight
     edges = graph['edges']
     edges.sort()

     # Initialize an empty list to store the minimum spanning tree
     mst = []

     # Traverse the edges and add them to the minimum spanning tree if they don't form a cycle
     for edge in edges:
          weight, node1, node2 = edge

          if union(node1, node2):
               mst.append(edge)

     # Return the minimum spanning tree
     return mst


# Sample graph
graph = {
    'vertices': ['A', 'B', 'C', 'D', 'E', 'F', 'G'],
    'edges': [
        (7, 'A', 'B'),
        (5, 'A', 'D'),
        (7, 'B', 'A'),
        (8, 'B', 'C'),
        (9, 'B', 'D'),
        (7, 'B', 'E'),
        (8, 'C', 'B'),
        (5, 'C', 'E'),
        (5, 'D', 'A'),
        (9, 'D', 'B'),
        (7, 'D', 'E'),
        (6, 'D', 'F'),
        (7, 'E', 'B'),
        (5, 'E', 'C'),
        (15, 'E', 'D'),
        (8, 'E', 'F'),
]}

tree = kruskal(graph)
print(tree)





