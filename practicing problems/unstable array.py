for _ in range(int(input())):
    n, m = map(int,input().split())
    if n == 1:
        print(0)
    else:
        print(min(2 * m, m * (n - 1)))
