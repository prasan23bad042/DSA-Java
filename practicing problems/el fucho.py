t = int(input())

for _ in range(t):
    n = int(input())

    w = n
    l = 0
    matches = 0

    while w >= 2 or l >= 2:
        # Matches played in this round
        matches += w // 2
        matches += l // 2

        # Teams remaining/moving to the next round
        new_w = (w + 1) // 2
        new_l = (l + 1) // 2 + w // 2

        w = new_w
        l = new_l

    # Final match between the last team in each group
    matches += 1

    print(matches)
