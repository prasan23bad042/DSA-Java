import sys

class Solution:
    def solve(self):
        input = sys.stdin.read
        data = input().split()
        
        if not data:
            return
        
        t = int(data[0])
        idx = 1
        out = []
        
        for _ in range(t):
            n = int(data[idx])
            arr = [int(x) for x in data[idx + 1 : idx + 1 + n]]
            idx += 1 + n
            
            min_val = min(arr)
            
            if min_val % 2 != 0:
                out.append("YES")
            else:
                has_odd = any(x % 2 != 0 for x in arr)
                if has_odd:
                    out.append("NO")
                else:
                    out.append("YES")
                    
        print('\n'.join(out))
Solution().solve()
