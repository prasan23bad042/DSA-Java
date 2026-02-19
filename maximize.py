import sys
input = sys.stdin.readline
for _ in range(int(input())):
    x = int(input())
    d = x
    for i in range(2,int(x**0.5) + 1):
        if x % i == 0:
            d = i
            break
    if d == x:
        print(x - 1)
    else:
        print(x - d)
