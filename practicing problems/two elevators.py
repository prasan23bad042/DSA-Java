import sys
d = sys.stdin.read().split()
i = 0
t = int(d[i])
i += 1
o = []
for _ in range(t):
    a = int(d[i]); b = int(d[i+1]); c = int(d[i+2])
    i += 3
    t1 = abs(a - 1)
    t2 = abs(b - c) + abs(c - 1)
    if t1 < t2:
        o.append("1")
    elif t2 < t1:
        o.append("2")
    else:
        o.append("3")
print("\n".join(o))
