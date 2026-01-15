import sys
d = sys.stdin.read().split()
i = 0
t = int(d[i])
i += 1
o = []
for _ in range(t):
    w = int(d[i]); h = int(d[i+1]); n = int(d[i+2])
    i += 3
    c = 1
    while w % 2 == 0:
        w //= 2
        c *= 2
    while h % 2 == 0:
        h //= 2
        c *= 2
    if c >= n:
        o.append("YES")
    else:
        o.append("NO")
print("\n".join(o))
