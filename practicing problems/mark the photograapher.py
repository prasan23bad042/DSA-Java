import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, x = map(int, input().split())
    h = list(map(int, input().split()))

    h.sort()

    for i in range(n):
        if h[i + n] - h[i] < x:
            print("NO")
            break
    else:
        print("YES")
