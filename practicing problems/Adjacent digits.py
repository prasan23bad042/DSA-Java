t = int(input())

for _ in range(t):
    x, y = map(int, input().split())

    diff = x + 1 - y

    if diff >= 0 and diff % 9 == 0:
        print("YES")
    else:
        print("NO")
