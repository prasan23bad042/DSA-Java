import math

t = int(input())

for _ in range(t):
    n = int(input())
    x, y = map(int,input().split())
    
    m = min(x, y)
    
    if n == 0:
        print(0)
    else:
        print((n + m - 1) // m)