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