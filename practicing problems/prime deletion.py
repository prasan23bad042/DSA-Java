import sys
import math


def is_prime(n):
    if n < 2:
        return False

    if n == 2:
        return True

    if n % 2 == 0:
        return False

    for i in range(3, math.isqrt(n) + 1, 2):
        if n % i == 0:
            return False

    return True


def solve():
    input = sys.stdin.readline

    t = int(input())

    for _ in range(t):
        s = input().strip()
        n = len(s)

        answer = "-1"

        # Try every subsequence
        for mask in range(1 << n):

            # Final sequence must contain at least 3 digits
            if mask.bit_count() < 3:
                continue

            subsequence = []

            for i in range(n):
                if mask & (1 << i):
                    subsequence.append(s[i])

            num = int(''.join(subsequence))

            if is_prime(num):
                answer = ''.join(subsequence)
                break

        print(answer)


if __name__ == "__main__":
    solve()
