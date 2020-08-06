class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs: return ''

        min_str = strs[0]
        for s in strs:
            if len(s) < len(min_str):
                min_str = s

        for i in range(len(min_str)):
            for s in strs:
                if s[i] != min_str[i]:
                    return min_str[:i]

        return min_str