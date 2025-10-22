from collections import deque

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

print("BFS Traversal starting from node 3:")
bfs_result = BFS(n, adjacency_list, 3)
print(bfs_result)  # Output: [3, 2, 4, 1, 5, 6, 7, 8, 9]