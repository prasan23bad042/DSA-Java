import sys
input = sys.stdin.readline
for _ in range(int(input())):
    keyboard = input().strip()
    s = input().strip()
    pos = {}
    for i in range(26):
        pos[keyboard[i]] = i
    time = 0
    for i in range(1,len(s)):
        time += abs(pos[s[i]] - pos[s[i-1]])
    print(time)
