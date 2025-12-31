t=int(input())
for _ in range(t):
    x=input().strip()
    mn=9
    for c in x:
        if int(c)<mn:
            mn=int(c)
    print(mn)s
