t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    d = {}
    for i in a:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    mx = 0
    for i in d:
        if d[i] > mx:
            mx = d[i]
    print(n - mx)