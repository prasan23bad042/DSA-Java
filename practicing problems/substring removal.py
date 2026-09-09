T = int(input())

for _ in range(T):
    s = input().strip()

    groups = []
    count = 0

    for ch in s:
        if ch == '1':
            count += 1
        else:
            if count > 0:
                groups.append(count)
                count = 0

    # Add the last group if it ends with 1
    if count > 0:
        groups.append(count)

    # Largest 1-groups are taken first
    groups.sort(reverse=True)

    # Alice gets 1st, 3rd, 5th, ...
    answer = sum(groups[::2])

    print(answer)
