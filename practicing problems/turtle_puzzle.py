def solve():
    import sys
    input = sys.stdin.readline
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int,input().split()))
        ans = 0
        for x in arr:
            ans += abs(x)
        print(ans)
solve()