import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    ptr = 0
    t = int(input_data[ptr])
    ptr += 1
    
    results = []
    
    for _ in range(t):
        n = int(input_data[ptr])
        ptr += 1
        a = list(map(int, input_data[ptr : ptr + n]))
        ptr += n
        max_neat_len = 0
        dp = 0 
        pos = {}
        best_at_index = [0] * (n + 1)
        count = {}
        history = {}

        for i in range(n):
            val = a[i]
            if val > n:
                best_at_index[i+1] = best_at_index[i]
                continue
            
            if val not in count:
                count[val] = 0
                history[val] = []
            history[val].append(best_at_index[i])
            count[val] += 1
            
            current_best = best_at_index[i]
            if count[val] >= val:
                prev_dp = history[val][count[val] - val]
                current_best = max(current_best, prev_dp + val)
            
            best_at_index[i+1] = current_best
            
        results.append(str(best_at_index[n]))

    sys.stdout.write("\n".join(results) + "\n")
solve()