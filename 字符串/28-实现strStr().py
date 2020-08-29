"""调函数大法"""
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle: return 0

        try:
            return haystack.index(needle)
        except:
            return -1

"""官方题解，不超时"""
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        L, n = len(needle), len(haystack)

        for start in range(n - L + 1):
            if haystack[start: start + L] == needle:
                return start
        return -1



class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle: return 0

        i, j = 0, 0
        while i < len(haystack) and j < len(needle):
            if haystack[i] != needle[j]:
                i += 1
            else:
                while i < len(haystack) and j < len(needle) and haystack[i] == needle[j]:
                    i += 1
                    j += 1

                if j == len(needle):
                    return i - j

                # 若没匹配到，i和j均回溯
                i -= (j-1)
                j = 0

        return -1


haystack = "mississippi"
needle ='issip'
sl = Solution()
print(sl.strStr(haystack, needle))