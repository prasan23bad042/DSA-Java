t = int(input())

for _ in range(t):
    n, q = map(int, input().split())
    a = list(map(int, input().split()))

    even_sum = 0
    odd_sum = 0
    even_count = 0
    odd_count = 0

    for num in a:
        if num % 2 == 0:
            even_sum += num
            even_count += 1
        else:
            odd_sum += num
            odd_count += 1

    total = even_sum + odd_sum

    for _ in range(q):
        typ, x = map(int, input().split())

        if typ == 0:
            # Add x to all even elements
            total += even_count * x

            if x % 2 == 1:
                # Even elements become odd
                odd_sum += even_count * x
                odd_count += even_count

                even_sum = 0
                even_count = 0

        else:
            # Add x to all odd elements
            total += odd_count * x

            if x % 2 == 1:
                # Odd elements become even
                even_sum += odd_count * x
                even_count += odd_count

                odd_sum = 0
                odd_count = 0

        print(total)
      
