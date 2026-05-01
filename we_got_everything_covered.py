import sys

def solve():
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return
        
    t = int(input_data[0])
    
    results = []
    for i in range(1, 2 * t, 2):
        n = int(input_data[i])
        k = int(input_data[i+1])
        base_block = "".join(chr(ord('a') + j) for j in range(k))
        ans = base_block * n
        
        results.append(ans)
    print('\n'.join(results))
solve()