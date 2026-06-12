import math

t = int(input())

for _ in range(t):
    k = int(input())

    n = math.isqrt(k)
    if n * n < k:
        n += 1

    mx = n * n
    mid = mx - n + 1

    if k >= mid:
        r = n
        c = mx - k + 1
    else:
        r = k - (n - 1) * (n - 1)
        c = n

    print(r, c)
