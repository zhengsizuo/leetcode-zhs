"""经典动态规划！！
状态是(K, N)，选择是碎或者没碎，选择之后带来状态转移
"""
class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        memo = dict()
        def dp(K, N):
            # base case
            if K == 1: return N  # 只有一个鸡蛋的情况只能做线性扫描
            if N == 0: return 0
            if memo[(K, N)]: return memo[(K, N)]