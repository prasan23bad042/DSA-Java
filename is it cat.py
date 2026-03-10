import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip().lower()   
    i = 0
    ok = True
    if i < n and s[i] == 'm':
        while i < n and s[i] == 'm':
            i += 1
    else:
        ok = False
    if ok and i < n and s[i] == 'e':
        while i < n and s[i] == 'e':
            i += 1
    else:
        ok = False
    if ok and i < n and s[i] == 'o':
        while i < n and s[i] == 'o':
            i += 1
    else:
        ok = False
    if ok and i < n and s[i] == 'w':
        while i < n and s[i] == 'w':
            i += 1
    else:
        ok = False
    if i != n:
        ok = False
    print("YES" if ok else "NO")