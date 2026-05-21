import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    
    if not data:
        return

    n = int(data[0])
    results = []
    idx = 1
    for _ in range(n):
        x = int(data[idx])
        y = int(data[idx+1])
        idx += 2
        if y >= -1:
            results.append("YES")
        else:
            results.append("NO")
    print('\n'.join(results))
solve()