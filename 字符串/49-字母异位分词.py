# """暴力法，超出时间限制"""
# class Solution:
#     def groupAnagrams(self, strs):
#         if not strs:
#             return []
#
#         result = []
#         def backtrack(ret_item, path_s="", list_s="eat"):
#             if len(list_s) == 0:
#                 for s in strs[:]:
#                     if path_s[:] == s:
#                         ret_item.append(path_s[:])
#                         strs.remove(path_s)
#                 return
#             # 回溯法搜索可能的异位分词
#             for i, s in enumerate(list_s):
#                 path_s += s
#                 backtrack(ret_item, path_s, list_s[:i]+list_s[i+1:])
#                 path_s = path_s[:-1]
#
#         def search(ret_item=[], strs=strs):
#             if len(strs) == 0:
#                 return
#
#             backtrack(ret_item, list_s=strs[0])
#             result.append(ret_item[:])
#             search(ret_item=[], strs=strs)
#
#         search()
#         return result

"""用26位元组对字符进行计数编码，做键"""
import collections
class Solution:
    def groupAnagrams(self, strs):
        ans = collections.defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            ans[tuple(count)].append(s)

        return list(ans.values())

"""以排序字符串元组做key"""
class Solution(object):
    def groupAnagrams(self, strs):
        ans = collections.defaultdict(list)
        for s in strs:
            ans[tuple(sorted(s))].append(s)
        return list(ans.values())


#strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
#strs = ["c", "c"]
strs = ["", ""]
sl = Solution()
print(sl.groupAnagrams(strs))
