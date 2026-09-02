t = int(input())

for _ in range(t):
    n = int(input())
    g = list(map(int, input().split()))

    g.sort()

    ans = 0

    # Take largest, 3rd largest, 5th largest, ...
    for i in range(n - 1, -1, -2):
        ans += g[i]

    print(ans)
