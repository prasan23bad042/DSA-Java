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
        k = int(next(iterator))
        brand_earnings = {}
        
        for _ in range(k):
            b = int(next(iterator))
            c = int(next(iterator))
            brand_earnings[b] = brand_earnings.get(b, 0) + c
        sorted_earnings = sorted(brand_earnings.values(), reverse=True)
        max_profit = sum(sorted_earnings[:n])
        
        out.append(str(max_profit))
    sys.stdout.write('\n'.join(out) + '\n')
solve()