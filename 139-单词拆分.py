# class Solution:
#     def match(self, s, word):
#         # 匹配模式串word在s中的起始位置
#         len_s = len(s)
#         len_w = len(word)
#         for i in range(len_s - len_w + 1):
#             for j in range(len_w):
#                 if word[j] != s[i + j]:
#                     break
#             if j == (len_w - 1):
#                 return i, i + j
#
#     def wordBreak(self, s: str, wordDict) -> bool:
#         print(s)
#         if len(s) == 0:
#             return True
#
#         for word in wordDict:
#             if word in s:
#                 start_ix, end_ix = self.match(s, word)
#                 if self.wordBreak(s[:start_ix], wordDict) and self.wordBreak(s[end_ix+1:], wordDict):
#                     return True
#                 else:
#                     continue
#
#         return False

"""带备忘录的回溯"""
import functools
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        @functools.lru_cache()
        def backtrack(s):
            if len(s) == 0:
                return True
            res = False
            for i in range(1, len(s) + 1):
                if s[:i] in wordDict:
                    res = backtrack(s[i:]) or res

            return res

        return backtrack(s)

"""动态规划"""
# s = "catsandog"
# wordDict = ["cats", "dog", "sand", "and", "cat"]
s = "aaaaaaa"
wordDict = ["aaaa", "aaa"]

# s = "cbca"
# wordDict = ["bc", "ca"]

sl = Solution()
print(sl.wordBreak(s, wordDict))



