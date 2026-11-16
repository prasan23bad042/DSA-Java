t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    ans = max(a[::2])

    print(ans)
