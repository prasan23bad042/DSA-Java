t = int(input())

for _ in range(t):
    s = list(input())

    for i in range(len(s)):
        if i % 2 == 0:      # Alice's turn
            if s[i] == 'a':
                s[i] = 'b'
            else:
                s[i] = 'a'
        else:               # Bob's turn
            if s[i] == 'z':
                s[i] = 'y'
            else:
                s[i] = 'z'

    print("".join(s))
