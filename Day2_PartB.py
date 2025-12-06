def check_invalid_id(str_i, divider):
    if len(str_i) % divider == 0:
        chunks = [str_i[i:i + divider] for i in range(0, len(str_i), divider)]

        reference_chunk = chunks[0]

        if all(chunk == reference_chunk for chunk in chunks):
            return int(str_i)

    return -1

def calculated_invalid_ids(start, end, cache):
    invalid_ids = 0
    for i in range(start, end + 1):
        str_i = str(i)
        if i in cache:
            invalid_ids += cache[i]
            continue

        for divider in reversed(range(1, (len(str_i) // 2) + 1)):
            result = check_invalid_id(str_i, divider)            

            if result != -1:
                cache[i] = result
                invalid_ids += result    
                break            
        
    return invalid_ids

with open("Day2_Input.txt") as file:
    ranges = file.read().strip().split(",")

total_sum = 0
cache = {}
for r in ranges:
    start_range = int(r.split("-")[0])
    end_range = int(r.split("-")[1])
    total_sum += calculated_invalid_ids(start_range, end_range, cache)

print(f"Total Invalid Ids: {total_sum}")