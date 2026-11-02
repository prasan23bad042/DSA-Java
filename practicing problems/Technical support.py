t = int(input())

for _ in range(t):
    n = int(input())
    s = input().strip()

    unanswered = 0
    valid = True

    for ch in s:
        if ch == 'Q':
            unanswered += 1
        else:
            unanswered -= 1

        if unanswered < 0:
            valid = False
            break

    if valid and unanswered == 0:
        print("Yes")
    else:
        print("No")
      
