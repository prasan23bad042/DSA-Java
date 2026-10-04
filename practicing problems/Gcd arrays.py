t = int(input())

for _ in range(t):
    l, r, k = map(int, input().split())

    if l == r:
        print("YES" if l > 1 else "NO")
    else:
        odd = (r + 1) // 2 - l // 2

        if odd <= k:
            print("YES")
        else:
            print("NO")
