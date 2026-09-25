a, b, c = map(int, input().split())

a, b, c = sorted([a, b, c])

print(max(0, c - a - b + 1))
