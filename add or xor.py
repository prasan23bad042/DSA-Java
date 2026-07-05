import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    a, b, x, y = map(int, input().split())

    if a == b:
        print(0)
        continue

    if b < a:
        if a % 2 == 1 and b == a - 1:
            print(y)
        else:
            print(-1)
        continue

    ans = 0
    inc_even = min(x, y)

    for cur in range(a, b):
        if cur % 2 == 0:
            ans += inc_even
        else:
            ans += x

    print(ans)
