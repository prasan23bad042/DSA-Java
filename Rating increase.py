t = int(input())

for _ in range(t):
    s = input().strip()
    n = len(s)
    found = False

    for i in range(1, n):
        a = s[:i]
        b = s[i:]

        if b[0] == '0':
            continue

        x = int(a)
        y = int(b)

        if y > x:
            print(x, y)
            found = True
            break

    if not found:
        print(-1)
