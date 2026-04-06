import sys
def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    t = int(input_data[0])
    current = 1
    results = []
    for _ in range(t):
        n = int(input_data[current])
        answers = input_data[current + 1]
        current += 2
        count_a = answers.count('A')
        count_b = answers.count('B')
        count_c = answers.count('C')
        count_d = answers.count('D')
        total_score = (
            min(count_a, n) +
            min(count_b, n) +
            min(count_c, n) +
            min(count_d, n)
        )
        results.append(str(total_score))
    sys.stdout.write("\n".join(results) + "\n")
solve()