for _ in range(int(input())):
    n = int(input())
    res = ""
    for i in range(3):   
        for v in range(1, 27):
            rem = n - v
            left = 2 - i
            if left*1 <= rem <= left*26:
                res += chr(ord('a') + v - 1)
                n -= v
                break
    print(res)
