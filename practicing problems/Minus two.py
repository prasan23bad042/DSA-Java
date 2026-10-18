t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    odd = sum(x % 2 == 1 for x in a)
    even = n - odd

    print(max(odd, even))
