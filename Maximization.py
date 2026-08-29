t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    # Count occurrences
    freq = [0] * 101

    for x in a:
        freq[x] += 1

    ans = []

    # Put 0, 1, 2, ... as early as possible
    mex = 0

    while mex <= 100 and freq[mex] > 0:
        ans.append(mex)
        freq[mex] -= 1
        mex += 1

    # Put all remaining elements
    for x in range(101):
        while freq[x] > 0:
            ans.append(x)
            freq[x] -= 1

    print(*ans)
