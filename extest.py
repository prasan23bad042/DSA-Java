import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    a, b, k = map(int, input().split())
    
    x = k // 2
    
    if k % 2 == 0:
        print(x * (a - b))
    else:
        print(x * (a - b) + a)
