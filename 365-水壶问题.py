class Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:

        def dfs(state, pre_a, path):
            print(state)
            path.append(state[:])
            if sum(state) == z or z in state:
                return True

            # 做选择
            for i in range(6):
                s = state.copy()
                if i == pre_a: continue
                if state == [x, y] and (i==0 or i==1):
                    # 如果两个水壶都满了，不必再装
                    continue
                if i == 0:
                    state[0] = x  # 装满1水壶
                    if state not in path:
                        dfs(state, i, path)
                        state = s
                if i == 1:
                    state[1] = y  # 装满2水壶
                    if state not in path:
                        dfs(state, i, path)
                        state = s
                if i == 2:
                    state[0] = 0  # 倒掉1水壶
                    if state not in path:
                        dfs(state, i, path)
                        state = s
                if i == 3:
                    state[1] = 0  # 倒掉2水壶
                    if state not in path:
                        dfs(state, i, path)
                        state = s
                if i == 4:
                    # 1倒向2
                    cur_sum = state[1] + state[0]
                    if cur_sum > y:
                        state[1] = y
                        state[0] = cur_sum - y
                    else:
                        state[1] = cur_sum
                        state[0] = 0
                    if state not in path:
                        dfs(state, i, path)
                        state = s
                if i == 5:
                    # 2倒向1
                    cur_sum = state[0] + state[1]
                    if cur_sum > x:
                        state[0] = x
                        state[1] = cur_sum - x
                    else:
                        state[0] = cur_sum
                        state[1] = 0
                    if state not in path:
                        dfs(state, i, path)
                        state = s

        state = [3, 0]
        return dfs(state, 0, [])

sl = Solution()
x, y, z = 3, 5, 4
print(sl.canMeasureWater(x, y, z))