'''
This problem was asked by Google.

Implement an LRU (Least Recently Used) cache.
It should be able to be initialized with a cache size n, and contain the
following methods:

-- set(key, value): sets key to value.
   If there are already n items in the cache and we are adding a new item,
   then it should also remove the least recently used item.
-- get(key): gets the value at key. If no such key exists, return null.

Each operation should run in O(1) time.
'''

from collections import deque


class LRU_Cache:
    def __init__(self, n):
        self.max_size = n
        self.cache = {}
        self.queue = deque()

    def set(self, key, value):
        self.queue.append(key)
        self.cache[key] = value
        if len(self.cache) > self.max_size:
            del self.cache[self.queue.popleft()]

    def get(self, key):
        if key not in self.cache:
            return None
        else:
            return self.cache[key]
