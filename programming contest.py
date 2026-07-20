t = int(input())

for _ in range(t):
    n = int(input())
    s = input().strip()

    ans = 1 if s[0] == '1' else 0

    for i in range(1, n):
        if s[i] != s[i - 1]:
            ans += 1

    print(ans)
