t = int(input())

for _ in range(t):
    n = int(input())

    s1, e1 = map(int, input().split())

    max_strength = 0

    for _ in range(n - 1):
        s, e = map(int, input().split())

        if e >= e1:
            max_strength = max(max_strength, s)

    w = max_strength + 1

    if w <= s1:
        print(w)
    else:
        print(-1)
      
