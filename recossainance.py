n = int(input())
a = list(map(int,input().split()))
mn = 10**9
x = 0
y = 1
for i in range(n-1):
    d = abs(a[i] - a[i+1])
    if d < mn:
        mn = d
        x = i
        y = i + 1
d = abs(a[n-1] - a[0])
if d < mn:
    x = n - 1
    y = 0
print(x+1, y+1)