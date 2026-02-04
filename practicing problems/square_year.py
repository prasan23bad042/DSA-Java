import math
import sys
d = sys.stdin.read().split()
if not d:
    sys.exit()
t = int(d[0])
r = []
idx = 1
for _ in range(t):
    s = d[idx]
    idx += 1
    n = int(s)
    x = int(math.isqrt(n))
    if x * x == n:
        r.append(f"0 {x}")
    else:
        r.append("-1")
sys.stdout.write("\n".join(r) + "\n")
