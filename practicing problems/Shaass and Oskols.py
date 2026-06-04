import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    
    if not data:
        return
    n = int(data[0])
    a = [int(x) for x in data[1:n+1]]
    m = int(data[n+1])
    queries_start = n + 2
    idx = queries_start
    
    for _ in range(m):
        x = int(data[idx]) - 1
        y = int(data[idx+1])
        idx += 2
        left_birds = y - 1
        right_birds = a[x] - y
        if x - 1 >= 0:
            a[x - 1] += left_birds
        if x + 1 < n:
            a[x + 1] += right_birds
        a[x] = 0
    for count in a:
        print(count)
solve()
