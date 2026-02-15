import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    occ = set()
    ok = True
    for i in range(n):
        x = a[i]
        if i == 0:
            occ.add(x)
            continue
        if (x-1 not in occ) and (x+1 not in occ):
            ok = False
            break
        occ.add(x)
    print("YES" if ok else "NO")
