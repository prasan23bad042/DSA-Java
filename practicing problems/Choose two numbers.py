class Solution:
    def chooseNumbers(self, A, B):
        setA = set(A)
        setB = set(B)

        for a in A:
            for b in B:
                s = a + b

                if s not in setA and s not in setB:
                    return a, b
