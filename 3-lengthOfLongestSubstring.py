class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0

        i, maxLen = 0, 1
        j = 1
        while j < len(s):
            if s[j] in s[i:j]:
                if (j - i) > maxLen:
                    maxLen = j - i
                i += 1
                j = i + 1
            else:
                j += 1

        if (j - i) > maxLen:
            # 排除子串处于最后一部分的情况
            maxLen = j - i
        return maxLen


"""leecode上用滑动窗口的推荐解法"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:return 0
        left = 0
        lookup = set()
        n = len(s)
        max_len = 0
        cur_len = 0
        for i in range(n):
            cur_len += 1
            while s[i] in lookup:
                lookup.remove(s[left])
                left += 1
                cur_len -= 1
            if cur_len > max_len:max_len = cur_len
            lookup.add(s[i])
        return max_len


# 链接：https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/solution/hua-dong-chuang-kou-by-powcai/
