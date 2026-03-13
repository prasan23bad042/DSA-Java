def solve():
    t = int(input())
    for _ in range(t):
        n, v = map(int, input().split())
        max_cost = (n * (n - 1)) // 2
        if v >= n:
            min_cost = n - 1
        else:
            min_cost = (v - 1) + ((n - v) * (n - v + 1)) // 2
        print(max_cost, min_cost)

solve()