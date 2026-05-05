import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    t = int(input_data[0])
    idx = 1
    
    results = []
    
    for _ in range(t):
        n = int(input_data[idx])
        idx += 1
        gears = input_data[idx : idx+n]
        idx += n
        if len(set(gears)) < len(gears):
            results.append("YES")
        else:
            results.append("NO")
    print('\n'.join(results))
solve()