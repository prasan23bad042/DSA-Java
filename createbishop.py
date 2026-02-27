import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    input()
    g = []
    for _ in range(8):
        g.append(input().strip())
    for i in range(1, 7):
        for j in range(1, 7):
            if (
                g[i][j] == '#'
                and g[i-1][j-1] == '#'
                and g[i-1][j+1] == '#'
                and g[i+1][j-1] == '#'
                and g[i+1][j+1] == '#'
            ):
                print(i + 1, j + 1)