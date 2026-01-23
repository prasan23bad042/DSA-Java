for _ in range(int(input())):
    s = input().strip()
    if len(s) >= 3 and s.startswith("10"):
        x = s[2:]
        if x[0] != '0' and int(x) >= 2:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")
