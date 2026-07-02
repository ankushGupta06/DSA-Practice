import heapq

def dijkstra(vertices, edges, src):
    # Build adjacency list
    adj_list = [[] for _ in range(vertices)]

    for u, v, w in edges:
        adj_list[u].append((v, w))

    # Distance array
    distance = [float("inf")] * vertices
    distance[src] = 0

    # Min-heap (distance, node)
    priority_queue = [(0, src)]

    while priority_queue:
        curr_dist, node = heapq.heappop(priority_queue)

        # Skip outdated entries
        if curr_dist > distance[node]:
            continue

        for adj_node, weight in adj_list[node]:
            new_dist = curr_dist + weight

            if new_dist < distance[adj_node]:
                distance[adj_node] = new_dist
                heapq.heappush(priority_queue, (new_dist, adj_node))

    return distance


# Example
vertices = 6
edges = [
    [0, 1, 4],
    [0, 2, 4],
    [1, 2, 2],
    [1, 3, 5],
    [2, 3, 5],
    [2, 4, 11],
    [3, 4, 2],
    [3, 5, 6],
    [4, 5, 3]
]

src = 0

distances = dijkstra(vertices, edges, src)

print("Shortest distances from source:", src)
for node in range(vertices):
    print(f"0 -> {node} = {distances[node]}")