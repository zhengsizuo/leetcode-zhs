directs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

"""DFS清晰简单：把与边缘O相连的O标记出来"""
class Solution:
    def solve(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return

        m = len(board)
        n = len(board[0])

        def dfs(i, j):
            board[i][j] = 'M'
            for d in directs:
                next_i = i + d[0]
                next_j = j + d[1]
                if 0 <= next_i < m and 0 <= next_j < n and board[next_i][next_j] == 'O':
                    dfs(next_i, next_j)

        for i in range(m):
            if board[i][0] == 'O':
                dfs(i, 0)
            if board[i][-1] == 'O':
                dfs(i, n - 1)

        for j in range(n):
            if board[0][j] == 'O':
                dfs(0, j)
            if board[m - 1][j] == 'O':
                dfs(m - 1, j)

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == 'M':
                    board[i][j] = 'O'

board = [["O","X","X","O","X"],["X","O","O","X","O"],["X","O","X","O","X"],["O","X","O","O","O"],["X","X","O","X","O"]]
sl = Solution()
sl.solve(board)
for b in board:
    print(b)