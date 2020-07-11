
class Solution(object):
    
    # 定义左右上下四个行走方向
    directs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        m = len(board)
        if m == 0:
            return False
        n = len(board[0])
        mark = [[0 for _ in range(n)] for _ in range(m)]
                
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    # 将该元素标记为已使用
                    mark[i][j] = 1
                    if self.backtrack(i, j, mark, board, word[1:]):
                        return True
                    else:
                        # 回溯
                        mark[i][j] = 0
        return False
        
        
    def backtrack(self, i, j, mark, board, word):
        if len(word) == 0:
            return True
        
        for direct in self.directs:
            cur_i = i + direct[0]
            cur_j = j + direct[1]
            
            if cur_i >= 0 and cur_i < len(board) and cur_j >= 0 and cur_j < len(board[0]) and board[cur_i][cur_j] == word[0]:
                # 如果是已经使用过的元素，忽略
                if mark[cur_i][cur_j] == 1:
                    continue
                # 将该元素标记为已使用
                mark[cur_i][cur_j] = 1
                if self.backtrack(cur_i, cur_j, mark, board, word[1:]):
                    return True
                else:
                    # 回溯
                    mark[cur_i][cur_j] = 0
        return False


"""关键在于标记数组passed并且回溯"""
direct = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 上下左右


class Solution:
    def exist(self, board, word: str) -> bool:
        m = len(board)
        n = len(board[0])
        passed = [[False] * n for _ in range(m)]

        def search(board, word, i, j, passed):
            if not word:
                return True

            for d in direct:
                next_i = i + d[0]
                next_j = j + d[1]
                if 0 <= next_i < m and 0 <= next_j < n and board[next_i][next_j] == word[0]:
                    if passed[next_i][next_j]:
                        continue

                    passed[next_i][next_j] = True
                    if search(board, word[1:], next_i, next_j, passed):
                        return True
                    else:
                        passed[next_i][next_j] = False
            return False

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    passed[i][j] = True
                    # print(i, j)
                    if search(board, word[1:], i, j, passed):
                        return True
                    else:
                        passed[i][j] = False  # 撤销选择

        return False

board =[['A','B','C','E'], ['S','F','C','S'], ['A','D','E','E']]
# word = 'ABCCED'
word = 'SEE'
# word = 'ABCB'
# print(board[1][3]==word[0])

sl = Solution()
print(sl.exist(board, word))