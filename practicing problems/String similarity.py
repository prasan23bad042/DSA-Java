t = int(input())

for _ in range(t):
    n = int(input())
    s = input().strip()

    z = "0" * n

    found = False
    for i in range(n):
        if s[i:i+n] == z:
            found = True
            break

    if found:
        print("0" * n)
    else:
        print("1" * n)
