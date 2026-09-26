class Solution:
    def maxProfit(self, n, a, b):
        k = b - a + 1

        # k cannot be negative
        k = max(0, k)

        # k cannot exceed n or b
        k = min(k, n, b)

        # Profit from k promotional buns
        promo = k * b - k * (k - 1) // 2

        # Profit from remaining buns
        normal = (n - k) * a

        return promo + normal


t = int(input())

for _ in range(t):
    n, a, b = map(int, input().split())
    print(Solution().maxProfit(n, a, b))
