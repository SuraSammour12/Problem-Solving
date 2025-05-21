# 146. LRU Cache
# https://leetcode.com/problems/lru-cache/

# import the OrderDict => it maintains the input order, (type of dictionary)
from collections import OrderedDict

class LRUCache(object):

    def __init__(self, capacity):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key):
        if key in self.cache:
            value = self.cache.pop(key)
            self.cache[key] = value
            return value
        return -1

    def put(self, key, value):
        if key in self.cache:
            self.cache.pop(key)
        elif len(self.cache) >= self.capacity:
            self.cache.popitem(last=False)
        self.cache[key] = value


