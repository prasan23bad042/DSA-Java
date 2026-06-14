t = int(input())

for _ in range(t):
    n, k = map(int, input().split())

    if n % 2 == 0:
        print((n + (k - 2)) // (k - 1))
    else:
        print(1 + (n - k + (k - 2)) // (k - 1))
