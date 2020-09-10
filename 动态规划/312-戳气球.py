"""递归法，自顶向下，超出时间限制"""
class Solution:
    def maxCoins(self, nums) -> int:
        def dp(nums):
            # base case
            if len(nums) == 0: return 0
            res = -float('INF')
            for i in range(len(nums)):
                cur_coin = 0
                if i == 0 and len(nums) != 1:
                    cur_coin = 1 * nums[i] * nums[i + 1]
                elif i == 0 and len(nums) == 1:
                    cur_coin = 1 * nums[i] * 1
                elif i == len(nums) - 1:
                    cur_coin = nums[i - 1] * nums[i] * 1
                else:
                    cur_coin = nums[i - 1] * nums[i] * nums[i + 1]

                res_new = cur_coin + dp(nums[:i] + nums[i + 1:])
                res = max(res, res_new)

            return res if res != -float('INF') else 0

        return dp(nums)

"""加备忘录，依然超出时间限制"""
class Solution:
    def maxCoins(self, nums) -> int:
        # 备忘录
        memo = []
        coin_memo = []

        def dp(nums):
            try:
                index = memo.index(nums)
                return coin_memo[index]
            except:
                # base case
                if len(nums) == 0: return 0
                res = -float('INF')
                for i in range(len(nums)):
                    cur_coin = 0
                    if i == 0 and len(nums) != 1:
                        cur_coin = 1 * nums[i] * nums[i + 1]
                    elif i == 0 and len(nums) == 1:
                        cur_coin = 1 * nums[i] * 1
                    elif i == len(nums) - 1:
                        cur_coin = nums[i - 1] * nums[i] * 1
                    else:
                        cur_coin = nums[i - 1] * nums[i] * nums[i + 1]

                    res_new = cur_coin + dp(nums[:i] + nums[i + 1:])
                    res = max(res, res_new)

                # 记入备忘录
                memo.append(nums)
                coin_memo.append(res if res != -float('INF') else 0)

            return coin_memo[memo.index(nums)]

        return dp(nums)

"""分治+动态规划（带备忘录）"""
class Solution:
    def maxCoins(self, nums):
        if not nums:
            return 0

        def getMaxCoins(nums, start, end, memo):
            # 先检查备忘录
            if memo[start][end] != 0:
                return memo[start][end]
            # base case
            if start == end - 1:
                return 0

            ret = 0
            for k in range(start + 1, end):
                left = getMaxCoins(nums, start, k, memo)  # 左边部分最大硬币数
                right = getMaxCoins(nums, k, end, memo)  # 右边最大的硬币数

                ret = max(ret, left + right + nums[start] * nums[k] * nums[end])

            memo[start][end] = ret
            return ret

        nums = [1, *nums, 1]  # 增加两侧区间的虚拟气球
        memo = [[0] * len(nums) for _ in range(len(nums))]
        return getMaxCoins(nums, 0, len(nums) - 1, memo)


"""用dp数组，注意分析遍历顺序"""


class Solution:
    def maxCoins(self, nums) -> int:
        if not nums: return 0

        nums = [1, *nums, 1]  # 首尾添加1
        n = len(nums)
        dp = [[0] * n for _ in range(n)]  # dp[i][j]表示(i,j)开区间获得的硬币最大数量

        # 遍历顺序是根据base case和状态转移方程推出来的
        for i in range(n - 2, -1, -1):
            # i从下到上
            for j in range(i + 1, n):
                # j从左到右
                for k in range(i + 1, j):
                    dp[i][j] = max(dp[i][j], dp[i][k] + dp[k][j] + nums[i] * nums[k] * nums[j])  # 假设最后戳爆的气球是k

        for d in dp:
            print(d)
        return dp[0][n - 1]


nums = [3, 1, 5, 8]
sl = Solution()
res = sl.maxCoins(nums)
print(res)
