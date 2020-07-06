"""159 / 167 个通过测试用例"""
class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        if len(left) == 0:
            return n - min(right)
        if not right:
            return max(left)

        # 如果左数组都在右数组的左边
        if max(left) < min(right):
            return max(max(left), n - min(right))

        # 讨论相遇的情况
        max_left = max(left)
        min_right = min(right)

        meet_time = (max_left - min_right) // 2
        meet_idx = meet_time + min_right
        res_time = max(n - meet_idx, meet_idx)

        return res_time + meet_time

"""网上题解：理解为穿透"""


class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        if len(left) == 0:
            return n - min(right)
        if not right:
            return max(left)

        return max(max(left), n - min(right))