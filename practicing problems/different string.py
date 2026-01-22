t = int(input())

for _ in range(t):
    s = input().strip()
    
    # if all characters are same, impossible
    if len(set(s)) == 1:
        print("NO")
        continue
    
    # otherwise, rearrange
    a = sorted(s)
    
    # if sorted string is same as original, reverse it
    if "".join(a) == s:
        a.reverse()
    
    print("YES")
    print("".join(a))
