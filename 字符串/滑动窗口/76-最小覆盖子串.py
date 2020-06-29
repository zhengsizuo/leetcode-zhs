from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left, right = 0, 0
        need = Counter(t)
        window = Counter()

        match = 0  # 统计窗口window和need中字符的匹配数
        minLen = float('inf')
        while right < len(s):
            c1 = s[right]
            if c1 in t:
                window[c1] += 1
                if window[c1] == need[c1]:
                    match += 1
                    # print('window: ', window, 'match: ', match)
            right += 1
            # print('left: ', left, 'right: ', right)
            # 当window符合要求后，开始收缩左指针
            while match == len(need):
                if right - left < minLen:
                    minLen = right - left
                    start = left
                c2 = s[left]
                if c2 in t:
                    window[c2] -= 1
                    if window[c2] < need[c2]:
                        # 这一句容易写错
                        match -= 1
                left += 1

        return '' if minLen == float('inf') else s[start:start + minLen]

s = 'ADOBECODEBANC'
t = 'ABC'
sl = Solution()
print(sl.minWindow(s, t))