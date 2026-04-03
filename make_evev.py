t = int(input())
for _ in range(t):
    n = input().strip()
    # Case 1: already even
    if int(n[-1]) % 2 == 0:
        print(0)
    # Case 2: first digit even
    elif int(n[0]) % 2 == 0:
        print(1)
    # Case 3: any even digit exists
    else:
        f = 0
        for c in n:
            if int(c) % 2 == 0:
                f = 1
                break
        if f == 1:
            print(2)
        else:
            print(-1)