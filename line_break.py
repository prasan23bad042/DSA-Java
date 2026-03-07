import sys
input = sys.stdin.read
data = input().split()
t = int(data[0])
idx = 1
output = []
for _ in range(t):
    n = int(data[idx])
    m = int(data[idx + 1])
    idx += 2
    total = 0
    count = 0
    for i in range(n):
        word = data[idx]
        idx += 1
        if total + len(word) <= m:
            total += len(word)
            count += 1
        else:
            idx += (n - i - 1)
            break
    output.append(str(count))
print("\n".join(output))