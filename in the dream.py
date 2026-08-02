import sys

input = sys.stdin.readline

def possible(x, y):
    return max(x, y) <= 2 * (min(x, y) + 1)

t = int(input())

for _ in range(t):
    a, b, c, d = map(int, input().split())

    if possible(a, b) and possible(c - a, d - b):
        print("YES")
    else:
        print("NO")
