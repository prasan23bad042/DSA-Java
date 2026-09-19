t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    s = input().strip()

    ans = 0

    for i in range(0, n, k):
        farm = s[i:i + k]

        if '0' not in farm:
            ans += 1

    print(ans)
