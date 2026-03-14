import sys
input=sys.stdin.readline
t=int(input())
for _ in range(t):
    n=int(input())
    x=n//3
    if n%3==0:
        h2=x
        h1=x+1
        h3=x-1
    elif n%3==1:
        h2=x
        h1=x+2
        h3=x-1
    else:
        h2=x+1
        h1=x+2
        h3=x-1
    print(h2,h1,h3)