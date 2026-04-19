import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    e = 0
    o = 0
    for x in a:
        if x % 2 == 0:
            e += 1
        else:
            o += 1
    print(min(e,o))