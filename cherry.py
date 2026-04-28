import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    
    a.sort()
    
    ans = 0
    
    for i in range(n - 1):
        p = a[i] * a[i + 1]
        if p > ans:
            ans = p
    
    print(ans)