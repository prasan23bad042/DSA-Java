import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    N = 1 << n

    # good[mask] = remaining array is non-decreasing
    good = [False] * N

    for mask in range(N):
        prev = -1
        ok = True
        for i in range(n):
            if mask & (1 << i):
                if a[i] < prev:
                    ok = False
                    break
                prev = a[i]
        good[mask] = ok

    reach = [False] * N
    full = N - 1
    reach[full] = True

    # Process masks from larger to smaller
    for mask in range(full, -1, -1):
        if not reach[mask]:
            continue
        if good[mask]:
            continue      # game stops here

        m = mask
        while m:
            bit = m & -m
            reach[mask ^ bit] = True
            m ^= bit

    ans = n
    for mask in range(N):
        if reach[mask] and good[mask]:
            ans = min(ans, mask.bit_count())

    print(ans)
