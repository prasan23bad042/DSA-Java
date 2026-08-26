import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, k = map(int, input().split())

    if k == 0:
        print(0)
        continue

    diagonals = list(range(1, n + 1)) + list(range(n - 1, 0, -1))

    diagonals.sort(reverse=True)

    total = 0
    answer = 0

    for size in diagonals:
        total += size
        answer += 1

        if total >= k:
            break

    print(answer)
