t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    first = a.index(1)
    last = max(i for i in range(n) if a[i] == 1)

    print(a[first:last + 1].count(0))
