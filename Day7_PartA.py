from collections import deque

def bfs(lines, pos):
    queue = deque([pos])
    visited = {pos}
    taychon = 0

    while queue:
        x, y = queue.popleft()

        if lines[x][y] != "^":
            deltas = [(1, 0)]
        else:
            taychon += 1
            deltas = [(0, -1), (0, 1)]

        for dx, dy in deltas:
            new_pos = (x + dx, y + dy)
            new_x, new_y = new_pos
            if (0 <= new_x < len(lines) and
                    0 <= new_y < len(lines[0]) and
                    new_pos not in visited):
                visited.add(new_pos)
                queue.append(new_pos)

    return taychon


with open("Day7_input.txt") as f:
    lines = [line.rstrip() for line in f]

pos = next(
    (i, line.index("S"))
    for i, line in enumerate(lines)
    if "S" in line
)

print(bfs(lines, pos))