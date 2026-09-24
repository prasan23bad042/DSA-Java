t = int(input())

for _ in range(t):
    px, py = map(int, input().split())
    s = input().strip()

    r = s.count('R')
    l = s.count('L')
    u = s.count('U')
    d = s.count('D')

    possible = True

    if px > 0 and r < px:
        possible = False
    elif px < 0 and l < abs(px):
        possible = False

    if py > 0 and u < py:
        possible = False
    elif py < 0 and d < abs(py):
        possible = False

    print("YES" if possible else "NO")
