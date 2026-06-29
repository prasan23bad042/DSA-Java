t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    mn = min(arr)
    cnt = arr.count(mn)

    if cnt == n:
        print(0)
    else:
        print(n - cnt)
