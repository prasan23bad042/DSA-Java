import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())

    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    k = -1
    ok = True

    for i in range(n):
        if b[i] > a[i]:
            ok = False
            break

        if b[i] > 0:
            diff = a[i] - b[i]

            if k == -1:
                k = diff
            elif diff != k:
                ok = False
                break

    if not ok:
        print("NO")
        continue

    # If every element in b is zero
    if k == -1:
        print("YES")
        continue

    for i in range(n):
        if b[i] == 0 and a[i] > k:
            ok = False
            break

    print("YES" if ok else "NO")
