# 需要用Python3执行
from collections import OrderedDict
class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self._capacity = capacity
        self.cache = OrderedDict()


    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.cache:
            self.cache.move_to_end(key)
            return self.cache[key]
        else:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache.setdefault(key, value)
        if len(self.cache) > self._capacity:
            self.cache.popitem(last=False)

"""不使用高级API"""
class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self._capacity = capacity
        self.cache = list()


    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        val = -1
        for i, item in enumerate(self.cache):
            if key == item[0]:
                val = self.cache.pop(i)[1]
                break

        self.cache.append([key, val])
        return val

    def traverse(self, key):
        """遍历cache，是否已有key"""
        for i, item in enumerate(self.cache):
            # 如果密钥已经存在
            if key == item[0]:
                return True, i

        return False, -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        flag, index = self.traverse(key)
        if flag:
            self.cache.pop(index)
        self.cache.append([key, value])
        if len(self.cache) > self._capacity:
            self.cache.pop(0)


# Your LRUCache object will be instantiated and called as such:
obj = LRUCache(2)
obj.put(2, 1)
obj.put(2, 2)
print(obj.get(2))
obj.put(1, 1)
# print(obj.get(2))
obj.put(4, 1)
print(obj.get(2))
# print(obj.get(3))
# print(obj.get(4))
