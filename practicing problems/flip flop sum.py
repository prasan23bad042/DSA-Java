t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    total = sum(a)

    if -1 not in a:
        # All elements are +1.
        # Any operation flips two +1s -> decreases by 4.
        print(total - 4)

    elif any(a[i] == -1 and a[i + 1] == -1 for i in range(n - 1)):
        # We can flip two -1s -> increase by 4.
        print(total + 4)

    else:
        # No adjacent -1s.
        # There must be a (+1, -1) or (-1, +1) pair.
        # Flipping it doesn't change the sum.
        print(total)
