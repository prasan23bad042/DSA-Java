import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    total = sum(map(int, input().split()))
    print(abs(total))
