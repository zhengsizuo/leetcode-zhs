"""暴力法，超时"""

class Solution:
    def findAnagrams(self, s: str, p: str):
        p = sorted(p)
        len_p = len(p)
        len_s = len(s)
        i = 0
        res = []
        while i != (len_s - len_p + 1):
            if sorted(s[i:i + len_p]) == p:
                res.append(i)
            i += 1

        return res


"""滑动窗口模板"""
from collections import Counter
# Counter类可以用于统计词频
class Solution:
    def findAnagrams(self, s: str, p: str):
        left, right = 0, 0  # 左右指针
        window, need = Counter(), Counter(p)

        res = []
        while right < len(s):
            c1 = s[right]
            if c1 in p:
                window[c1] += 1
                print(window)
            right += 1
            while (right - left) >= len(p):
                # 收缩左窗口
                if window == need:
                    res.append(left)
                c2 = s[left]
                if c2 in p:
                    window[c2] -= 1  # 更新窗口
                left += 1

        return res



s = 'cbaebabacd'
p = 'abc'
sl = Solution()
print(sl.findAnagrams(s, p))