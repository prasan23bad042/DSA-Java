import sys
def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    t = int(input_data[0])
    results = []
    for i in range(1, t + 1):
        n = int(input_data[i])
        if n % 4 == 0:
            results.append("YES")
        else:
            results.append("NO")
    sys.stdout.write("\n".join(results) + "\n")
solve()