class Solution:
    def solve(self):
        import sys
        input = sys.stdin.readline
        t = int(input())
        for _ in range(t):
            n, j, k = map(int,input().split())
            a = list(map(int,input().split()))
            x = a[j-1]
            cnt = 0
            for v in a:
                if v > x:
                    cnt += 1
            if k == 1:
                if cnt == 0:
                    print("YES")
                else:
                    print("NO")
            else:
                if cnt < k:
                    print("YES")
                else:
                    print("NO")