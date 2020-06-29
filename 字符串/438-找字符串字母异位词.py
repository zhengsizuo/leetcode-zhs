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