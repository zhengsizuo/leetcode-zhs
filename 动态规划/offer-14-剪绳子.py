class Solution:
    def cuttingRope(self, n: int) -> int:
        if n == 2: return 1
        if n == 3: return 2
        memo = {2: 2, 3: 3, 4: 4, 5: 6}

        def dp(n):
            if n in memo:
                return memo[n]

            res = 0
            for i in range(2, n // 2 + 1):
                res = max(res, dp(i) * dp(n - i))
            memo[n] = res
            return res

        return dp(n)


"""内存更优的解法"""
import functools


class Solution:
    def cuttingRope(self, n: int) -> int:
        if n == 2: return 1
        if n == 3: return 2
        memo = {2: 2, 3: 3, 4: 4, 5: 6}

        @functools.lru_cache(None)
        def dp(n):
            if n == 2: return 2
            if n == 3: return 3

            res = 0
            for i in range(2, n // 2 + 1):
                res = max(res, dp(i) * dp(n - i))

            return res

        return dp(n)