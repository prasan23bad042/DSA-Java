t = int(input())

for _ in range(t):
    n = int(input())
    a = sorted(map(int, input().split()))

    b = []
    for i in range(n):
        b.append(a[i])
        b.append(a[i + n])

    print(*b)
