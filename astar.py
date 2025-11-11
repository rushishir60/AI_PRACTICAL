from heapq import heappop, heappush

def heuristic(a, b):
    # Manhattan distance as heuristic
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def astar(start, goal, grid):
    rows, cols = len(grid), len(grid[0])
    open_list = []
    heappush(open_list, (0 + heuristic(start, goal), 0, start, [start]))
    visited = set()

    while open_list:
        f, g, node, path = heappop(open_list)
        if node == goal:
            return path
        if node in visited:
            continue
        visited.add(node)

        x, y = node
        for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 0:
                new_cost = g + 1
                heappush(open_list, (new_cost + heuristic((nx, ny), goal), new_cost, (nx, ny), path + [(nx, ny)]))

    return None

# --- Main program ---
grid = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0]
]

start = (0, 0)
goal = (4, 4)

path = astar(start, goal, grid)
print("Shortest Path found by A*:", path)
