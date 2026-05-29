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
        reviewers = data[idx+1 : idx+1+n]
        upvotes = 0
        for r in reviewers:
            if r == '1' or r == '3':
                upvotes += 1
                
        out.append(str(upvotes))
        idx += 1 + n
    print('\n'.join(out))
solve()