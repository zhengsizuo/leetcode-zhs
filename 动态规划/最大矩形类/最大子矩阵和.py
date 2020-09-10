# 重点在于滚动遍历计算前缀和之后转化为一维的最大子序和问题
class Solution:
    def getMaxMatrix(self, matrix):
        m = len(matrix)
        n = len(matrix[0])
        max_sum = -float('inf')
        res = [0, 0, 0, 0]

        for i in range(m):  # 以i为上边，从上到下扫描
            b = [0] * n  # 由列前缀和组成的一维数组
            for k in range(i, m):  # 子矩阵的下边
                for j in range(n):
                    b[j] += matrix[k][j]

                cur_max, start, end = self.getMax(b)
                if cur_max > max_sum:
                    res = [i, start, k, end]
                    max_sum = cur_max

        return res

    def getMax(self, nums):
        dp_i = nums[0]
        begin_idx = 0
        start, end = 0, 0
        max_val = nums[0]
        for i in range(1, len(nums)):
            if dp_i < 0:
                dp_i = nums[i]
                begin_idx = i
            else:
                dp_i += nums[i]

            if dp_i > max_val:
                max_val = dp_i
                start = begin_idx
                end = i

        return max_val, start, end

