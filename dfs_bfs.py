from collections import deque

def dfs(node, visited, graph):
    visited[node] = True
    print(node, end=" ")
    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs(neighbor, visited, graph)

def bfs(start, graph):
    visited = [False] * len(graph)
    queue = deque([start])
    visited[start] = True

    while queue:
        node = queue.popleft()
        print(node, end=" ")
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)

# --- Example Input  ---

V = 5   # number of vertices
E = 4   # number of edges
edges = [
    (0, 1),
    (0, 2),
    (1, 3),
    (2, 4)
]

# --- Building the Graph ---
graph = [[] for _ in range(V)]
for u, v in edges:
    graph[u].append(v)
    graph[v].append(u)  # undirected graph

# --- DFS and BFS Traversal ---
print("DFS Traversal:", end=" ")
visited = [False] * V
dfs(0, visited, graph)

print("\nBFS Traversal:", end=" ")
bfs(0, graph)
