import sys
d = sys.stdin.read().split()
i = 0
t = int(d[i])
i += 1
o = []
for _ in range(t):
    a = int(d[i])
    b = int(d[i+1])
    i += 2
    if a == b:
        o.append("0")
    elif b > a:
        x = b - a
        if x & 1:
            o.append("1")
        else:
            o.append("2")
    else:
        x = a - b
        if x % 2 == 0:
            o.append("1")
        else:
            o.append("2")
print("\n".join(o))
