import sys
from collections import Counter

def solve():
    input = sys.stdin.read
    data = input().split()
    
    if not data:
        return

    # Number of test cases
    t = int(data[0])
    
    idx = 1
    out = []
    
    for _ in range(t):
        n = int(data[idx])
        idx += 1
        
        # Extract the array for the current testcase
        arr = [int(x) for x in data[idx : idx + n]]
        idx += n
        
        # Count the frequency of each number
        counts = Counter(arr)
        
        # The answer is the maximum frequency of any element
        max_frequency = max(counts.values())
        out.append(str(max_frequency))
        
    # Print all outputs separated by a newline
    print('\n'.join(out))

if __name__ == '__main__':
    solve()
