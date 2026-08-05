import sys

input = sys.stdin.readline

n, q = map(int, input().split())
s = input().strip()

pref = [0] * (n + 1)

for i in range(1, n + 1):
    pref[i] = pref[i - 1] + (ord(s[i - 1]) - ord('a') + 1)

for _ in range(q):
    l, r = map(int, input().split())
    print(pref[r] - pref[l - 1])import sys

input = sys.stdin.readline

n, q = map(int, input().split())
s = input().strip()

pref = [0] * (n + 1)

for i in range(1, n + 1):
    pref[i] = pref[i - 1] + (ord(s[i - 1]) - ord('a') + 1)

for _ in range(q):
    l, r = map(int, input().split())
    print(pref[r] - pref[l - 1])
