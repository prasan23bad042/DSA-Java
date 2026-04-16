import sys

def solve():
    input = sys.stdin.read().split()
    if not input:
        return
    ptr = 0
    t = int(input[ptr])
    ptr += 1
    results = []
    for _ in range(t):
        n = int(input[ptr])
        ptr += 1
        a = []
        for i in range(n):
            a.append(int(input[ptr]))
            ptr += 1
        sorted_a = sorted(a)
        
        possible = True
        for i in range(n):
            if a[i] % 2 != sorted_a[i] % 2:
                possible = False
                break
        if possible:
            results.append("YES")
        else:
            results.append("NO")
    sys.stdout.write("\n".join(results) + "\n")
solve()