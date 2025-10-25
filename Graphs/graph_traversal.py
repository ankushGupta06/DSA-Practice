from collections import deque

# This BFS is used to traverse the entire graph, including disconnected components.
def BFS_all(n, adj):
    visited = [0]*(n+1)
    ans = []

    def traversal(node, visited, graph):
        queue = deque()
        queue.append(node)
        visited[node] = 1

        while queue:
            current = queue.popleft()
            ans.append(current)
            for neighbor in graph[current]:
                if not visited[neighbor]:
                    visited[neighbor] = 1
                    queue.append(neighbor)

    for i in range(1,n+1):
        if not visited[i]:
            traversal(i, visited, adj)
    return ans

# This BFS is used to traverse a graph from a given starting node.
def BFS(n,adj, starting_node):
    ans = []
    queue = deque()
    visited = [0]*(n+1)

    queue.append(starting_node)
    visited[starting_node] = 1
    while queue:
        node = queue.popleft()
        ans.append(node)
        for neighbor in adjacency_list[node]:
            if not visited[neighbor]:
                visited[neighbor] = 1
                queue.append(neighbor)
    return ans

# This DFS is used to traverse the entire graph, including disconnected components.
def DFS(n, adj):
    visited = [0]*(n+1)
    ans = []

    def traversal(node, visited, graph):
        visited[node] = 1
        ans.append(node)
        for neighbor in graph[node]:
            if not visited[neighbor]:
                traversal(neighbor, visited, graph)

    for i in range(1,n+1):
        if not visited[i]:
            traversal(i, visited, adj)
    return ans


#This DFS is used to traverse a graph from a given starting node and only for the connected nodes.
def newDFS(node, result, visited, graph):
    visited[node] = 1
    result.append(node)
    for n in graph[node]:
        if visited[n] != 1:
            newDFS(n, result, visited, graph)


n = 9
adjacency_list = [
    [],
    [2,8],
    [1,3,4],
    [2],
    [2,5,6],
    [4,6],
    [5,7],
    [6,8],
    [1,7,9],
    [8]
]
print("BFS Traversal of the entire graph:")
bfs_all_result = BFS_all(n, adjacency_list)
print(bfs_all_result) # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]

print("BFS Traversal starting from node 3:")
bfs_result = BFS(n, adjacency_list, 3)
print(bfs_result)  # Output: [3, 2, 4, 1, 5, 6, 7, 8, 9]

print("\nDFS Traversal of the graph:")
dfs_result = DFS(n, adjacency_list)
print(dfs_result)

print("\nNew DFS Traversal starting from node 3:")
visited_nodes = [0]*(n+1)
new_dfs_result = []
newDFS(3, new_dfs_result, visited_nodes, adjacency_list)
print(new_dfs_result)  # Output: [3, 2, 1, 8, 7, 6, 5, 4, 9]