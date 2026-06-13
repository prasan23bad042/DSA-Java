t = int(input())

for _ in range(t):
    x, y = map(int, input().split())

    if y % x != 0:
        print(0, 0)
    else:
        print(1, y // x)
