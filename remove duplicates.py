def solve():
    try:
        line1 = input().split()
        if not line1:
            return
        n = int(line1[0])
        a = list(map(int, input().split()))
    except EOFError:
        return

    seen = set()
    result = []
    for i in range(n - 1, -1, -1):
        if a[i] not in seen:
            result.append(a[i])
            seen.add(a[i])
    result.reverse()
    print(len(result))
    print(*(result))
solve()