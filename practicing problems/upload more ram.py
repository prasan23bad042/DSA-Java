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
        n = int(data[idx])
        k = int(data[idx+1])
        idx += 2
        ans = (n - 1) * k + 1
        results.append(str(ans))
    print('\n'.join(results))
solve()