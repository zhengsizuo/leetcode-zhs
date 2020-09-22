"""两数之和扩展版，继续使用哈希表方法，时间复杂度O(n^2)"""
class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        n = len(A)
        if n == 0: return 0

        res = 0
        lookup = dict()
        for a in A:
            for b in B:
                lookup.setdefault(a + b, 0)
                lookup[a + b] += 1
        for c in C:
            for d in D:
                if -(c + d) in lookup:
                    res += lookup[-(c + d)]

        return res