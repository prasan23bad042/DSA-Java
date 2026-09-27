n, k = map(int, input().split())
a = list(map(int, input().split()))

left = 0
right = n - 1
ans = 0

while left <= right:
    if a[left] <= k:
        left += 1
        ans += 1
    elif a[right] <= k:
        right -= 1
        ans += 1
    else:
        break

print(ans)
