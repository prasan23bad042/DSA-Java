t = int(input())

for _ in range(t):
    n, m, r, c = map(int, input().split())

    grid = [input().strip() for _ in range(n)]

    r -= 1
    c -= 1

    # Case 1: Target cell is already black
    if grid[r][c] == 'B':
        print(0)
        continue

    # Case 2: Check the target row
    if 'B' in grid[r]:
        print(1)
        continue

    # Case 3: Check the target column
    if any(grid[i][c] == 'B' for i in range(n)):
        print(1)
        continue

    # Case 4: Check whether any black cell exists
    if any('B' in row for row in grid):
        print(2)
    else:
        print(-1)
      
