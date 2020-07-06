"""滑动窗口的思路不对，因为数组是有负数的"""


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0

        count = 0
        left, right = 0, 0
        while right < len(nums):
            window = nums[left:right + 1]
            sum_win = sum(window)
            right += 1
            # 缩减窗口条件判断
            while sum_win >= k and left < len(nums):
                if sum_win == k:
                    count += 1

                sum_win -= nums[left]  # 更新窗口和
                left += 1

        return count


"""前缀和+哈希表优化"""


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hash_map = dict()
        count = 0
        acc = 0
        for n in nums:
            acc += n
            if acc == k:
                count += 1
            if (acc - k) in hash_map.keys():
                count += hash_map[acc - k]
            hash_map.setdefault(acc, 0)
            hash_map[acc] += 1

        return count


nums = [0,0,0,0,0,0,0,0,0,0]
k = 0
