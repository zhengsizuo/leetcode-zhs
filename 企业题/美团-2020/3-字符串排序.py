def Solution(s):
    s_list = s.split(',')
    def compare(str1, str2):
        # 比较str1是否在str2前面
        # str2为空串或者是str1的前缀，都应该排前面
        if str1 in str2: return True

        if str2 == '': return False
        if str2 in str1: return False

        n = len(str1) if len(str1)<len(str2) else len(str2)
        for i in range(n):
            if str1[i] < str2[i]:
                return False
            elif str1[i] > str2[i]:
                return True

        # return False

    def quick_sort(s_list):
        # print(s_list)
        if len(s_list) < 2:
            return s_list

        pivot = s_list[0]
        # print(pivot, s_list)
        forehead = [s for s in s_list[1:] if compare(s, pivot)]
        behind = [s for s in s_list[1:] if not compare(s, pivot)]
        return quick_sort(forehead) + [pivot] + quick_sort(behind)

    str_list = quick_sort(s_list)
    # print(str_list)
    return ','.join(str_list)



s = 'waimai,dache,lvyou,liren,,meishi,jiehun,lvyoujingdian,jiaopei,menpiao,jiudian'
s = input()
print(Solution(s))