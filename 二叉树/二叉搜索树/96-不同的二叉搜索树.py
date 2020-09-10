"""卡特兰数：关键在于递归i节点左右两边"""
class Solution:
    def numTrees(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1

        G = [0] * (n + 1)
        G[0] = 1
        G[1] = 1
        for k in range(2, n + 1):
            for i in range(1, k + 1):
                G[k] += G[i - 1] * G[k - i]

        return G[-1]