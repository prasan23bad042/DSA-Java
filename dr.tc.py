import sys
t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    s = sys.stdin.readline().strip()
    ones = s.count('1')
    ans = ones*(n-1) + (n - ones)
    print(ans)