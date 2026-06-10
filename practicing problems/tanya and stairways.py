import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    
    if not data:
        return

    n = int(data[0])
    a = [int(x) for x in data[1:]]
    
    stairway_steps = []
    for i in range(1, n):
        if a[i] == 1:
            stairway_steps.append(a[i - 1])
    stairway_steps.append(a[-1])
    print(len(stairway_steps))
    print(*(stairway_steps))
solve()
