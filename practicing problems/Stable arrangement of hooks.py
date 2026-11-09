t = int(input())

for _ in range(t):
    n, k = map(int, input().split())

    if k > (n + 1) // 2:
        print(-1)
    else:
        board = [['.' for _ in range(n)] for _ in range(n)]

        for i in range(k):
            board[2 * i][2 * i] = 'R'

        for row in board:
            print(''.join(row))
