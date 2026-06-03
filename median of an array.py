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
        a = [int(x) for x in data[idx + 1 : idx + 1 + n]]
        idx += 1 + n
        a.sort()
        median_idx = ((n + 1) // 2) - 1
        
        target = a[median_idx]
        operations = 0
        for i in range(median_idx, n):
            if a[i] == target:
                operations += 1
            else:
                break
                
        out.append(str(operations))
    print('\n'.join(out))
solve()