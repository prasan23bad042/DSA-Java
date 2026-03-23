import sys
input=sys.stdin.readline
t=int(input())
for _ in range(t):
    n,d=input().split()
    d=int(d)
    s=input().strip()
    f=0
    r=""
    for c in s:
        if not f and int(c)<d:
            r+=str(d)
            f=1
        r+=c
    if not f:
        r+=str(d)
    print(r)