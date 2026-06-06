import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    
    if not data:
        return
    
    t = int(data[0])
    results = []
    
    idx = 1
    for _ in range(t):
        row1 = data[idx]
        row2 = data[idx+1]
        idx += 2
        pixels = row1 + row2
        unique_colors = set(pixels)
        moves = len(unique_colors) - 1
        results.append(str(moves))
    print('\n'.join(results))
solve()
