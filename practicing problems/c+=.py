import sys
d = sys.stdin.read().split()
i = 0
t = int(d[i])
i += 1
o = []
for _ in range(t):
    a = int(d[i]); b = int(d[i+1]); n = int(d[i+2])
    i += 3
    c = 0
    if a > b:
        a, b = b, a
    while b <= n:
        a, b = b, a + b
        c += 1
    o.append(str(c))
print("\n".join(o))
