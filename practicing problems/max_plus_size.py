import sys

input = sys.stdin.readline

def mis_segment(arr, l, r, limit):
    if l > r:
        return 0

    dp2 = 0
    dp1 = 0

    for k in range(l, r + 1):
        if arr[k] <= limit:
            cur = max(dp1, dp2 + 1)
        else:
            cur = dp1
        dp2, dp1 = dp1, cur

    return dp1


t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    ans = 0

    for i in range(n):
        limit = a[i]

        left = mis_segment(a, 0, i - 2, limit)
        right = mis_segment(a, i + 2, n - 1, limit)

        ans = max(ans, limit + 1 + left + right)

    print(ans)
