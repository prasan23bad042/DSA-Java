import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    t = int(input_data[0])
    results = []
    
    for i in range(1, t + 1):
        n = int(input_data[i])
        if n % 2 != 0:
            results.append("NO")
        else:
            results.append("YES")
            pairs_needed = n // 2
            
            ans = []
            for j in range(pairs_needed):
                if j % 2 == 0:
                    ans.append("AA")
                else:
                    ans.append("BB")
            results.append("".join(ans))
    print("\n".join(results))
solve()