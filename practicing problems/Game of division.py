t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    ans = -1

    for i in range(n):
        for j in range(n):
            if i != j and abs(a[i] - a[j]) % k == 0:
                break
        else:
            ans = i
            break

    if ans == -1:
        print("NO")
    else:
        print("YES")
        print(ans + 1)
      
