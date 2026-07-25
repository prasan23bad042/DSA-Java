import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())

    ans = 1
    while n > 3:
        ans *= 2
        n //= 4

    print(ans)
