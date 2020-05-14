import sys

s = 'ADDBECODEBANC'
t = 'ABC'

def insert_key(str_key, dictionary):
    if str_key in dictionary:
        dictionary[str_key] += 1
    else:
        dictionary[str_key] = 1


def minWindow(s, t):
    """
    :type s: str
    :type t: str
    :rtype: str
    """
    res = str()
    start = 0  # 记录所返回字符开始位置
    minLen = sys.maxsize  # 记录所返回字符的长度
    left, right = 0, 0  # 左右指针
    window, need = dict(), dict()
    # 由子串t初始化need
    for s_t in t:
        insert_key(s_t, need)

    match = 0  # 统计窗口window和need中字符的匹配数

    while (right < len(s)):
        c1 = s[right]
        if c1 in need:
            insert_key(c1, window)
            if window[c1] == need[c1]:
                match += 1
        right += 1
        # 当window符合要求时，移动左指针
        while (match == (len(need))):
            if (right - left) < minLen:
                minLen = right - left
                start = left

            c2 = s[left]
            if c2 in need:
                if c2 in window:
                    window[c2] -= 1
                if window[c2] < need[c2]:
                    match -= 1
            left += 1

    print('start:', start)
    print("match:", match)
    if minLen == sys.maxsize:
        return ""
    else:
        return s[start:start + minLen]

print(minWindow(s, t))