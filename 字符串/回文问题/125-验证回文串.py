class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s or len(s)==1: return True
        left = 0
        right = len(s) - 1
        valid_char = list(range(ord('a'), ord('z') + 1)) + list(range(ord('A'), ord('Z') + 1))
        valid_ascii = valid_char + list(range(ord('0'), ord('9') + 1))
        while left < right:
            while left<len(s) and ord(s[left]) not in valid_ascii:
                left += 1
            while right>=0 and ord(s[right]) not in valid_ascii:
                right -= 1

            if left<len(s) and right>=0:
                if s[left].lower() == s[right].lower():
                    left += 1
                    right -= 1
                else:
                    return False

        return True

"""可以使用isalnum函数判断方法检测字符串是否由字母和数字组成。"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        sgood = "".join(ch.lower() for ch in s if ch.isalnum())
        n = len(sgood)
        left, right = 0, n - 1

        while left < right:
            if sgood[left] != sgood[right]:
                return False
            left, right = left + 1, right - 1
        return True





s = "A man, a plan, a canal: Panama"
sl = Solution()
print(sl.isPalindrome(s))