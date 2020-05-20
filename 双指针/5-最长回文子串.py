"""暴力法"""
class Solution(object):
    def isPalindrome(self, s):
        # 判断某字符串片段是否为回文字符串，返回bool
        n = len(s)
        for i in range(n/2):
            if s[i]!=s[n-i-1]:
                return False
        
        return True
    
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s)==0 or len(s)==1:
            return s

        ret_s = str()
        maxLen = 0
        # 枚举所有子串，保存最长的回文串
        for i in range(len(s)-1):
            for j in range(i, len(s)):
                if self.isPalindrome(s[i:j]) and (j-i)>maxLen:
                    maxLen = j-i
                    ret_s = s[i:j]
                if j==(len(s)-1):
                    if self.isPalindrome(s[i:]) and (j-i+1)>maxLen:
                        maxLen = j-i+1
                        ret_s = s[i:]

        return ret_s

"""双指针中心扩展法"""
class Solution(object):
    def expandPalindrome(self, s, l, r):
        # 以l和r为中心扩展字符串寻找回文串
        while(l>=0 and r<len(s) and s[l]==s[r]):
            l -= 1
            r += 1

        return s[l+1:r] 
    
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s)==0 or len(s)==1:
            return s
        
        res = str()
        for i in range(len(s)):
            s1 = self.expandPalindrome(s, i, i)
            s2 = self.expandPalindrome(s, i, i+1)

            print("The {}th iteration, s1: {}, s2: {}".format(i, s1, s2))
            res = res if len(res)>len(s1) else s1
            res = res if len(res)>len(s2) else s2
        
        return res

input_str = 'babad'
sl = Solution()
sl.longestPalindrome(input_str)