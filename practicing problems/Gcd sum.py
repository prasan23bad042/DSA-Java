import math

def digit_sum(x):
    s = 0
    while x > 0:
        s += x % 10
        x //= 10
    return s

t = int(input())

for _ in range(t):
    n = int(input())

    while True:
        if math.gcd(n, digit_sum(n)) > 1:
            print(n)
            break
        n += 1
      
