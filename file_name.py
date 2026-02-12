n = int(input())
s = input().strip()
cnt = 0
cur = 0
for ch in s:
    if ch == 'x':
        cur += 1
        if cur >= 3:
            cnt += 1
    else:
        cur = 0
print(cnt)
