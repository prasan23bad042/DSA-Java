import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    t = int(input_data[0])
    pointer = 1
    results = []
    
    for _ in range(t):
        n = int(input_data[pointer])
        pointer += 1
        unhappy_count = 0
        for i in range(1, n + 1):
            p_i = int(input_data[pointer])
            if p_i == i:
                unhappy_count += 1
            pointer += 1
        ans = (unhappy_count + 1) // 2
        results.append(str(ans))
    sys.stdout.write('\n'.join(results) + '\n')
solve()