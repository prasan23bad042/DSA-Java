import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    a = [0]*n
    x = 1
    for i in range(1, n, 2):
        a[i] = x
        x += 1
    for i in range(0, n, 2):
        a[i] = x
        x += 1
    print(*a)