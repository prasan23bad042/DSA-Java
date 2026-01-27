n, x = map(int,input().split())
ice = x
sad = 0
for _ in range(n):
    t, d = input().split()
    d = int(d)
    if t == '+':
        ice += d
    else:
        if ice >= d:
            ice -= d
        else:
            sad += 1
print(ice, sad)
