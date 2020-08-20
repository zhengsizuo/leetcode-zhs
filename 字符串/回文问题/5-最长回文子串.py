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


"""动态规划法"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s: return ''

        dp = [[False] * len(s) for _ in range(len(s))]
        # 初始化base case，对角线即单个字符的时候为True
        for i in range(len(s)):
            dp[i][i] = True

        for i in range(len(s)-1, -1, -1):
            for j in range(i + 1, len(s)):
                if s[i] == s[j]:
                    if j - i == 1:
                        # 特殊情况
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i + 1][j - 1]

        max_len = 0
        pos =[0, 0]
        for i in range(len(dp)):
            for j in range(i, len(dp[0])):
                if dp[i][j]:
                    if j-i > max_len:
                        max_len = j-i
                        pos[0], pos[1] = i, j

        return s[pos[0]:pos[1]+1]


input_str = 'babad'
input_str = 'ccc'
sl = Solution()
print(sl.longestPalindrome(input_str))