t = int(input())

for _ in range(t):
    n = int(input())

    if n % 2050 != 0:
        print(-1)
    else:
        x = n // 2050
        ans = 0

        while x:
            ans += x % 10
            x //= 10

        print(ans)
