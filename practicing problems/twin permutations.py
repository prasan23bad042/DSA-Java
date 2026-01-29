import sys
input = sys.stdin.read
data = input().split()
t = int(data[0])
idx = 1
out = []
for _ in range(t):
    n = int(data[idx])
    idx += 1
    a = list(map(int,data[idx:idx+n]))
    idx += n
    b = [n + 1 - x for x in a]
    out.append(" ".join(map(str,b)))
print("\n".join(out))

