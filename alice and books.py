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
        max_other_book = max(a[:-1])
        ans = max_other_book + a[-1]
        out.append(str(ans))
        
    print('\n'.join(out))
solve()