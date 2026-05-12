import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    t = int(input_data[0])
    pointer = 1
    results = []
    
    for _ in range(t):
        n = int(input_data[pointer])
        pointer += 1
        count_map = {}
        
        for i in range(1, n + 1):
            val = int(input_data[pointer])
            pointer += 1
            
            if val in count_map:
                count_map[val][0] += 1
            else:
                count_map[val] = [1, i]
        
        min_unique_val = float('inf')
        winner_index = -1
        for val, info in count_map.items():
            count = info[0]
            index = info[1]
            
            if count == 1:
                if val < min_unique_val:
                    min_unique_val = val
                    winner_index = index
        
        results.append(str(winner_index))
    sys.stdout.write("\n".join(results) + "\n")
solve()