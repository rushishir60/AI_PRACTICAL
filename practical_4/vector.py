# Distance Vector Routing (Simple Example)

# network represented as a dictionary
graph = {
    'A': {'B': 2, 'C': 5},
    'B': {'A': 2, 'C': 1, 'D': 2},
    'C': {'A': 5, 'B': 1, 'D': 3, 'E': 1},
    'D': {'B': 2, 'C': 3, 'E': 2},
    'E': {'C': 1, 'D': 2}
}

# initialize routing tables (distance from each router to others)
dist = {}
for node in graph:
    dist[node] = {}
    for other in graph:
        if node == other:
            dist[node][other] = 0
        elif other in graph[node]:
            dist[node][other] = graph[node][other]
        else:
            dist[node][other] = 999  # infinity

# run distance vector algorithm
for _ in range(len(graph) - 1):
    for u in graph:
        for v in graph[u]:
            for d in graph:
                if dist[u][d] > graph[u][v] + dist[v][d]:
                    dist[u][d] = graph[u][v] + dist[v][d]

# print final routing tables
for node in dist:
    print(f"\nRouting table for {node}:")
    for dest in dist[node]:
        print(f"To {dest} : Cost = {dist[node][dest]}")
