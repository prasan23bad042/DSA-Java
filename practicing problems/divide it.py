
q = int(input())

for _ in range(q):
    n = int(input())
    count = 0

    for p in (2, 3, 5):
        while n % p == 0:
            n //= p
            count += 1

    print(count if n == 1 else -1)
