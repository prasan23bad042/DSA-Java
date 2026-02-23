import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    s = input().strip()
    pos = {}
    ok = True
    for i in range(n):
        ch = s[i]
        if ch not in pos:
            pos[ch] = i % 2
        else:
            if pos[ch] != i % 2:
                ok = False
                break
    if ok:
        print("YES")
    else:
        print("NO")