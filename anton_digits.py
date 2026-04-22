k2, k3, k5, k6 = map(int,input().split())
x = min(k2, k5, k6)
k2 -= x
y = min(k3, k2)
print(x * 256 + y * 32)