import sys


def solve():
    input = sys.stdin.readline

    t = int(input())

    # Each tuple contains 3 different nearly-prime numbers.
    triples = [
        (6, 10, 14),
        (6, 10, 15),
        (6, 10, 21),
        (6, 14, 15),
        (6, 14, 21),
        (10, 14, 15),
        (10, 14, 21),
    ]

    for _ in range(t):
        n = int(input())

        found = False

        for a, b, c in triples:
            d = n - (a + b + c)

            # d must be positive and different from all three.
            if d > 0 and d != a and d != b and d != c:
                print("YES")
                print(a, b, c, d)
                found = True
                break

        if not found:
            print("NO")
solve()
