class Solution:
    def romanToInt(self, s: str) -> int:
        roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        special_case = {'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}

        res = 0
        i = 0
        while i < len(s):
            res += roman_dict[s[i]]
            enter_special = False
            if s[i] in ['I', 'X', 'C'] and i + 1 < len(s):
                if s[i:i + 2] in special_case:
                    enter_special = True
                    res -= roman_dict[s[i]]
                    res += special_case[s[i:i + 2]]
                    i += 2
            if not enter_special:
                i += 1

        return res