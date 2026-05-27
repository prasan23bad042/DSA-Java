import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    t = int(input_data[0])
    results = []
    
    idx = 1
    for _ in range(t):
        n = int(input_data[idx])
        k = int(input_data[idx+1])
        idx += 2
        
        if k == 0:
            results.append("0" * n)
            continue
        if k == n:
            results.append("1" * n)
            continue
            
        total_ones = k
        total_zeros = n - k
        
        A = min(total_ones - 1, total_zeros - 1)
        D = A
        
        C = total_ones - A
        B = total_zeros - D
        
        res = ("1" * A) + ("0" * B) + ("1" * C) + ("0" * D)
        results.append(res)
        
    print('\n'.join(results))

if __name__ == '__main__':
    solve()
