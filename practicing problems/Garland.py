t = int(input())

for _ in range(t):
    s = input().strip()

    if len(set(s)) == 1:
        print(-1)
    else:
        print(4 + 2 * (max(s.count(c) for c in set(s)) - 1))
