t = int(input())

for _ in range(t):
    n, a, b = map(int, input().split())

    if b < 3 * a:
        ans = (n // 3) * b + (n % 3) * a
    else:
        ans = n * a

    print(ans)
  
