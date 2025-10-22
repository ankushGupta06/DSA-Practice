n = 5
e = 6
edges = [[1,2], [1,3], [2,4], [3,4], [4,5], [3,5]]
directed_edges = [[1,2], [1,3], [2,4], [3,4], [4,5], [3,5]]

# storing the graph using matrix
print("Graph represented as an adjacency matrix:")
graph_matrix = [[0 for i in range(n+1)] for j in range(n+1)]

for u, v in edges:
    graph_matrix[u][v] = 1
    graph_matrix[v][u] = 1

for i in range(1, n+1):
    print(graph_matrix[i])


#storing the graph using adjacency list
print("\n Graph represented as an adjacency list:")
graph_list = [[] for _ in range(n+1)]

for u, v in edges:
    graph_list[u].append(v)
    graph_list[v].append(u)

for i in range(n+1):
    print(f"{i}: {graph_list[i]}")

# storing the graph using a dictionary
print("\n Graph represented as a dictionary:")
graph_dict = {}
for i in range(1, n+1):
    graph_dict[i] = []

for u,v in edges:
    graph_dict[u].append(v)
    graph_dict[v].append(u)

for key in graph_dict:
    print(f"{key}: {graph_dict[key]}")

#storing directed graph using adjacency matrix
print("\n Directed Graph represented as an adjacency matrix:")

directed_graph_matrix = [[0 for i in range(n+1)] for j in range(n+1)]

for u,v in directed_edges:
    directed_graph_matrix[u][v] = 1

for i in range(n+1):
    print(directed_graph_matrix[i])

# storing directed graph using adjacency list
print("\n Directed Graph represented as an adjacency list:")

directed_graph_list = [[] for _ in range(n+1)]

for u,v in directed_edges:
    directed_graph_list[u].append(v)

for i in range(n+1):
    print(f"{i}: {directed_graph_list[i]}")

# storing directed graph using a dictionary
print("\n Directed Graph represented as a dictionary:")
directed_graph_dict = {}

for i in range(1, n+1):
    directed_graph_dict[i] = []

for u,v in directed_edges:
    directed_graph_dict[u].append(v)

for key in directed_graph_dict:
    print(f"{key}: {directed_graph_dict[key]}")

