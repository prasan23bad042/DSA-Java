import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    
    if not data:
        return

    iterator = iter(data)
    num_test_cases = int(next(iterator))
    
    output = []
    
    for _ in range(num_test_cases):
        n = int(next(iterator))
        s = [int(next(iterator)) for _ in range(n)]
        f = [int(next(iterator)) for _ in range(n)]
        
        durations = []
        durations.append(str(f[0] - s[0]))
        for i in range(1, n):
            start_time = max(s[i], f[i-1])
            durations.append(str(f[i] - start_time))
        output.append(" ".join(durations))
    print("\n".join(output))
solve()
