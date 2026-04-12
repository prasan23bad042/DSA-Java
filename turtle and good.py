import sys
def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    t = int(input_data[0])
    pointer = 1
    results = []
    for _ in range(t):
        n = int(input_data[pointer])
        s = input_data[pointer + 1]
        pointer += 2
        if s[0] != s[-1]:
            results.append("YES")
        else:
            results.append("NO")
    sys.stdout.write("\n".join(results) + "\n")
solve()