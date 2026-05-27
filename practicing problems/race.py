import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    
    if not data:
        return
        
    t = int(data[0])
    results = []
    
    idx = 1
    for _ in range(t):
        a = int(data[idx])
        x = int(data[idx+1])
        y = int(data[idx+2])
        idx += 3
        dx = abs(a - x)
        dy = abs(a - y)
        left_bound = max(x - dx, y - dy)
        right_bound = min(x + dx, y + dy)
        if right_bound - left_bound >= 2:
            results.append("YES")
        else:
            results.append("NO")
            
    print('\n'.join(results))
solve()