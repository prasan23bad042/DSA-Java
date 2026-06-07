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
        idx += 1
        
        # Read the array for the current test case
        a = [int(x) for x in data[idx:idx+n]]
        idx += n
        
        max_needed = 0
        # Check every adjacent pair
        for i in range(n - 1):
            if a[i] > a[i+1]:
                # If a violation is found, we need at least a[i] operations
                if a[i] > max_needed:
                    max_needed = a[i]
                    
        out.append(str(max_needed))
        
    # Print all results separated by newlines
    print('\n'.join(out))

if __name__ == '__main__':
    solve()
  
