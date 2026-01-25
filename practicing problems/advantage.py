from sys import stdin
t = int(stdin.readline())
for _ in range(t):
    n = int(stdin.readline())
    a = list(map(int,stdin.readline().split()))
    mx = max(a)
    cnt = a.count(mx)
    smx = -1
    for x in a:
        if x != mx:
            smx = max(smx, x)
    res = []
    for x in a:
        if x == mx:
            if cnt > 1:
                res.append(0)
            else:
                res.append(x - smx)
        else:
            res.append(x - mx)
    print(*res)
