t = int(input())

for _ in range(t):
    n = int(input())

    total = n + 1

    full_blocks = total // 15
    remaining = total % 15

    answer = full_blocks * 3 + min(remaining, 3)

    print(answer)
