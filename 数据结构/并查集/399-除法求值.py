"""有向图+DFS"""
class Solution:
    def calcEquation(self, equations, values, queries):
        # 建立有向图
        hash_set = dict()
        for i, equa in enumerate(equations):
            hash_set.setdefault(equa[0], {})
            hash_set.setdefault(equa[1], {})

            hash_set[equa[0]].setdefault(equa[1], values[i])
            hash_set[equa[1]].setdefault(equa[0], 1 / values[i])

        def dfs(q_start, q_end):
            if q_start not in hash_set or q_end not in hash_set:
                return -1.0
            if q_start == q_end:
                return 1.0

            print(visited)
            s_dict = hash_set.get(q_start, {})
            if q_end in s_dict.keys():
                return s_dict[q_end]
            for key, value in s_dict.items():
                if key not in visited:
                    visited.add(key)
                    next_v = dfs(key, q_end)
                    if next_v != -1.0:
                        return value * next_v

            return -1.0

        ret = []
        for q in queries:
            visited = set()
            ret.append(dfs(q[0], q[1]))

        return ret


"""更普遍的解法：并查集Union-Find"""