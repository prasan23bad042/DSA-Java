t = int(input())

for _ in range(t):
    s = input().strip()
    n = len(s)

    l, r = 0, n - 1
    cur = ord('a') + n - 1

    ok = True

    while l <= r:
        ch = chr(cur)

        if s[l] == ch:
            l += 1
        elif s[r] == ch:
            r -= 1
        else:
            ok = False
            break

        cur -= 1

    print("YES" if ok else "NO")
