"""入度表，BFS，抽象为有向无环图的判断"""

# 拓扑排序的次数等于numCourses，则返回True
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites:
            return True

        from collections import deque
        queue = deque()  # 入度为0的节点入队
        indegrees = dict()  # 入度表
        adjacency = [[] for _ in range(numCourses)]  # 邻接表
        for k in range(numCourses):
            indegrees.setdefault(k, 0)

        for p in prerequisites:
            indegrees[p[1]] += 1
            adjacency[p[0]].append(p[1])

        for key, item in indegrees.items():
            if item == 0:
                queue.append(key)

        while queue:
            head = queue.popleft()
            numCourses -= 1
            # 与head邻接的点的入度均减1
            for node in adjacency[head]:
                indegrees[node] -= 1
                if indegrees[node] == 0:
                    queue.append(node)

        return not numCourses


"""深度优先"""


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indgrees = dict()  # 入度表
        directed_graph = dict()
        for i in range(numCourses):
            indgrees.setdefault(i, 0)
            directed_graph.setdefault(i, [])

        for edge in prerequisites:
            indgrees[edge[1]] += 1
            directed_graph[edge[0]].append(edge[1])

        def dfs(node, path=[]):
            if node in path:
                return False
            path.append(node)
            if not directed_graph[node]:
                ret_list.append(path[::-1])
                return

            for next_node in directed_graph[node]:
                # print(path)
                dfs(next_node, path)
                path.remove(next_node)  # 撤销选择

        for i in range(numCourses):
            if indgrees[i] == 0:
                dfs(i, [])