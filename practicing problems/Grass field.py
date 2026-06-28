t = int(input())

for _ in range(t):
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    cnt = sum(a) + sum(b)

    if cnt == 0:
        print(0)
    elif cnt == 4:
        print(2)
    else:
        print(1)
