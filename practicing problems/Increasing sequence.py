t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    prev = 0

    for x in a:
        cur = prev + 1
        if cur == x:
            cur += 1
        prev = cur

    print(prev)
