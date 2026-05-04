import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    t = int(input_data[0])
    results = []
    idx = 1
    
    for _ in range(t):
        a = int(input_data[idx])
        b = int(input_data[idx+1])
        c = int(input_data[idx+2])
        idx += 3
        time1 = abs(a - 1)
        time2 = abs(b - c) + abs(c - 1)
        if time1 < time2:
            results.append("1")
        elif time2 < time1:
            results.append("2")
        else:
            results.append("3")
    sys.stdout.write('\n'.join(results) + '\n')
solve()