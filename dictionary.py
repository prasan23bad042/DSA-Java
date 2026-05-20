import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    t = int(input_data[0])
    results = []
    
    for i in range(1, t + 1):
        word = input_data[i]
        c1 = word[0]
        c2 = word[1]
        
        idx1 = ord(c1) - ord('a')
        idx2 = ord(c2) - ord('a')
        ans = idx1 * 25
        
        if idx2 < idx1:
            ans += idx2 + 1
        else:
            ans += idx2
            
        results.append(str(ans))
    print('\n'.join(results))
solve()