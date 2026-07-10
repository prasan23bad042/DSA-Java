t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    zero = False
    neg = 0

    for x in a:
        if x == 0:
            zero = True
        elif x < 0:
            neg += 1

    if zero or neg % 2 == 1:
        print(0)
    else:
        print(1)
        print(1, 0)
