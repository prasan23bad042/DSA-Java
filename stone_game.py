import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    i = a.index(min(a))
    j = a.index(max(a))
    left = max(i, j) + 1
    right = n - min(i, j)
    both = min(i, j) + 1 + n - max(i, j)
    print(min(left, right, both))
