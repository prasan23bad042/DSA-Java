from bisect import bisect_right

t = int(input())

for _ in range(t):
    k, q = map(int, input().split())
    a = list(map(int, input().split()))
    queries = list(map(int, input().split()))

    ans = []

    for n in queries:
        while n >= a[0]:
            removed = bisect_right(a, n)
            n -= removed

        ans.append(n)

    print(*ans)
  
