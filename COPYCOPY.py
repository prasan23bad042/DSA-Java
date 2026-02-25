import sys
input = sys.stdin.readline
ans = []
for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    ans.append(str(len(set(a))))
print("\n".join(ans))