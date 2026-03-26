import sys
i = sys.stdin.read().split()
t = int(i[0])
p = 1
res = []
for _ in range(t):
    n = int(i[p])
    p += 1
    a = []
    x = 1
    for j in range(n):
        a.append(str(x))
        x += 2
    res.append(" ".join(a))
sys.stdout.write("\n".join(res))