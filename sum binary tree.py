import sys
input = sys.stdin.readline
t = int(input())
while t > 0:
    n = int(input())
    s = 0
    while n > 0:
        s += n
        n //= 2
    print(s)
    t -= 1