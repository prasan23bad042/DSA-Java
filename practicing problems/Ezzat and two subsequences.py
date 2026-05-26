import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    iterator = iter(input_data)
    num_test_cases = int(next(iterator))
    
    output = []
    for _ in range(num_test_cases):
        n = int(next(iterator))
        
        arr = [int(next(iterator)) for _ in range(n)]
        
        max_val = max(arr)
        total_sum = sum(arr)
        
        remaining_sum = total_sum - max_val
        
        max_avg_sum = max_val + (remaining_sum / (n - 1))
        
        output.append(f"{max_avg_sum:.9f}")
        
    sys.stdout.write('\n'.join(output) + '\n')

if __name__ == '__main__':
    solve()
