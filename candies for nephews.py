import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    t = int(input_data[0])
    results = []
    
    for i in range(1, t + 1):
        n = int(input_data[i])
        remainder = n % 3
        
        if remainder == 0:
            results.append(0)
        else:
            results.append(3 - remainder)
    sys.stdout.write('\n'.join(map(str, results)) + '\n')
solve()