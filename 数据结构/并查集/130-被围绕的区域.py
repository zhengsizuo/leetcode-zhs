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


"""并查集的方法，将边界上的O与虚拟哑结点相连"""
class Solution:
    directs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    def solve(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        m = len(board)
        n = len(board[0])
        parent = {x: x for x in range(m * n + 1)}  # 初始化并查集树，键表示节点，键值表示根节点
        directs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def find(x):
            # 使用路径压缩法可以通过
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return parent[x]

        def union(p, q):
            root_p = find(p)
            root_q = find(q)
            parent[root_p] = root_q

        dummy = m * n  # 虚拟节点作为根
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    if i==0 or i==m-1 or j==0 or j==n-1:
                        union(i*n+j, dummy)
                    else:
                        # 把不在边缘的‘O’的上下左右区域连起来
                        for x, y in directs:
                            if board[i + x][j + y] == "O":
                                union(i * n + j, (i + x) * n + (j + y))

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    if find(i*n+j) == find(dummy):
                        continue
                    else:
                        board[i][j] = 'X'



board = [["X","O","X","X"],["O","X","O","X"],["X","O","X","O"],["O","X","O","X"],["X","O","X","O"],["O","X","O","X"]]
sl = Solution()
sl.solve(board)
for b in board:
    print(b)