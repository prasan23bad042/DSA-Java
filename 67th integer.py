import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    t = int(input_data[0])
    results = []
    
    for i in range(1, t + 1):
        x = int(input_data[i])
        results.append(str(x))
    print('\n'.join(results))
solve()