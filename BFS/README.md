# BFS套路框架 
* 先用字典建图，再建立队列和visited集合开始访问
```python
graph = {}
visted = set()
def BFS(start, target):
    queue = [start]
    visted.add(start)
    step = 0  # 记录扩散的步数
    while queue:
        sz = len(queue)
        for i in range(sz):
            head = queue.pop(0)
            if head == target:
                return step 
                
            for node in graph[head]:
                if node not in visted:
                    queue.append(node)
                    visted.add(node)
         step += 1

```