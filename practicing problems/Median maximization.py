t = int(input())

for _ in range(t):
    n, s = map(int, input().split())

    k = n // 2 + 1

    print(s // k)
