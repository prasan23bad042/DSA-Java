class Solution:
    def solve(self):
        t = int(input())

        for _ in range(t):
            x, y, k = map(int, input().split())

            d = abs(x - y)

            # Strategy 1:
            # Pick up the key first, then go to the chest.
            ans1 = y + d

            # Strategy 2:
            # Go to the chest, carry it towards the key
            # for at most k seconds, then handle the remaining distance.
            carry = min(k, d)
            ans2 = x + 2 * d - carry

            print(min(ans1, ans2))


Solution().solve()
