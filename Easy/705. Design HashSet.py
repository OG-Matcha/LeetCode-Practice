# easy

'''
Design a HashSet without using any built-in hash table libraries.

Implement MyHashSet class:

void add(key) Inserts the value key into the HashSet.
bool contains(key) Returns whether the value key exists in the HashSet or not.
void remove(key) Removes the value key in the HashSet. If key does not exist in the HashSet, do nothing.
'''

# https://leetcode.com/problems/design-hashset/description/


class MyHashSet:

    def __init__(self):
        self.size = 10000
        self.table = [None] * self.size

    def hashing_func(self, key: int) -> int:
        return key % self.size

    def add(self, key: int) -> None:
        hv = self.hashing_func(key)

        if not self.table[hv]:
            self.table[hv] = [key]
        else:
            self.table[hv].append(key)

    def remove(self, key: int) -> None:
        hv = self.hashing_func(key)

        if self.table[hv]:
            while key in self.table[hv]:
                self.table[hv].remove(key)

    def contains(self, key: int) -> bool:
        hv = self.hashing_func(key)

        if self.table[hv]:
            return any(num == key for num in self.table[hv])
        return False

# Time complexity = O(n)
# Space complexity = O(n)


class MyHashSet:

    def __init__(self):
        self.hash = [False] * 1000001

    def add(self, key: int) -> None:
        self.hash[key] = True

    def remove(self, key: int) -> None:
        self.hash[key] = False

    def contains(self, key: int) -> bool:
        return self.hash[key]

# Time complexity = O(1)
# Space complexity = O(n)

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
