t = int(input())

for _ in range(t):
    n, a, b = map(int, input().split())

    if a <= b:
        print("YES" if n % 2 == b % 2 else "NO")
    else:
        print("YES" if (n % 2 == a % 2 == b % 2) else "NO")
