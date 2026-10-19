t = int(input())

for _ in range(t):
    n, m = map(int, input().split())

    a = set(map(int, input().split()))
    b = set(map(int, input().split()))

    print(len(a & b))
