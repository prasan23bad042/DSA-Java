t = int(input())
for _ in range(t):
    x,y = list(map(int,input().split()))
    a = x // (y+1)
    if x%(y+1):
        a += 1
    print(max(a,(-2)*y+x))