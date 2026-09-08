a1, a2, a3 = map(int, input().split())
b1, b2, b3 = map(int, input().split())
n = int(input())

cups = a1 + a2 + a3
medals = b1 + b2 + b3

cup_shelves = (cups + 4) // 5
medal_shelves = (medals + 9) // 10

if cup_shelves + medal_shelves <= n:
    print("YES")
else:
    print("NO")
