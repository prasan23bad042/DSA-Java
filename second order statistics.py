n = int(input())
arr = list(map(int, input().split()))

unique = sorted(set(arr))

if len(unique) < 2:
    print("NO")
else:
    print(unique[1])
