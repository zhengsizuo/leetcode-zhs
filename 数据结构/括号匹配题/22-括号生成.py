class Solution:
    def generateParenthesis(self, n: int):
        if n == 0:
            return []

        result = []
        brackets_dict = {"(": 1, ")": -1}

        def backtrack(path_s="(", list_p=["(", ")"], match_flag=1):
            if len(path_s) == (2*n):
                result.append(path_s[:])
                return

            for p in list_p:
                # 剪枝，当左括号全部匹配，下一个不能选右括号
                if match_flag == 0 and p==")":
                    continue
                # 当左括号全部用完，不能选左括号
                if path_s.count("(") == n and p=="(":
                    continue
                path_s += p  # 做选择
                match_flag += brackets_dict[p]  # 保存匹配状态，若为0则左括号匹配完
                backtrack(path_s, list_p, match_flag)
                match_flag -= brackets_dict[p]
                path_s = path_s[:-1]  # 撤销选择

        backtrack()
        return result

sl = Solution()
print(sl.generateParenthesis(n=3))