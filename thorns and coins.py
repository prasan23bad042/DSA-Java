import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip()
    dp = [-1] * n
    dp[0] = 0   
    for i in range(1, n):
        if s[i] == '*':
            continue
        a = -1
        b = -1
        if dp[i-1] != -1:
            a = dp[i-1]
        if i > 1 and dp[i-2] != -1:
            b = dp[i-2]
        best = max(a, b)
        if best != -1:
            dp[i] = best + (1 if s[i] == '@' else 0)
    print(max(dp))