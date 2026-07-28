from collections import Counter

t = int(input())

for _ in range(t):
    s = input().strip()

    freq = Counter(s)

    left = []

    for ch in sorted(freq):
        left.append(ch * freq[ch])

    left = "".join(left)

    print(left + left[::-1])
