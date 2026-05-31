import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    
    if not data:
        return
    
    t = int(data[0])
    idx = 1
    
    out = []
    for _ in range(t):
        n = int(data[idx])
        S = [int(x) for x in data[idx+1 : idx+1+n]]
        idx += 1 + n
        
        c0 = S.count(0)
        c1 = S.count(1)
        sum_gt_1 = sum(x for x in S if x >= 2)
        
        max_score = 0
        for k in range(min(c0, c1) + 1):
            score_pairs = 2 * k
            score_ones = c1 - k
            score_zeros = c0 - k
            
            total = sum_gt_1 + score_pairs + score_ones + score_zeros
            if total > max_score:
                max_score = total
                
        out.append(str(max_score))
        
    print('\n'.join(out))
solve()