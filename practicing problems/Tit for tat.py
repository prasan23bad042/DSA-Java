t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    for i in range(n - 1):
        x = min(a[i], k)

        a[i] -= x
        a[n - 1] += x
        k -= x

        if k == 0:
            break

    print(*a)
  
