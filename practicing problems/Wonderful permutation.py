t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    p = list(map(int, input().split()))

    ans = sum(1 for x in p[:k] if x > k)
    print(ans)
  
