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
        if arr[0] + arr[1] <= arr[-1]:
            output.append(f"1 2 {n}")
        else:
            output.append("-1")
    print('\n'.join(output))
solve()