t = int(input())

for _ in range(t):
    x = int(input())
    arr = list(map(int, input().split()))
    
    k = x
    
    for _ in range(2):
        if k == 0:
            break
        k = arr[k - 1]
    
    if k == 0:
        print("NO")
    else:
        print("YES")