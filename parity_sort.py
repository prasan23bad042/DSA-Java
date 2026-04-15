import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    even = []
    odd = []
    for x in a:
        if x % 2 == 0:
            even.append(x)
        else:
            odd.append(x)
    even.sort()
    odd.sort()
    i = 0 
    j = 0  
    b = []
    for x in a:
        if x % 2 == 0:
            b.append(even[i])
            i += 1
        else:
            b.append(odd[j])
    if b == sorted(a):
        print("YES")
    else:
        print("NO")