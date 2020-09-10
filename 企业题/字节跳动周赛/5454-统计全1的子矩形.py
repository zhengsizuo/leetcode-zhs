# 与85-最大矩形相似
class Solution:
    def numSubmat(self, mat) -> int:
        if not mat or not mat[0]: return 0

        rows, cols = len(mat), len(mat[0])
        dp = [[0] * cols for _ in range(rows)]  # DP 初始化

        ans = 0
        for i in range(rows):
            for j in range(cols):
                if mat[i][j]:
                    dp[i][j] = ((dp[i][j - 1] + 1) if j > 0 else 1)
                    mmin = float('inf')
                    for k in range(i, -1, -1):  # 从i开始遍历,到0结束, 计算能组成的矩阵个数
                        mmin = min(mmin, dp[k][j])
                        ans += mmin
                        print("i: %d \t j:%d \t ans: %d \t " % (i, j, ans))
                        # 提前结束循环
                        if mmin == 0:
                            break
        return ans


mat = [[1, 0, 1], [1, 1, 0], [1, 1, 0]]
sl = Solution()
print(sl.numSubmat(mat))
# 作者：dz - lee
# 链接：https: // leetcode - cn.com / problems / count - submatrices -
# with-all - ones / solution / dpdong - tai - gui - hua - python3 - by - dz - lee /
#     来源：力扣（LeetCode）
#     著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。