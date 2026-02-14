for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    ok = True
    for i in range(1,n):
        diff = abs(arr[i] - arr[i - 1])
        if diff != 5 and diff != 7:
            ok = False
            break
    if ok:
        print("YES")
    else:
        print("NO")
