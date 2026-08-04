import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())

    x = y = 0
    rects = []
    xs = []
    ys = []

    for _ in range(n):
        dx, dy = map(int, input().split())
        x += dx
        y += dy
        rects.append((x, y, x + m, y + m))
        xs.extend([x, x + m])
        ys.extend([y, y + m])

    xs = sorted(set(xs))
    ys = sorted(set(ys))

    x_id = {v: i for i, v in enumerate(xs)}
    y_id = {v: i for i, v in enumerate(ys)}

    W = len(xs) - 1
    H = len(ys) - 1

    covered = [[False] * H for _ in range(W)]

    for x1, y1, x2, y2 in rects:
        for i in range(x_id[x1], x_id[x2]):
            for j in range(y_id[y1], y_id[y2]):
                covered[i][j] = True

    perimeter = 0

    for i in range(W):
        cell_width = xs[i + 1] - xs[i]
        for j in range(H):
            if not covered[i][j]:
                continue

            cell_height = ys[j + 1] - ys[j]

            # Left edge
            if i == 0 or not covered[i - 1][j]:
                perimeter += cell_height

            # Right edge
            if i == W - 1 or not covered[i + 1][j]:
                perimeter += cell_height

            # Bottom edge
            if j == 0 or not covered[i][j - 1]:
                perimeter += cell_width

            # Top edge
            if j == H - 1 or not covered[i][j + 1]:
                perimeter += cell_width

    print(perimeter)
