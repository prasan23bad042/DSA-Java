t = int(input())

for _ in range(t):
    n, m = map(int, input().split())

    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    s = set(a)
    found = False

    for x in b:
        if x in s:
            print("YES")
            print(1, x)
            found = True
            break

    if not found:
        print("NO")
