import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    need = {0:3, 1:1, 2:2, 3:1, 5:1}
    cnt = {0:0, 1:0, 2:0, 3:0, 5:0}
    ans = 0
    for i in range(n):
        d = a[i]
        if d in cnt:
            cnt[d] += 1
        ok = True
        for k in need:
            if cnt[k] < need[k]:
                ok = False
                break
        if ok:
            ans = i + 1
            break
    print(ans)