import sys

def solve():
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return
        
    t = int(input_data[0])
    results = []
    for i in range(1, t + 1):
        s = input_data[i]
        rearranged_s = "".join(sorted(s))
        
        results.append(rearranged_s)
    print("\n".join(results))
solve()