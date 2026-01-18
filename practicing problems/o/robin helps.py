for _ in range(int(input())):
    n, k = map(int,input().split())
    a = list(map(int,input().split()))
    g = 0
    cnt = 0
    for x in a:
        if x >= k:
            g += x
        elif x == 0 and g > 0:
            g -= 1
            cnt += 1
    print(cnt)
