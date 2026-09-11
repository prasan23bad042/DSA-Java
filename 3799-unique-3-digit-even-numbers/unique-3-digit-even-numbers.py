class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        nums,lis = 0,set()
        for i in range(len(digits)):
            for j in range(len(digits)):
                for k in range(len(digits)):
                    if(digits[i] == 0):
                        continue
                    if i == j or i==k or j == k:
                        continue
                    if digits[k] % 2 != 0:
                        continue
                    nums = digits[i] * 100 + digits[j] * 10 + digits[k]
                    lis.add(nums)
        return len(lis)