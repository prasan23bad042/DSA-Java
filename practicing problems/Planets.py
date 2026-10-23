t = int(input())

for _ in range(t):
    n, c = map(int, input().split())
    a = list(map(int, input().split()))

    from collections import Counter
    freq = Counter(a)

    ans = 0
    for count in freq.values():
        ans += min(count, c)

    print(ans)
  
