"""暴力法，居然通过了"""
class Solution:
    def isValidSudoku(self, board) -> bool:

        def search_sub(m, n):
            path = []
            for i in range(3):
                for j in range(3):
                    element = board[m + i][n + j]
                    if element != '.':
                        if element in path: return False
                        path.append(element)

            return True


        # 搜索3x3子方格模块
        for m in range(0, 9, 3):
            for n in range(0, 9, 3):
                if not search_sub(m, n):
                    return False
        # 搜索行
        for i in range(9):
            path = []
            for b in board[i]:
                if b != '.':
                    if b in path: return False
                    path.append(b)
        # 搜索列
        for j in range(9):
            path = []
            for i in range(9):
                element = board[i][j]
                if element != '.':
                    if element in path: return False
                    path.append(element)

        return True


"""官方题解用哈希表存储，一次遍历"""

board = [[".",".",".",".","5",".",".","1","."],[".","4",".","3",".",".",".",".","."],[".",".",".",".",".","3",".",".","1"],["8",".",".",".",".",".",".","2","."],[".",".","2",".","7",".",".",".","."],[".","1","5",".",".",".",".",".","."],[".",".",".",".",".","2",".",".","."],[".","2",".","9",".",".",".",".","."],[".",".","4",".",".",".",".",".","."]]
for b in board:
    print(b)
sl = Solution()
print(sl.isValidSudoku(board))