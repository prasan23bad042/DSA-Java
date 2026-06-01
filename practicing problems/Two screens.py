import sys

def solve():
    # Read all input from standard input efficiently
    input = sys.stdin.read
    data = input().split()
    
    if not data:
        return

    num_test_cases = int(data[0])
    results = []
    
    idx = 1
    for _ in range(num_test_cases):
        s = data[idx]
        t = data[idx+1]
        idx += 2
        
        len_s = len(s)
        len_t = len(t)
        
        # Find the length of the longest common prefix
        lcp_length = 0
        min_len = min(len_s, len_t)
        
        while lcp_length < min_len and s[lcp_length] == t[lcp_length]:
            lcp_length += 1
            
        # Calculate minimum seconds based on our formula
        if lcp_length > 0:
            total_time = len_s + len_t - lcp_length + 1
        else:
            total_time = len_s + len_t
            
        results.append(str(total_time))
        
    # Print all results separated by a newline
    print('\n'.join(results))

if __name__ == '__main__':
    solve()
  
