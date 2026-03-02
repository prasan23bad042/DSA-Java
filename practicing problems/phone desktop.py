import sys
input = sys.stdin.readline
for _ in range(int(input())):
    x, y = map(int,input().split())
    screens = (y + 1) // 2   
    if y % 2 == 0:
        free_cells = screens * 15 - y * 4
    else:
        free_cells = screens * 15 - y * 4
    remaining_ones = max(0, x - free_cells)
    screens += (remaining_ones + 14) // 15
    print(screens)
