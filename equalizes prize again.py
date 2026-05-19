import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    
    if not data:
        return

    num_queries = int(data[0])
    idx = 1
    
    out = []
    for _ in range(num_queries):
        n = int(data[idx])
        prices = [int(x) for x in data[idx + 1 : idx + 1 + n]]
        idx += 1 + n
        
        total_sum = sum(prices)
        min_equal_price = (total_sum + n - 1) // n
        out.append(str(min_equal_price))
    print('\n'.join(out))
solve()