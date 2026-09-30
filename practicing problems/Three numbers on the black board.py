class Solution:
    def solve(self):
        t = int(input())

        for _ in range(t):
            a, b, c = map(int, input().split())

            x, y, z = sorted([a, b, c])

            ans = min(z - x, y)

            print(ans)


Solution().solve()
