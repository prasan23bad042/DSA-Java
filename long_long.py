import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    total = 0
    for x in a:
        total += abs(x)
    ops = 0
    i = 0
    while i < n:
        if a[i] < 0:
            ops += 1
            while i < n and a[i] <= 0:
                i += 1
        else:
            i += 1
    print(total, ops)