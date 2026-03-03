import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    a.sort()
    i = 0
    j = n - 1
    ans = 0
    while i < j:
        ans += a[j] - a[i]
        i += 1
        j -= 1
    print(ans)