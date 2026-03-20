import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    ans = 0
    for i in range(n):
        if i == n - 1:
            if a[i] > 0:
                ans += a[i]
        else:
            g = a[i] - b[i + 1]
            if g > 0:
                ans += g
    print(ans)