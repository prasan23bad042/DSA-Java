import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    t = int(input_data[0])
    pointer = 1
    results = []
    
    for _ in range(t):
        r = int(input_data[pointer])
        b = int(input_data[pointer + 1])
        d = int(input_data[pointer + 2])
        pointer += 3
        small = min(r, b)
        large = max(r, b)
        if large <= small * (1 + d):
            results.append("YES")
        else:
            results.append("NO")
    sys.stdout.write("\n".join(results) + "\n")
solve()