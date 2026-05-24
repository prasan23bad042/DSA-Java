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
        
        a = data[idx+1 : idx+1+n]
        distinct_a = len(set(a))
        
        b = data[idx+1+n : idx+1+2*n]
        distinct_b = len(set(b))
        
        if distinct_a + distinct_b >= 4:
            out.append("YES")
        else:
            out.append("NO")
            
        idx += 1 + 2 * n
        
    print('\n'.join(out))

if __name__ == '__main__':
    solve()
