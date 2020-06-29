
class Solution:
    def decodeString(self, s: str) -> str:
        res = ''
        i = 0
        while i < len(s):
            if s[i] != '[':
                res += s[i]
                i += 1
                print(s)
            else:
                res = res.replace(s[i-1], '')  # 去除数字
                stack_num = [int(s[i-1])]
                stack_index = [i]  # 存储中括号的索引
                bracket_index = []
                # decode_str = ''
                while stack_index:
                    i += 1
                    print(i)
                    if s[i] == '[':
                        stack_num.append(int(s[i-1]))
                        stack_index.append(i)
                    elif s[i] == ']':
                        bracket_index.append([stack_index.pop(), i])

                stack_num.reverse()
                print(stack_num)
                print(bracket_index)
                begin_i = bracket_index[0][0]
                end_i = bracket_index[0][1]
                decode_str = stack_num[0] * s[begin_i+1:end_i]
                print(decode_str)

                for j in range(1, len(bracket_index)):
                    begin_i = bracket_index[j][0]
                    end_i = bracket_index[j][1]

                    s_resdual = s[begin_i+1:bracket_index[j-1][0]-1] + s[bracket_index[j-1][1]+1:end_i]
                    decode_str = stack_num[j] * (s_resdual+decode_str)

                res += decode_str
                i += 1

        return res

"""辅助栈"""
class Solution:
    def decodeString(self, s: str) -> str:
        stack, res, multi = [], "", 0
        for c in s:
            if c == '[':
                stack.append([multi, res])
                res, multi = "", 0
            elif c == ']':
                cur_multi, last_res = stack.pop()
                res = last_res + cur_multi * res
            elif '0' <= c <= '9':
                multi = multi * 10 + int(c)
            else:
                res += c
        return res


"""递归法"""

# s = 'ef3[a2[c]]'
s = '3[a]2[bc]'

sl = Solution()
print(sl.decodeString(s))