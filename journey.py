for _ in range(int(input())):
    n, a, b, c = map(int,input().split())
    s = a + b + c
    k = n // s
    d = k * 3
    r = n % s
    if r == 0:
        print(d)
    else:
        if r <= a:
            print(d + 1)
        elif r <= a + b:
            print(d + 2)
        else:
            print(d + 3)