# 二叉树套路框架
## 递归型
```python
def traverse(root):
    traverse(root.left)
    traverse(root.right)

```
递归左右子树，明确函数返回值含义的情况下丰富框架（递归结束条件等）