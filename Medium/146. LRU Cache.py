# medium

'''
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
The functions get and put must each run in O(1) average time complexity.
'''

# https://leetcode.com/problems/lru-cache/description/

import collections


class LRUCache:

    def __init__(self, capacity: int):
        self.data = collections.OrderedDict()
        self.cap = capacity

    def get(self, key: int) -> int:
        if key in self.data:
            self.data.move_to_end(key)
            return self.data[key]

        return -1

    def put(self, key: int, value: int) -> None:
        self.data[key] = value
        self.data.move_to_end(key)

        if len(self.data) > self.cap:
            self.data.popitem(False)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

# Time complexity = O(1)
# Time complexity = O(n) where n is the maximum number of unique key calls by put()
