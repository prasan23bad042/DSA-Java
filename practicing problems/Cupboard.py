n = int(input())

left_ones = 0
right_ones = 0

for _ in range(n):
    l, r = map(int, input().split())
    left_ones += l
    right_ones += r

answer = min(left_ones, n - left_ones) + \
         min(right_ones, n - right_ones)

print(answer)
