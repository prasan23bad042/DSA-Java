import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    
    if not data:
        return

    t = int(data[0])
    idx = 1
    
    out = []
    for _ in range(t):
        n = int(data[idx])
        h = [int(x) for x in data[idx + 1 : idx + 1 + n]]
        idx += 1 + n
        min_k = max(h) - min(h) + 1
        out.append(str(min_k))
        
    print('\n'.join(out))
solve()
