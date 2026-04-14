import sys

def solve():
    try:
        line1 = sys.stdin.readline().split()
        if not line1: return
        n, x = map(int,line1)
        a = list(map(int,sys.stdin.readline().split()))
    except ValueError:
        return
    a.sort(reverse=True)
    total_teams = 0
    current_team_size = 0

    for skill in a:
        current_team_size += 1
        if skill * current_team_size >= x:
            total_teams += 1
            current_team_size = 0
    print(total_teams)

def main():
    line = sys.stdin.readline()
    if line:
        t = int(line)
        for _ in range(t):
            solve()
main()