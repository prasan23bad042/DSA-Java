import sys
def solve():
    # Use fast I/O for competitive programming
    input = sys.stdin.read().split()
    if not input:
        return
    t = int(input[0])
    pointer = 1
    results = []
    for _ in range(t):
        n = int(input[pointer])
        pointer += 1
        a = list(map(int,input[pointer : pointer + n]))
        pointer += n
        b = list(map(int,input[pointer : pointer + n]))
        pointer += n
        # Calculate the sum of (a_i - b_i) only for cases where a_i > b_i
        total_decreases = 0
        for i in range(n):
            if a[i] > b[i]:
                total_decreases += (a[i] - b[i])
        # The number of iterations is the total decreases possible + 1
        # (The +1 is the iteration where Step 1 is checked and fails)
        results.append(str(total_decreases + 1))
    # Print all results separated by newlines
    sys.stdout.write("\n".join(results) + "\n")
solve()
