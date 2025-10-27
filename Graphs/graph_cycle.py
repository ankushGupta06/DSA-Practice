from collections import deque
from inspect import stack

n = 7
adj_list = [[],[2,4],[1,3,6],[2],[1,5],[4,7],[2,7],[5,6]]

# Detection cycle in graph using Bredth First Search
def had_cycle(graph,starting_node):
    visited = [0]*(n+1)
    queue = deque()
    queue.append([starting_node,-1])
    
    while queue:
        current,parent = queue.popleft()
        visited[current] = 1
        for neighbor in graph[current]:
            if not visited[neighbor]:
                queue.append([neighbor,current])
            elif neighbor != parent:
                return True
    return False

# Detection cycle in graph using Depth First Search
def DFS_cycle(graph, starting_node):
    visited = [0]*(n+1)
    parent = {starting_node: -1}

    def dfs(node):
        visited[node] = 1
        for neighbor in graph[node]:
            if not visited[neighbor]:
                parent[neighbor] = node
                if dfs(neighbor):
                    return True
            elif parent[node] != neighbor:
                return True
        return False

    return dfs(starting_node)

# Detecting Cycle in graph using DFS for disconnected components
def had_cycle_DFS(graph):
    visited = [0]*(n+1)

    def dfs(node, parent):
        visited[node] = 1
        for neighbor in graph[node]:
            if not visited[neighbor]:
                if dfs(neighbor, node):
                    return True
            elif neighbor != parent:
                return True
        return False

    for i in range(1, n+1):
        if not visited[i]:
            if dfs(i, -1):
                return True
    return False



# Detecting Cycle in graph using BFS for disconnected components
def detect_cycle(graph):
    visited = [0]*(n+1)
    for i in range(1,n+1):
        if visited[i] == 1:
            continue
        
        queue = deque()
        queue.append([i,-1])
        while queue:
            current,parent = queue.popleft()
            visited[current] = 1
            for neighbor in graph[current]:
                if not visited[neighbor]:
                    queue.append([neighbor,current])
                elif neighbor != parent:
                    return True
    return False

print(had_cycle(adj_list,3))
print(detect_cycle(adj_list))
print(DFS_cycle(adj_list,3))
print(had_cycle_DFS(adj_list))

