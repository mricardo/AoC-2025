from collections import deque

def get_neighbours(current_node, max_width, max_height):
    neighbours = []
    x, y = current_node

    neighbours.append((x + 1, y)) if x + 1 < max_width else None
    neighbours.append((x - 1, y)) if x - 1 >= 0 else None
    neighbours.append((x, y + 1)) if y + 1 < max_height else None
    neighbours.append((x, y - 1)) if y - 1 >= 0 else None
    neighbours.append((x - 1, y - 1))  if x - 1 >= 0 and y - 1 >= 0 else None
    neighbours.append((x + 1, y - 1)) if x + 1 < max_width and y - 1 >= 0 else None
    neighbours.append((x - 1, y + 1)) if x - 1 >= 0 and y + 1 < max_height else None
    neighbours.append((x + 1, y + 1)) if x + 1 < max_width and y + 1 < max_height else None

    return neighbours

def bfs(puzzle, start_node, max_width, max_height):
    # Keep track of visited nodes to avoid infinite loops
    visited = set()
    # Create a queue and enqueue the starting node
    queue = deque([start_node])
    visited.add(start_node)
    
    total_rolls_paper = 0

    result = []

    while queue:
        # Dequeue a vertex from the front
        current_node = queue.popleft()
        current_node_value = puzzle[current_node[0]][current_node[1]]
           
        neighbours = get_neighbours(current_node, max_width, max_height)
        
        # Look at all neighbors of the current node
        total_neighbours = 0
        for neighbor in neighbours:
            if neighbor is None:
                continue

            neighbor_value = puzzle[neighbor[0]][neighbor[1]]
        
            if current_node_value == "@" and neighbor_value == "@":                
                total_neighbours += 1

            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                
        if total_neighbours < 4 and current_node_value == "@":
            result.append(current_node)
            total_rolls_paper += 1
                
    return (result, total_rolls_paper)

with open("Day4_Input.txt") as f:
    content = f.readlines()

puzzle = []
for row in content:
    puzzle.append(list(row.strip()))

total_rolls_paper_removed = 0

while True:
    total_rolls_paper = bfs(puzzle, (0, 0), len(puzzle[0]), len(puzzle))
    if total_rolls_paper[1] == 0:
        break

    total_rolls_paper_removed += total_rolls_paper[1]

    for node in total_rolls_paper[0]:
        puzzle[node[0]][node[1]] = "."

print("Total rolls paper removed:", total_rolls_paper_removed)