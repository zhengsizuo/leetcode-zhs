
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


"""类似哈希表的方法"""
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs: return []
        anagrams = []
        res = []
        for s in strs:
            if sorted(s) in anagrams:
                idx = anagrams.index(sorted(s))
                res[idx].append(s)
            else:
                anagrams.append(sorted(s))
                res.append([s])

        return res

#strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
#strs = ["c", "c"]
strs = ["", ""]
sl = Solution()
print(sl.groupAnagrams(strs))
