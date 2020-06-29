
class Solution:
    def reconstructQueue(self, people):
        res = [[] for _ in range(len(people))]
        if not people: return res

        people = sorted(people, key=lambda x: x[0])  # 先升序排序
        index = list(range(len(people)))
        memo = []
        for i in range(0, len(people)-1):
            rank = people[i][1]
            res[index[rank]] = people[i]

            if people[i + 1][0] == people[i][0]:
                # 记录相等的元素
                memo.append(index[rank])
            if people[i + 1][0] > people[i][0]:
                # 若下一个元素更大，则把index栈里面所有比i+1更小的元素删掉
                memo.append(index[rank])
                for m in memo:
                    index.remove(m)
                memo = []
                # print(res)

        rank = people[-1][1]
        res[index[rank]] = people[-1]
        return res

"""官方题解，贪心算法"""
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x: (-x[0], x[1]))
        output = []
        for p in people:
            output.insert(p[1], p)
        return output



heights = [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
#heights =[[2, 0], [1, 1]]
sl = Solution()
print(sl.reconstructQueue(heights))