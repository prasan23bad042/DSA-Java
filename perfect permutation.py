import sys

input = sys.stdin.readline

t = int(input())
ans = []

for _ in range(t):
    n = int(input())

    if n == 1:
        ans.append("1")
        continue

    p = []

    if n % 2 == 0:
        # Swap adjacent pairs
        for i in range(1, n + 1, 2):
            p.append(i + 1)
            p.append(i)

    else:
        # Swap pairs until the last 3 elements
        for i in range(1, n - 2, 2):
            p.append(i + 1)
            p.append(i)

        # Rotate the last 3 elements
        p.append(n - 1)
        p.append(n)
        p.append(n - 2)

    ans.append(" ".join(map(str, p)))

print("\n".join(ans))
