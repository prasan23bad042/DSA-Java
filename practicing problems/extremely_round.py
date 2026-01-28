import sys
a = sys.stdin.read().split()
if not a:
    sys.exit()
t = int(a[0])
res = []
for i in range(1, t + 1):
    s = a[i]
    d = len(s)
    f = int(s[0])
    ans = (d - 1) * 9 + f
    res.append(str(ans))
sys.stdout.write("\n".join(res) + "\n")
