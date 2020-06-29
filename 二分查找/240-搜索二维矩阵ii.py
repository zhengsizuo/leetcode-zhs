"""从左下角开始搜索"""
class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False

        col = 0
        row = len(matrix) - 1

        while col < len(matrix[0]) and row >= 0:
            if target == matrix[row][col]:
                return True
            if target > matrix[row][col]:
                col += 1
            elif target < matrix[row][col]:
                row -= 1

        return False



"""尝试对每一行二分查找"""
class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False

        row = 0
        while row < len(matrix):
            if target > matrix[row][-1]:
                row += 1
            elif target < matrix[row][0]:
                return False

            else:
                search_arr = matrix[row]
                left = 0
                right = len(search_arr)-1
                mid = left + (right - left) // 2
                while left <= right:
                    if target == search_arr[mid]:
                        return True
                    elif target < search_arr[mid]:
                        right = mid - 1
                    elif target > search_arr[mid]:
                        left = mid + 1

                row += 1

        return False