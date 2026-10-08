t = int(input())

for _ in range(t):
    l, r = map(int, input().split())
    print(((r + 1) // 2 - l // 2) // 2)
