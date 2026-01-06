t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    ma = min(a)
    mb = min(b)
    ans = 0
    for i in range(n):
        x = a[i] - ma
        y = b[i] - mb
        if x > y:
            ans += x
        else:
            ans += y
    print(ans)
