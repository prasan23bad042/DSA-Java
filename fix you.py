import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    t = int(input_data[0])
    idx = 1
    results = []
    
    for _ in range(t):
        n = int(input_data[idx])
        m = int(input_data[idx + 1])
        idx += 2
        
        grid = []
        for _ in range(n):
            grid.append(input_data[idx])
            idx += 1
            
        changes = 0
        for j in range(m - 1):
            if grid[n - 1][j] == 'D':
                changes += 1
        for i in range(n - 1):
            if grid[i][m - 1] == 'R':
                changes += 1
                
        results.append(str(changes))
        
    sys.stdout.write('\n'.join(results) + '\n')
solve()