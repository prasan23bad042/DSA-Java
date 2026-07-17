import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    odd = []
    even = []

    for x in arr:
        if x % 2:
            odd.append(x)
        else:
            even.append(x)

    print(*(odd + even))
