# Link State Routing (Simple Example)

graph = {
    'A': {'B': 2, 'C': 5},
    'B': {'A': 2, 'C': 1, 'D': 2},
    'C': {'A': 5, 'B': 1, 'D': 3, 'E': 1},
    'D': {'B': 2, 'C': 3, 'E': 2},
    'E': {'C': 1, 'D': 2}
}

def dijkstra(start):
    visited = set()
    distance = {node: 999 for node in graph}
    distance[start] = 0

    while len(visited) < len(graph):
        # pick node with smallest distance
        min_node = None
        for node in graph:
            if node not in visited:
                if min_node is None or distance[node] < distance[min_node]:
                    min_node = node

        visited.add(min_node)

        for neighbor, cost in graph[min_node].items():
            if distance[min_node] + cost < distance[neighbor]:
                distance[neighbor] = distance[min_node] + cost

    return distance

# show shortest paths from each router
for node in graph:
    result = dijkstra(node)
    print(f"\nRouter {node}:")
    for dest in result:
        print(f"To {dest} : Cost = {result[dest]}")
