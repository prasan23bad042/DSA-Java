t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    a.sort()

    ans = 2 * ((a[-1] + a[-2]) - (a[0] + a[1]))
    print(ans)
