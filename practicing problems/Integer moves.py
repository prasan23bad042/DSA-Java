import math

t = int(input())

for _ in range(t):
    x, y = map(int, input().split())

    if x == 0 and y == 0:
        print(0)

    elif math.isqrt(x * x + y * y) ** 2 == x * x + y * y:
        print(1)

    else:
        print(2)
