import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    s = input().strip()

    if n % 2 == 0 and s.count('(') == n // 2:
        print("YES")
    else:
        print("NO")
