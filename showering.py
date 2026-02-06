import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n, s, m = map(int,input().split())
    intervals = []
    for _ in range(n):
        l, r = map(int, input().split())
        intervals.append((l,r))
    can_shower = False
    if intervals[0][0] >= s:
        can_shower = True
    for i in range(1, n):
        if intervals[i][0] - intervals[i-1][1] >= s:
            can_shower = True
            break
    if m - intervals[-1][1] >= s:
        can_shower = True
    print("YES" if can_shower else "NO")
