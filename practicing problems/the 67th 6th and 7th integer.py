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
        a = [int(x) for x in data[idx:idx+7]]
        idx += 7
        total_sum = sum(a)
        max_val = max(a)
        max_possible_sum = 2 * max_val - total_sum
        results.append(str(max_possible_sum))
    sys.stdout.write('\n'.join(results) + '\n')
solve()
