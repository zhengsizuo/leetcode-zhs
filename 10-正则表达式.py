class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if s is None and p is not None:
            return False
        if p is None:
            return True
        
        if '*' not in p:
            if len(p) != len(s):
                return False
            else:
                for i in range(len(p)):
                    if p[i] == s[i] or p[i] == '.':
                        continue
                    else:
                        return False
                return True
            
        else:
            N, M = len(p), len(s)
            if N>=M:
                for i in range(0, N-m+1):
                    for j in range(0, M):
                        if p[i+j] == '.' or p[i+j] == s[j]:
                            continue
                        if j>0:
                            if (p[i]=='*') and (p[i+j-1]==s[j-1] or p[i+j-1]=='.'):
                                continue
                        else:
                            break
                    if j==M-1:
                        return True
                return False