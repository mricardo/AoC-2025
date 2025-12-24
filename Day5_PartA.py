def solve():
    with open("Day5_Input.txt") as f:
        database = [s.strip('\n') for s in f.readlines()]
    
    fresh_ingrediantes = []
    available_ingredients = []
    record_available_ingredients = False
    for row in database:
        if len(row) == 0:
          record_available_ingredients = True
          continue

        if not record_available_ingredients:            
            fresh_ingrediantes.append(list(map(int,row.split("-"))))
        
        if record_available_ingredients:
            available_ingredients.append(int(row))
        
    total_available_ingredients = 0
    for ai in available_ingredients:
        for fi in fresh_ingrediantes:
            if ai>= fi[0] and ai <= fi[1]:
                total_available_ingredients += 1
                break
    
    print("Total available ingredients: ", total_available_ingredients)

if __name__ == "__main__":
    solve()