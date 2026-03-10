import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    a = []
    for _ in range(n):
        a.append(input().strip())
    c = []
    for i in range(n):
        x = a[i].count('1')
        if x > 0:
            c.append(x)
    if len(set(c)) == 1:
        print("SQUARE")
    else:
        print("TRIANGLE")