t = int(input())
for _ in range(t):
    s = input().strip()
    c = s[0]
    r = s[1]
    for i in range(1, 9):
        if str(i) != r:
            print(c + str(i))
    for i in range(ord('a'), ord('h') + 1):
        if chr(i) != c:
            print(chr(i) + r)
