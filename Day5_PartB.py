from sortedcontainers import SortedSet

def solve():
    with open("Day5_Input.txt") as f:
        database = [s.strip('\n') for s in f.readlines()]
    
    fresh_ingrediantes = SortedSet()
    
    for row in database:
        if len(row) == 0:
          break

        l = list(map(int, row.split("-")))
        start, end = l[0], l[1]

        fresh_ingrediantes.add((start, end))
    
    current_walk = (0, 0)
    new_walks = []
    #O(n)
    for fi in fresh_ingrediantes:
        if current_walk == (0,0):
            current_walk = fi
            continue

        # new interval
        if fi[0] > current_walk[1]:
            new_walks.append(current_walk)
            current_walk = fi
            continue
        elif fi[0] == current_walk[1]:
            current_walk = (current_walk[0], fi[1])
            continue
        elif fi[1] >= current_walk[1]:
            if (current_walk[0] <= fi[0] < current_walk[1]) or \
               (current_walk[0] < fi[0] <= current_walk[1]):
                current_walk = (current_walk[0], fi[1])
                continue
            
    new_walks.append(current_walk)

    print(new_walks)
    total_walks = 0
    for nw in new_walks:
        total_walks += (nw[1] - nw[0] + 1)
    
    # 328809021493328 too low
    # 347338785050534 wrong answer
    # 347338785050518
    # 347338785050515
    return total_walks

if __name__ == "__main__":
    print("Total available ingredients: ", solve())