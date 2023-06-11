# medium

'''
Implement a SnapshotArray that supports the following interface:

SnapshotArray(int length) initializes an array-like data structure with the given length. Initially, each element equals 0.
void set(index, val) sets the element at the given index to be equal to val.
int snap() takes a snapshot of the array and returns the snap_id: the total number of times we called snap() minus 1.
int get(index, snap_id) returns the value at the given index, at the time we took the snapshot with the given snap_id
'''

# https://leetcode.com/problems/snapshot-array/description/


class SnapshotArray:

    def __init__(self, length: int):
        self.data = [[[0, 0]] for _ in range(length)]
        self.id = 0

    def set(self, index: int, val: int) -> None:
        self.data[index].append([self.id, val])

    def snap(self) -> int:
        self.id += 1
        return self.id - 1

    def get(self, index: int, snap_id: int) -> int:
        idx = bisect.bisect_right(self.data[index], [snap_id, 1000000000])
        return self.data[index][idx - 1][1]

# Time complexity = O(nlogn) where n is the number of total calls
# Space complexity = O(n)


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)
