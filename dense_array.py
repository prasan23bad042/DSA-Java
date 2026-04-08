t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    
    c = 0
    
    for i in range(n - 1):
        x = a[i]
        y = a[i + 1]
        
        mn = min(x, y)
        mx = max(x, y)
        
        while mx > 2 * mn:
            mn *= 2
            c += 1
    
    print(c)