class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums)==0:
            return False
        if len(nums)==1:
            return True
        
        i = len(nums)-1  #从倒数第一个位置开始回溯
        while(i != 0):
            # 对第i个位置来说，前i-1个数中一定有满足条件
            # 所谓条件指与i的距离小于等于该位置的数值
            for index in range(i-1, -1, -1):
                if nums[index] >= (i-index):
                    i = index
                elif index==0 and nums[index]<(i-index):
                    return False
        
        return True


"""官方题解，贪心法"""
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n, rightmost = len(nums), 0
        for i in range(n):
            if i <= rightmost:
                # 看从i能不能跳更远，若能则更新
                rightmost = max(rightmost, i + nums[i])
                if rightmost >= n - 1:
                    # 到达最后一个位置
                    return True
        return False

# https://leetcode-cn.com/problems/jump-game/solution/tiao-yue-you-xi-by-leetcode-solution/
