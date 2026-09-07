q = int(input())

for _ in range(q):
    n, t = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    best_value = -1
    answer = -1

    for i in range(n):
        # i is 0-based, so skipping time = i
        time_needed = i + a[i]

        if time_needed <= t:
            if b[i] > best_value:
                best_value = b[i]
                answer = i + 1   # convert to 1-based index

    print(answer)
