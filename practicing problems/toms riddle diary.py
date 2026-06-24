import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    
    if not data:
        return
    n = int(data[0])
    names = data[1:]
    seen_names = set()
    for name in names:
        if name in seen_names:
            print("YES")
        else:
            print("NO")
            seen_names.add(name)
solve()
