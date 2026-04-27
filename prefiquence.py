import sys
input = sys.stdin.readline

t = int(input())
while t:
    n, m = map(int,input().split())
    a = input().strip()
    b = input().strip()
    
    i = 0
    j = 0
    
    while i < n and j < m:
        if a[i] == b[j]:
            i += 1
        j += 1
    
    print(i)
    t -= 1