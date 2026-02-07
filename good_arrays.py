t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    ans = 0
    i = 0
    while i < n:
        j = i
        while j < n and (a[j] % 2) == (a[i] % 2):
            j += 1
        ans += (j - i - 1)
        i = j
    print(ans)
