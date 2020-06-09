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