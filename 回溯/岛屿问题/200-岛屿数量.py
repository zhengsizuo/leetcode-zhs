class Solution:
    directs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def numIslands(self, grid):
        ret = 0
        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])
        marked = [[0 for _ in range(n)] for _ in range(m)]

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                # 遇到陆地且没被访问过
                if grid[i][j] == '1' and marked[i][j] == 0:
                    marked[i][j] = 1
                    self.search(grid, i, j, marked)
                    ret += 1

        return ret

    def search(self, grid, i, j, marked):
        count = 0  # 标志是否有新的陆地‘1’被标记
        for direct in self.directs:
            cur_i = i + direct[0]
            cur_j = j + direct[1]
            if cur_i >= 0 and cur_i < len(grid) and cur_j >= 0 and cur_j < len(grid[0]) and grid[cur_i][cur_j] == '1':
                if marked[cur_i][cur_j] == 1:
                    continue
                marked[cur_i][cur_j] = 1
                count += 1
                self.search(grid, cur_i, cur_j, marked)

        # 如果该陆地周围都被搜索过，递归结束
        if count == 0:
            return


"""精简版，去掉marked数组"""

class Solution:
    directs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def numIslands(self, grid: List[List[str]]) -> int:
        ret = 0
        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                # 遇到陆地且没被访问过
                if grid[i][j] == '1':
                    ret += 1
                    self.search(grid, i, j)

        return ret

    def search(self, grid, i, j):
        for direct in self.directs:
            cur_i = i + direct[0]
            cur_j = j + direct[1]
            if cur_i >= 0 and cur_i < len(grid) and cur_j >= 0 and cur_j < len(grid[0]) and grid[cur_i][cur_j] == '1':
                grid[cur_i][cur_j] = '0'
                self.search(grid, cur_i, cur_j)