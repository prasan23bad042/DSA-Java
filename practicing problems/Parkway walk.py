t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    a = map(int, input().split())

    total_distance = sum(a)

    print(max(0, total_distance - m))
