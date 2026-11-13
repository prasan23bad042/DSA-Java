t = int(input())

for _ in range(t):
    n, l, r, k = map(int, input().split())
    a = list(map(int, input().split()))

    chocolates = []

    for price in a:
        if l <= price <= r:
            chocolates.append(price)

    chocolates.sort()

    count = 0

    for price in chocolates:
        if price <= k:
            k -= price
            count += 1
        else:
            break

    print(count)
  
