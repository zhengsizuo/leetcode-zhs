"""BFS，效率更高，更清晰，注意维护入度表！"""
class Solution:
    def findOrder(self, numCourses: int, prerequisites):
        indgrees = dict()  # 入度表
        directed_graph = dict()
        for i in range(numCourses):
            indgrees.setdefault(i, 0)
            directed_graph.setdefault(i, [])

        for edge in prerequisites:
            indgrees[edge[1]] += 1
            directed_graph[edge[0]].append(edge[1])

        queue = []
        for k, v in indgrees.items():
            if v == 0:
                queue.append(k)

        res = []
        while queue:
            front = queue.pop(0)
            res.insert(0, front)
            for next_node in directed_graph[front]:
                indgrees[next_node] -= 1
                if indgrees[next_node] == 0:
                    queue.append(next_node)

        if len(res) == numCourses:
            return res
        else:
            return []


"""DFS，需要染色，0=未搜索，1=搜索中，2=已完成"""
n = 4
pre = [[1,0],[2,0],[3,1],[3,2]]
# n = 3
# pre = [[0, 2], [2, 0], [1, 2]]
sl = Solution()
print(sl.findOrder(n, pre))