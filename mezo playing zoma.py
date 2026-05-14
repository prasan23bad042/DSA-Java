import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    t = int(input_data[0])
    idx = 1
    
    for _ in range(t):
        n = int(input_data[idx])
        idx += 1
        a = []
        for _ in range(n):
            a.append(int(input_data[idx]))
            idx += 1
        if n == 1:
            print(0)
            continue
            
        max_kept = 1
        for i in range(n):
            for j in range(n):
                min_val = a[i]
                max_val = a[j]
                if min_val <= max_val and (min_val + max_val) % 2 == 0:
                    current_count = 0
                    for x in a:
                        if min_val <= x <= max_val:
                            current_count += 1
                    
                    if current_count > max_kept:
                        max_kept = current_count
        print(n - max_kept)
solve()