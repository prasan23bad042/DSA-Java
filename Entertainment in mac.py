import sys

def solve():
    # Fast I/O
    input = sys.stdin.read
    data = input().split()
    
    if not data:
        return
    
    t = int(data[0])
    results = []
    idx = 1
    
    for _ in range(t):
        n = int(data[idx])
        s = data[idx+1]
        idx += 2
        
        # Generate the reversed string
        rev_s = s[::-1]
        
        # Decision rule based on our deep analysis
        if s <= rev_s:
            results.append(s)
        else:
            results.append(rev_s + s)
            
    # Print all results separated by a newline
    print('\n'.join(results))

if __name__ == '__main__':
    solve()
