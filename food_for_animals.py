t = int(input())
for _ in range(t):
    a, b, c, x, y = map(int,input().split())
    d = max(0, x - a)
    e = max(0, y - b)
    if d + e <= c:
        print("YES")
    else:
        print("NO")