t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    ones = a.count(1)
    zeros = 2 * n - ones

    mn = ones % 2
    mx = min(ones, zeros)

    print(mn, mx)
