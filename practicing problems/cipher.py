import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip()
    i = 0
    ans = []
    while i < n:
        ch = s[i]
        ans.append(ch)
        i += 1
        while i < n and s[i] != ch:
            i += 1
        i += 1 
    print("".join(ans))
