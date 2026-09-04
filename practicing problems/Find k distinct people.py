class Solution:
    def canFormPalindrome(self, s):
        freq = [0] * 26

        for ch in s:
            freq[ord(ch) - ord('a')] += 1

        odd = 0

        for count in freq:
            if count % 2 == 1:
                odd += 1

        return odd <= 1
