import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    t = int(input_data[0])
    results = []
    pointer = 1
    
    for _ in range(t):
        l = int(input_data[pointer])
        r = int(input_data[pointer + 1])
        pointer += 2
        if l == 1 and r == 1:
            results.append(1)
        else:
            results.append(r - l)
            
    sys.stdout.write('\n'.join(map(str, results)) + '\n')
solve()