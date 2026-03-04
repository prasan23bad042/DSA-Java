import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n, k = map(int,input().split())
    a = list(map(int,input().split()))
    i = 0
    ans = 0
    while i <= n - k:
        ok = 1
        for j in range(i, i + k):
            if a[j] == 1:
                ok = 0
                break
        if ok == 1:
            ans += 1
            i += k + 1
        else:
            i += 1
    print(ans)