class Solution:
    def canCompleteCircuit(self, gas, cost) -> int:
        n = len(gas)  # n个加油站
        for i in range(n):
            if gas[i] >= cost[i]:
                # 尝试从i出发
                idx = i
                cur_gas = 0
                count = 0
                while count < n:
                    cur_gas += gas[idx] - cost[idx]
                    if cur_gas < 0: break
                    idx = idx + 1 if idx < n - 1 else 0  # 到下一个加油站
                    count += 1

                if count == len(gas):
                    return i

        return -1