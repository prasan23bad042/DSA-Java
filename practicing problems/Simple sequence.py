t = int(input())

for _ in range(t):
    n = int(input())
    print(n, *range(n - 1, 0, -1))
