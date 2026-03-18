t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    cnt = {}
    for ch in s:
        if ch in cnt:
            cnt[ch] += 1
        else:
            cnt[ch] = 1
    ans = 0
    for ch in cnt:
        need = ord(ch) - ord('A') + 1
        if cnt[ch] >= need:
            ans += 1
    print(ans)