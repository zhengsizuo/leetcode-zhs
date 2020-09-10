class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort(reverse=True)
        return nums[k-1]


"""快排"""

"""堆排，删除k次根或把前k个数维护成大根堆"""