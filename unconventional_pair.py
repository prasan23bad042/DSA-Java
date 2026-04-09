import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    a.sort()
    m = 0
    for i in range(0, n, 2):
        d = abs(a[i] - a[i+1])
        if d > m:
            m = d
    print(m)