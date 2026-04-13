import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    t = int(input_data[0])
    test_cases = input_data[1:]
    pattern = "Yes" * 20
    
    results = []
    for s in test_cases:
        if s in pattern:
            results.append("YES")
        else:
            results.append("NO")
    sys.stdout.write("\n".join(results) + "\n")
solve()