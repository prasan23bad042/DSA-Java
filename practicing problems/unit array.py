def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        neg = arr.count(-1)
        pos = n - neg
        ops = 0
        while pos - neg < 0:
            neg -= 1
            pos += 1
            ops += 1
        if neg % 2 == 1:
            ops += 1
        print(ops)
solve()