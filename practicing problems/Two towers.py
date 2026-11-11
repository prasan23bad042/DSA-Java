t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    s = input().strip()
    r = input().strip()

    count = 0

    for i in range(1, n):
        if s[i] == s[i - 1]:
            count += 1

    for i in range(1, m):
        if r[i] == r[i - 1]:
            count += 1

    if count == 0:
        print("YES")
    elif count == 1 and s[0] != r[0]:
        print("YES")
    else:
        print("NO")
  
