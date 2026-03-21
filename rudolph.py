import sys
i = sys.stdin.read().split()
p = 0
t = int(i[p]); p += 1
r = []
for _ in range(t):
    n = int(i[p]); p += 1
    m = {}
    for _ in range(n):
        a = int(i[p]); b = int(i[p+1])
        p += 2
        d = a - b
        if d <= 0:
            if d in m:
                m[d] += 1
            else:
                m[d] = 1
    mx = 0
    for k in m:
        if m[k] > mx:
            mx = m[k]
    r.append(str(n - mx))
print("\n".join(r))