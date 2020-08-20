"""原来暴力BFS就可以"""
class Solution:
    def openLock(self, deadends, target: str) -> int:
        if '0000' in deadends:
            return -1
        def generate_candidates(num_str):
            # 从一串数字生成下一个候选集
            num_l = list(num_str)
            num_list = num_l.copy()
            candidates = []
            for i in range(len(num_list)):
                if num_list[i] == '0':
                    for c in ['1', '9']:
                        new_item = ''.join(num_list[:i] + [c] + num_list[i+1:])
                        if new_item in visited or new_item in deadends:
                            continue
                        candidates.append(new_item)
                elif num_list[i] == '9':
                    for c in ['0', '8']:
                        new_item = ''.join(num_list[:i] + [c] + num_list[i+1:])
                        if new_item in visited or new_item in deadends:
                            continue
                        candidates.append(new_item)
                else:
                    n_ascii = ord(num_list[i])
                    choices = [chr(n_ascii+1), chr(n_ascii-1)]
                    for c in choices:
                        new_item = ''.join(num_list[:i] + [c] + num_list[i + 1:])
                        if new_item in visited or new_item in deadends:
                            continue
                        candidates.append(new_item)

            return candidates


        queue = ['0000']
        visited = set()
        visited.add('0000')
        step = 0
        while queue:
            sz = len(queue)
            for i in range(sz):
                head = queue.pop(0)
                if head == target:
                    return step

                for c in generate_candidates(head):
                    queue.append(c)
                    visited.add(c)

            step += 1

        return -1


deadends = ["0201", "0101", "0102", "1212", "2002"]
target = "0202"
deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"]
target = "0009"

sl = Solution()
print(sl.openLock(deadends, target))



