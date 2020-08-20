class Solution:
    def partition(self, s: str):
        def is_valid(s):
            return s == s[::-1]
            # left = 0
            # right = len(s) - 1
            # while left <= right:
            #     if s[left] == s[right]:
            #         left += 1
            #         right -= 1
            #     else:
            #         return False
            #
            # return True

        ret = []
        def backtrack(s, path):
            print(s, path)
            if not s:
                if path not in ret:
                    ret.append(path.copy())
                return

            for j in range(len(s)):
                if is_valid(s[:j+1]):
                    backtrack(s[j+1:], path + [s[:j+1]])

        backtrack(s, [])
        return ret


s = 'acaaa'
s = 'aab'
sl = Solution()
print(sl.partition(s))
