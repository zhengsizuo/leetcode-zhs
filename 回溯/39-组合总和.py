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

"""自己写的，效率低一些"""
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()

        def backtrack(path, cur_sum):
            if cur_sum == target:
                path.sort()
                # 排序之后去重
                if path not in result:
                    result.append(path.copy())
                return

            for i in range(len(candidates)):
                if cur_sum + candidates[i] > target:
                    # 因为排过序，所以可以不继续往后面做选择了，直接break而不是continue
                    break
                cur_sum += candidates[i]
                path.append(candidates[i])
                backtrack(path, cur_sum)
                path.remove(candidates[i])
                cur_sum -= candidates[i]

        backtrack(path=[], cur_sum=0)
        return result
candidates = [2, 3, 6, 7]
target = 7
sl = Solution()

result = sl.combinationSum(candidates, target)
print(result)