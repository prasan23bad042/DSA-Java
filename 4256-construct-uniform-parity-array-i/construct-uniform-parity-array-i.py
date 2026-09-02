class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        n = len(nums1)
        e = []
        o = []
        for x in nums1:
            if x%2 == 0:
                e.append(x)
            else:
                o.append(x)
        ne = len(e)
        no = len(o)
        if no != 1:
            ce = 1
        else:
            ce = 0
        if no > 0:
            co = 1
        else:
            co = 0
        if ce or co:
            return True
        else:
            return False
        