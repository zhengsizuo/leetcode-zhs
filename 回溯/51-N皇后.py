class Solution:
    def solveNQueens(self, n: int):
        result = []

        def backtrack(path):
            # path用来记录每一行合理的列
            # print(path)
            if len(path) == n:
                result.append(path.copy())
                return

            for j in range(n):
                # 剪枝
                if j in path: continue
                cut = False  # 是否剪枝的标志
                for i in range(len(path)):
                    if abs(len(path)-i) == abs(j-path[i]):
                        cut = True
                        break

                if not cut:
                    path.append(j)
                    backtrack(path)
                    path.remove(j)

        backtrack(path=[])
        print(result)
        grid = [['.'] * n for _ in range(n)]
        res = [[] for _ in range(len(result))]
        for k, r in enumerate(result):
            for i, j in enumerate(r):
                grid[i][j] = 'Q'
                res[k].append(''.join(grid[i]))
            grid = [['.'] * n for _ in range(n)]


        return res


sl = Solution()
print(sl.solveNQueens(6))