"""我我写的双指针法，测试用例[1,3,2,2,2]类型不能通过"""
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        if len(nums) == (0 or 1): return 0

        l = 0
        r = len(nums) - 1
        while l < len(nums) - 1 and nums[l + 1] > nums[l]:
            l += 1
        while r > 0 and nums[r - 1] <= nums[r]:
            r -= 1

        if r <= l:
            return 0
        else:
            return r - l + 1


"""网上参考的双指针法，用最小最大值，效率不高"""
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        l,r = 0, len(nums)-1
        while l <= r:
            Max = max(nums[l:r+1])
            Min = min(nums[l:r+1])
            if nums[l] == Min:
                l += 1
            elif nums[r] == Max:
                r -= 1
            else:
                break
        return r-l+1

"""排序，比较最左边和最右边最不匹配的元素"""