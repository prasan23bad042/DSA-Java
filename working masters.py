for _ in range(int(input())):
    a, b, c, d = map(int,input().split())
    if d < b:
        print(-1)
        continue
    diag = d - b
    x_after = a + diag
    if x_after < c:
        print(-1)
    else:
        print(diag + (x_after - c))
