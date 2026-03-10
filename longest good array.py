import sys
import math
def solve():
    a = sys.stdin.read().split()
    if not a:
        return
    b = int(a[0])
    r = []
    c = 1
    for _ in range(b):
        d = int(a[c])
        e = int(a[c+1])
        c += 2
        f = e - d
        if f == 0:
            r.append("1")
            continue
        g = (1 + math.isqrt(1 + 8*f)) // 2
        r.append(str(g))
    sys.stdout.write("\n".join(r))
solve()