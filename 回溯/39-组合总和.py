class Solution:
    def combinationSum(self, candidates, target):
        if not candidates:
            return []

        candidates.sort()
        ret = list()

        def backtrack(candidates, target, path):
            # 结束条件
            if target < 0:
                return
            if target == 0:
                # print(path)
                path.sort()
                if path not in ret:
                    ret.append(path.copy())
                return

            for i in range(len(candidates)):
                item = candidates[i]
                if (target-item) < 0:
                    break
                # 每次递归的时候只在candidates中当前及之后的数字中选择，这一步需要理解
                backtrack(candidates[i:], target - item, path+[item])

        backtrack(candidates, target, [])

        return ret

candidates = [2, 3, 6, 7]
target = 7
sl = Solution()

result = sl.combinationSum(candidates, target)
print(result)