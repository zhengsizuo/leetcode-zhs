"""基于桶画图"""


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_dicts = dict()
        for s in tasks:
            task_dicts.setdefault(s, 0)
            task_dicts[s] += 1

        task_dicts = sorted(task_dicts.items(), key=lambda x: x[1], reverse=True)  # 按值降序排序
        res = 0

        max_count = task_dicts[0][1]
        res += (max_count - 1) * (n + 1)
        for task in task_dicts:
            if task[1] == max_count:
                res += 1

        # 处理特殊情况
        if res < len(tasks):
            res = len(tasks)
        return res