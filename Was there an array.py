t = int(input())

for _ in range(t):
    n = int(input())
    b = list(map(int, input().split()))

    possible = True

    for i in range(len(b) - 2):
        if b[i] == 1 and b[i + 1] == 0 and b[i + 2] == 1:
            possible = False
            break

    print("YES" if possible else "NO")
