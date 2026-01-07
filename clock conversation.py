for _ in range(int(input())):
    s = input().strip()
    h = int(s[:2])
    m = s[3:]
    if h == 0:
        hh = 12
        ap = "AM"
    elif h < 12:
        hh = h
        ap = "AM"
    elif h == 12:
        hh = 12
        ap = "PM"
    else:
        hh = h - 12
        ap = "PM"
    if hh < 10:
        hh = "0" + str(hh)
    else:
        hh = str(hh)
    print(hh + ":" + m, ap)
