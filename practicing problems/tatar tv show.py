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
        s = data[idx+2]
        idx += 3
        ones_count = [0] * k
        for i in range(n):
            if s[i] == '1':
                ones_count[i % k] += 1
        possible = True
        for count in ones_count:
            if count % 2 != 0:
                possible = False
                break
                
        if possible:
            out.append("YES")
        else:
            out.append("NO")
            
    print('\n'.join(out))
solve()
