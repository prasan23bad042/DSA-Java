t = int(input())
for _ in range(t):
    n, a, b = map(int,input().split())
    if abs(a - b) % 2 == 1:
        print("YES")
    else:
        print("NO")