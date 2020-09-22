
"""前缀和+哈希表优化"""


class Solution:
    def subarraySum(self, nums, k: int) -> int:
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


"""自己写的"""


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hash_table = dict()
        acc = 0
        res = 0
        for n in nums:
            hash_table.setdefault(acc, 0)
            hash_table[acc] += 1
            acc += n

            if acc - k in hash_table:
                res += hash_table[acc - k]

        return res

nums = [0,0,0,0,0,0,0,0,0,0]
k = 0
