import sys
data = sys.stdin.read().strip().split()
t = int(data[0])
idx = 1
ans = []
for _ in range(t):
    n = int(data[idx])
    m = int(data[idx + 1])
    idx += 2
    ans.append(str((n * m + 1) // 2))
print("\n".join(ans))
