for _ in range(int(input())):
    x=input().strip()
    mn=9
    for c in x:
        if int(c)<mn:
            mn=int(c)
    print(mn)
