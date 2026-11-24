import heapq

# 1. Heuristic: Count misplaced tiles (ignoring 0)
def h(state, goal):
    return sum(1 for i in range(9) if state[i] != 0 and state[i] != goal[i])

# 2. Generate valid neighbor states
def get_neighbors(state):
    neighbors = []
    idx = state.index(0)       # Find blank tile (0)
    r, c = divmod(idx, 3)      # Convert 1D index to (row, col)
    
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < 3 and 0 <= nc < 3:
            new_idx = nr * 3 + nc
            lst = list(state)
            lst[idx], lst[new_idx] = lst[new_idx], lst[idx]
            neighbors.append(tuple(lst))
    return neighbors

# 3. A* Search
def a_star(start, goal):
    pq = [(h(start, goal), 0, start, [start])]  # (f_score, g_score, state, path)
    visited = set()

    while pq:
        f, g, curr, path = heapq.heappop(pq)
        if curr == goal:
            return path
        if curr in visited:
            continue
        visited.add(curr)

        for nxt in get_neighbors(curr):
            if nxt not in visited:
                heapq.heappush(pq, (g + 1 + h(nxt, goal), g + 1, nxt, path + [nxt]))
    return None

# --- Main ---
start = tuple(map(int, input("Start (9 numbers): ").split()))
goal = tuple(map(int, input("Goal (9 numbers): ").split()))

solution = a_star(start, goal)
if solution:
    for step in solution:
        print(step[:3], "\n", step[3:6], "\n", step[6:], "\n")
else:
    print("No solution")