import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    
    if not data:
        return
    
    t = int(data[0])
    results = []
    
    # Process each test case
    for i in range(1, t + 1):
        n = int(data[i])
        # Generate the array [1, 2, 3, ..., n]
        ans = [str(j) for j in range(1, n + 1)]
        results.append(" ".join(ans))
        
    # Print all results separated by a newline
    print("\n".join(results))

if __name__ == '__main__':
    solve()
  
