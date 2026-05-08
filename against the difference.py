import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    t = int(input_data[0])
    results = []
    
    for i in range(1, t + 1):
        n = int(input_data[i])
        additional_needed = (3 - (n % 3)) % 3
        results.append(str(additional_needed))
    sys.stdout.write("\n".join(results) + "\n")
solve()