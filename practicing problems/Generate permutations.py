import sys

def solve():
    input = sys.stdin.readline

    t = int(input())

    for _ in range(t):
        n = int(input())

        if n % 2 == 0:
            print(-1)
            continue

        ans = []

        # Even numbers
        for i in range(2, n, 2):
            ans.append(i)

        # Middle element
        ans.append(n)

        # Remaining odd numbers in decreasing order
        for i in range(n - 2, 0, -2):
            ans.append(i)

        print(*ans)


solve()
