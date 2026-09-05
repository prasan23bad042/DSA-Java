class Solution:
    def solve(self, a, b):
        n = len(a)

        i = n - 1
        j = n - 1
        ans = 0

        while i >= 0 and j >= 0:
            if a[i] <= b[j]:
                # Existing problem can satisfy this requirement
                i -= 1
                j -= 1
            else:
                # This problem is too difficult, replace it
                ans += 1
                i -= 1

        return ans


# Input
t = int(input())

for _ in range(t):
    n = int(input())

    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    obj = Solution()
    print(obj.solve(a, b))
