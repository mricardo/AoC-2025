def solve():
    with open("Day5_Input.txt") as f:
        database = [s.strip('\n') for s in f.readlines()]
    
    fresh_ingrediants = []
    
    for row in database:
        if len(row) == 0:
          break

        l = list(map(int, row.split("-")))
        start, end = l[0], l[1]

        fresh_ingrediants.append((start, end))
    
    fresh_ingrediants.sort()
    curr_start, curr_end = fresh_ingrediants[0]
    new_walks = []
    
    for next_start, next_end in fresh_ingrediants[1:]:        
        if next_start <= curr_end + 1:
            curr_end = max(curr_end, next_end)
        else:
            new_walks.append((curr_start, curr_end))
            curr_start, curr_end = next_start, next_end
            
    new_walks.append((curr_start, curr_end))
    total_walks = sum(end - start + 1 for start, end in new_walks)

    return total_walks

if __name__ == "__main__":
    print("Total available ingredients: ", solve())