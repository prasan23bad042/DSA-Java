import sys
d = sys.stdin.read().split()
i = 0
q = int(d[i])
i += 1
o = []
for _ in range(q):
    n = int(d[i])
    i += 1
    s = d[i]
    t = d[i+1]
    i += 2
    if sorted(s) == sorted(t):
        o.append("YES")
    else:
        o.append("NO")
print("\n".join(o))
