class Solution:
    def tripletCount(self, a: List[int], b: List[int], c: List[int]) -> int:
        def count(arr):
            even = odd = 0
            for x in arr:
                if bin(x).count('1') % 2 == 0:
                    even += 1
                else:
                    odd += 1
            return even, odd

        ea, oa = count(a)
        eb, ob = count(b)
        ec, oc = count(c)
        return ea*eb*ec + ea*ob*oc + oa*eb*oc + oa*ob*ec
