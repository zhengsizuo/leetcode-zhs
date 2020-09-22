"""把每一个小于k的字符找出来多路递归分治"""
from collections import Counter
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if len(s)<k: return 0
        if k==1: return len(s)

        hash_table = Counter(s)
        split = []
        for i in range(len(s)):
            if hash_table[s[i]] < k:
                split.append(i)

        if not split: return len(s)
        left = 0
        res = 0
        split.append(len(s))
        for idx in split:
            res = max(self.longestSubstring(s[left:idx], k), res)
            left = idx + 1

        return res


"""多路分治，把出现最小次数的字符两边分割开"""
from collections import Counter


class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if len(s) < k: return 0
        if k == 1: return len(s)

        hash_table = Counter(s)
        min_char = min(hash_table, key=hash_table.get)
        if hash_table[min_char] >= k:
            return len(s)

        return max(self.longestSubstring(sub_s, k) for sub_s in s.split(min_char))


s = 'aaabbcddddee'
# s = "weitong"
k = 2
sl = Solution()
print(sl.longestSubstring(s, k))


