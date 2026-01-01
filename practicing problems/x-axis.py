for _ in range(int(input())):
    a = list(map(int,input().split()))
    a.sort()
    m=a[1]
    print(abs(a[0]-m)+abs(a[1]-m)+abs(a[2]-m))
