for _ in range(int(input())):
    n, m = map(int, input().split())
    s = input().strip()
    cnt = [0] * 7
    for x in s:
        cnt[ord(x) - ord('A')] += 1
    ans = 0
    for i in range(7):
        if cnt[i] < m:
            ans += m - cnt[i]
    print(ans)
