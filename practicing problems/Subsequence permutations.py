t = int(input())

for _ in range(t):
    n = int(input())
    s = input()

    x = sorted(s)

    ans = 0

    for i in range(n):
        if s[i] != x[i]:
            ans += 1

    print(ans)
