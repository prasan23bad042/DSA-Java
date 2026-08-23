t = int(input())

for _ in range(t):
    a, b, c = map(int, input().split())

    total = a + b + c

    if total % 3 == 0 and total // 3 >= b:
        print("YES")
    else:
        print("NO")
