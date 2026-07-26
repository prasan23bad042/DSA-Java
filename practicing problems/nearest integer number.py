a = int(input())

while True:
    digit_sum = 0
    temp = a

    while temp > 0:
        digit_sum += temp % 10
        temp //= 10

    if digit_sum % 4 == 0:
        print(a)
        break

    a += 1
