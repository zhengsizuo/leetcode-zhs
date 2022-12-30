"""递归法，自顶向下，超出时间限制"""
# class Solution(object):
#     def rob(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         if not nums:
#             return 0
#         # 边界条件
#         if len(nums) == 1 or len(nums)==2:
#             return max(nums)
#         if len(nums) == 3:
#             return max(nums[0]+nums[2], nums[1])
        
#         if len(nums) >= 4:
#             return max(nums[0]+self.rob(nums[2:]), nums[1]+self.rob(nums[3:]))

"""动态规划，自底向上"""
# class Solution(object):
#     def rob(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         if not nums:
#             return 0
        
#         # 边界条件
#         if len(nums)==1 or len(nums)==2:
#             return max(nums)

#         dp = [nums[0], max(nums[:2])]
#         for i in range(2, len(nums)):
#             dp.append(max(dp[i-1], dp[i-2]+nums[i]))
        
#         return dp[-1]

"""进阶，空间优化为O(1)"""
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prev, curr = 0, 0
        for i in range(len(nums)):
            # curr: dp[k-1]; prev: dp[k-2]
            temp = max(curr, prev+nums[i])
            prev = curr  # dp[k-1]
            curr = temp  # dp[k]
        
        return curr
# nums = [1, 2, 3, 1]
nums = [2, 10, 9, 1, 3]
sl = Solution()
print(sl.rob(nums))

def robber(nums):
    if len(nums) <= 2:
        return max(nums)

    dp = [0]*len(nums)
    dp[0], dp[1] = nums[0], nums[1]
    for i in range(2, len(nums)):
        dp[i] = nums[i] + max(dp[:i-1])  # 相邻不可取

    return max(dp[-2], dp[-1])
