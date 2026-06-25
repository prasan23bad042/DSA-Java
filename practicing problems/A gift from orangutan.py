t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    ans = (max(a) - min(a)) * (n - 1)
    print(ans)
