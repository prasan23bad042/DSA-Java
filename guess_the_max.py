import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    
    m = 10**18
    
    for i in range(n-1):
        x = max(a[i], a[i+1])
        if x < m:
            m = x
    
    print(m - 1)