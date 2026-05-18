import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    iterator = iter(input_data)
    t_cases = int(next(iterator))
    out = []
    
    for _ in range(t_cases):
        n = int(next(iterator))
        for _ in range(n):
            next(iterator)
            
        available_digits = 10 - n
        ways_to_choose_digits = (available_digits * (available_digits - 1)) // 2
        total_sequences = ways_to_choose_digits * 6
        
        out.append(str(total_sequences))
    sys.stdout.write('\n'.join(out) + '\n')
solve()