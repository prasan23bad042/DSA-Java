import sys

def solve():
    input = sys.stdin.read().split()
    if not input:
        return
    
    idx = 0
    t = int(input[idx])
    idx += 1
    INF = float('inf')
    
    results = []
    
    for _ in range(t):
        n = int(input[idx])
        idx += 1
        min_10 = INF
        min_01 = INF
        min_11 = INF
        
        for i in range(n):
            m = int(input[idx])
            s = input[idx + 1]
            idx += 2
            if s == "11":
                min_11 = min(min_11, m)
            elif s == "10":
                min_10 = min(min_10, m)
            elif s == "01":
                min_01 = min(min_01, m)
        ans = min(min_11, min_10 + min_01)
        
        if ans == INF:
            results.append("-1")
        else:
            results.append(str(ans))
            
    sys.stdout.write("\n".join(results) + "\n")
solve()