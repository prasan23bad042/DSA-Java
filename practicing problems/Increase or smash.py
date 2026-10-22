t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    k = len(set(a))
    print(2 * k - 1)
  
