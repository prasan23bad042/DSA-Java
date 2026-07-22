import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    enemy = list(input().strip())
    gregor = input().strip()

    ans = 0

    for i in range(n):
        if gregor[i] == '1':
            if enemy[i] == '0':
                ans += 1
                enemy[i] = '2'
            elif i > 0 and enemy[i - 1] == '1':
                ans += 1
                enemy[i - 1] = '0'
            elif i + 1 < n and enemy[i + 1] == '1':
                ans += 1
                enemy[i + 1] = '0'

    print(ans)
