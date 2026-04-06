t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    
    ans = []
    
    for i in range(n, k+1, -1):
        ans.append(i)
    
    for i in range(1, k+1):
        ans.append(i)
    
    print(*ans)