t = int(input())
for _ in range(t):
    s = input().strip()
    
    def f(x):
        time = 2
        for i in range(1, len(x)):
            if x[i] == x[i-1]:
                time += 1
            else:
                time += 2
        return time
    
    ans = ""
    best = -1
    
    for i in range(len(s) + 1):
        for c in "abcdefghijklmnopqrstuvwxyz":
            x = s[:i] + c + s[i:]
            val = f(x)
            
            if val > best:
                best = val
                ans = x
    
    print(ans)
