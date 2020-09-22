class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1: return '1'

        str_list = ['1']
        for i in range(1, n):
            new_str = ''
            s = str_list[i - 1]
            count = 1
            for j in range(1, len(s)):
                if s[j] == s[j - 1]:
                    count += 1
                else:
                    new_str += str(count) + s[j - 1]
                    count = 1

            new_str += str(count) + s[-1]
            str_list.append(new_str)

        return str_list[-1]


n = 4
sl = Solution()
print(sl.countAndSay(n))