t = int(input())

for _ in range(t):
    x, y, a, b = map(int, input().split())

    distance = y - x
    speed = a + b

    if distance % speed == 0:
        print(distance // speed)
    else:
        print(-1)
