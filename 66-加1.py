class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if not digits: return []

        if digits[-1] < 9:
            digits[-1] += 1
            return digits

        elif digits.count(9) == len(digits):
            return [1] + [0] * len(digits)
        else:
            # digits[-1] = 0
            return self.plusOne(digits[:-1]) + [0]