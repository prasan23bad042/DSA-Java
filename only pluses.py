import sys
input = sys.stdin.readline
for _ in range(int(input())):
   a, b, c = map(int,input().split())
   arr = [a, b, c]
   for _ in range(5):
      arr.sort()
      arr[0] += 1
   print(arr[0] * arr[1] * arr[2])
