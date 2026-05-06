import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    t = int(input_data[0])
    out = []
    for i in range(1, t + 1):
        n = int(input_data[i])
        ans = []
        
        for j in range(n):
            if j % 2 == 0:
                ans.append("-1")
            else:
                if j == n - 1:
                    ans.append("2")
                else:
                    ans.append("3")
                    
        out.append(" ".join(ans))
    print("\n".join(out))
solve()