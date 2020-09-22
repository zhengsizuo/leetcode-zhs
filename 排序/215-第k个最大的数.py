class Solution:
    def findKthLargest(self, nums, k: int) -> int:
        nums.sort(reverse=True)
        return nums[k-1]


"""自己写的快排，没这么高效"""


class Solution:
    def findKthLargest(self, nums, k: int) -> int:
        def quick_sort(nums):
            if len(nums) < 2:
                return nums
            else:
                pivot = nums[0]
                less = [n for n in nums[1:] if n <= pivot]
                larger = [n for n in nums[1:] if n > pivot]
                if len(larger) >= k:
                    # 如果更大的部分比k大，只排后面部分
                    return quick_sort(larger)
                else:
                    return quick_sort(larger) + [pivot] + quick_sort(less)

        nums = quick_sort(nums)
        print(nums)
        return nums[k - 1]

"""借助快排算法partion的细节，划分元的位置在数组中是不变的，二分查找的思想"""
from typing import List
import random


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        size = len(nums)

        target = size - k
        left = 0
        right = size - 1
        while True:
            index = self.__partition(nums, left, right)
            if index == target:
                return nums[index]
            elif index < target:
                # 下一轮在 [index + 1, right] 里找
                left = index + 1
            else:
                right = index - 1

    #  循环不变量：[left + 1, j] < pivot
    #  (j, i) >= pivot
    def __partition(self, nums, left, right):

        pivot = nums[left]
        j = left
        for i in range(left + 1, right + 1):
            if nums[i] < pivot:
                j += 1
                nums[i], nums[j] = nums[j], nums[i]

        nums[left], nums[j] = nums[j], nums[left]
        return j


# 作者：liweiwei1419
# 链接：https://leetcode-cn.com/problems/kth-largest-element-in-an-array/solution/partitionfen-er-zhi-zhi-you-xian-dui-lie-java-dai-/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

nums = [3, 2, 1, 5, 6, 4]
k = 2
sl = Solution()
print(sl.findKthLargest(nums, k))
"""堆排，删除k次根或把前k个数维护成大根堆"""