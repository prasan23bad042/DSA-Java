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
        k = int(data[idx+1])
        idx += 2
        
        b = [int(x) for x in data[idx : idx + n]]
        idx += n
        
        prod_b = 1
        for num in b:
            prod_b *= num
            
        if 2023 % prod_b == 0:
            out.append("YES")
            missing_elements = [2023 // prod_b] + [1] * (k - 1)
            out.append(" ".join(map(str, missing_elements)))
        else:
            out.append("NO")
            
    print("\n".join(out))
solve()
