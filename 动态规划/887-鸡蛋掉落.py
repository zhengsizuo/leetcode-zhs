"""经典动态规划！！
状态是(K, N)，选择是碎或者没碎，选择之后带来状态转移
"""
from functools import lru_cache

# 超时
class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        @lru_cache(None)
        def dp(K, N):
            # K个鸡蛋，N层楼，确定F的最小移动次数
            print(K, N)
            if K == 1: return N
            if N == 0: return 0

            res = float('inf')
            for i in range(1, N + 1):
                res = min(res,
                          max(dp(K - 1, i - 1),  # 碎了
                              dp(K, N - i)  # 没碎
                              ) + 1
                          )  # 碎或没碎，两种选择状态转移
            return res

        return dp(K, N)


"""使用字典保存重复的递归结果，超时"""
memo = dict()
class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        def dp(K, N):
            # K个鸡蛋，N层楼，确定F的最小移动次数
            print(K, N)
            if K == 1: return N
            if N == 0: return 0

            if (K, N) in memo:
                return memo[(K, N)]
            res = float('inf')
            for i in range(1, N+1):
                res = min(res,
                            max(dp(K-1, i-1), # 碎了
                                dp(K, N-i)  # 没碎
                            )+1
                        )  # 碎或没碎，两种选择状态转移
                print(i, memo, res)
            memo[(K, N)] = res
            return res


        return dp(K, N)

"""更高效的解法之一：二分搜索优化"""
class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        memo = dict()
        def dp(K, N):
            # K个鸡蛋，N层楼，确定F的最小移动次数
            # print(K, N)
            if K == 1: return N
            if N == 0: return 0
            if (K, N) in memo:
                return memo[(K, N)]

            res = float('INF')
            # 用二分搜索代替线性搜索
            lo, hi = 1, N
            while lo <= hi:
                mid = (lo + hi) // 2
                broken = dp(K - 1, mid - 1) # 碎
                not_broken = dp(K, N - mid) # 没碎
                # res = min(max(碎，没碎) + 1)
                if broken > not_broken:
                    hi = mid - 1
                    res = min(res, broken + 1)
                else:
                    lo = mid + 1
                    res = min(res, not_broken + 1)

            memo[(K, N)] = res
            return res

        return dp(K, N)

"""更高效的解法之一：重新定义dp含义"""
sl = Solution()
print(sl.superEggDrop(2, 6))
print(memo)