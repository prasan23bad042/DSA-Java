import sys
input = sys.stdin.read
data = input().split()
t = int(data[0])
idx = 1
results = []
for _ in range(t):
    n = int(data[idx])
    idx += 1
    arr = list(map(int, data[idx:idx+n]))
    idx += n
    neg = arr.count(-1)
    zero = arr.count(0)
    ops = 0
    ops += zero
    if neg % 2 == 1:
        ops += 2
    results.append(str(ops))
print("\n".join(results))
