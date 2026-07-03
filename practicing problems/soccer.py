import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())

    d1 = x1 - y1
    d2 = x2 - y2

    if (d1 > 0 and d2 > 0) or (d1 < 0 and d2 < 0):
        print("YES")
    else:
        print("NO")
