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
        x = int(data[idx])
        y = int(data[idx+1])
        idx += 2
        if x % 2 != 0 and y % 2 != 0:
            results.append("NO")
        else:
            results.append("YES")
    print('\n'.join(results))
solve()
