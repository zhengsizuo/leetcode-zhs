#
# 实现方案
# @param m int整型 最少m个键
# @param n int整型 最多n个键
# @return int整型
#
"""通过40%的用例"""
class Solution:
    def solution(self , m , n ):
        # write code here
        index2pos = {0: (0, 0), 1: (0, 1), 2: (0, 2), 3: (1, 0), 4: (1, 1), 5: (1, 2), 6: (2, 0), 7: (2, 1), 8: (2, 2)}
        directed_edges = dict()
        for key, item in index2pos.items():
            directed_edges.setdefault(key, [])
            for i in range(9):
                if i == key:
                    continue
                next_pos = index2pos[i]
                if item[0] == next_pos[0] and abs(item[1] - next_pos[1]) == 2:
                    continue
                if item[1] == next_pos[1] and abs(item[0] - next_pos[0]) == 2:
                    continue
                # 对角线情况
                if abs(item[0] - next_pos[0]) == 2 and abs(item[1] - next_pos[1]) == 2:
                    continue
                # 符合条件的有向边，加入
                directed_edges[key].append([key, i])

        def dfs(s, path, n):
            """n: 键的数目"""
            # print(path)
            nonlocal count
            if len(path) == n:
                count += 1
                return
            for e in directed_edges[s]:
                # print(e)
                if e[1] in path:
                    continue
                path.append(e[1])
                dfs(e[1], path, n)
                path.remove(e[1])

        total_count = 0
        if m==1:
            total_count = 9
            for i in range(2, n+1):
                for s in range(9):
                    count = 0
                    dfs(s, path=[s], n=i)
                    print(count)
                    total_count += count
        else:
            for i in range(m, n+1):
                for s in range(9):
                    count = 0
                    dfs(s, path=[s], n=i)
                    total_count += count

        return total_count



sl = Solution()
print(sl.solution(m=3, n=3))

# 正确答案应为320

# index2pos = dict()


"""帖子里面的一个答案"""
# Python3 dfs
# 所有方向
di = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1), (1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1),
      (2, -1), (-2, 1), (-2, -1)]
# 可跨一个点的方向
ds = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
# 9个点
nodes = {(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)}


def dfs(x, y, visited, count):
    visited.add((x, y))
    count -= 1
    ans = 0
    if count == 0:
        ans += 1
    else:
        for d in di:
            if (x + d[0], y + d[1]) in visited or (x + d[0], y + d[1]) not in nodes:
                if d not in ds:
                    continue
                else:
                    dx = d[0] * 2
                    dy = d[1] * 2
                    if (x + dx, y + dy) in nodes and (x + dx, y + dy) not in visited:
                        ans += dfs(x + dx, y + dy, visited, count)
            else:
                ans += dfs(x + d[0], y + d[1], visited, count)
    visited.remove((x, y))
    return ans


ans = [0] * 10
for count in range(1, 10):
    for i in range(3):
        for j in range(3):
            visited = set()
            ans[count] += dfs(i, j, visited, count)
# ans[i]即为i个键的结果数
# ans = [0, 9, 56, 320, 1624, 7152, 26016, 72912, 140704, 140704]
print(ans)
