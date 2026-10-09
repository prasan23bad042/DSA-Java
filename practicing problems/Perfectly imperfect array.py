from math import isqrt

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    ans = "NO"

    for x in a:
        r = isqrt(x)
        if r * r != x:
            ans = "YES"
            break

    print(ans)
  
