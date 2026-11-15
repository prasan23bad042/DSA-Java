t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    s = input().strip()

    if k == 0 or s == s[::-1]:
        print(1)
    else:
        print(2)
      
