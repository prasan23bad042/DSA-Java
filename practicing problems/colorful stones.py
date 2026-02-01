s = input().strip()
t = input().strip()
i = 0
for c in t:
    if s[i] == c:
        i += 1
print(i + 1)
