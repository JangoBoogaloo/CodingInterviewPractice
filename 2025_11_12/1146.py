# https://leetcode.com/problems/snapshot-array/description/
"""
Implement a SnapshotArray that supports the following interface:

* SnapshotArray(int length) initializes an array-like data structure with the given length. Initially, each element equals 0.
* void set(index, val) sets the element at the given index to be equal to val.
* int snap() takes a snapshot of the array and returns the snap_id: the total number of times we called snap() minus 1.
* int get(index, snap_id) returns the value at the given index, at the time we took the snapshot with the given snap_id

1, snapshot = [0] * length
2, snapshot[index=0] = val=5   [0, 5]
3, snapid = snap_id+=1 - 1


# snapshot = 0, [5]
# snap
#          = 1, [6]

# get [0,0] -> 5


# snap0 [1,2,3,4,5]
# snap1 [1,9,3,4,5]
# snap2
# ...



# snapshotArray = [[0:1], [0:2, 100:9], [0:3], [0:4, 2:100], [0:5]]
get(1, 50)

Example 1:

Input: ["SnapshotArray","set","snap","set","get"]
[[3],[0,5],[],[0,6],[0,0]]
Output: [null,null,0,null,5]
Explanation: 
SnapshotArray snapshotArr = new SnapshotArray(3); // set the length to be 3
snapshotArr.set(0,5);  // Set array[0] = 5
snapshotArr.snap();  // Take a snapshot, return snap_id = 0
snapshotArr.set(0,6);
snapshotArr.get(0,0);  // Get the value of array[0] with snap_id = 0, return 5

"""
from collections import defaultdict
from bisect import bisect_left, bisect_right

class SnapshotArray:
    def __init__(self, length: int):
        self.snapshotArray = [defaultdict(int) for _ in range(length)]
        self.snapshotId = 0
        return

    def set(self, index: int, val: int) -> None:
        self.snapshotArray[index][self.snapshotId] = val
        return

    def snap(self) -> int:
        self.snapshotId += 1 
        return self.snapshotId - 1

    def get(self, index: int, snap_id: int) -> int:
        snapshots = self.snapshotArray[index].items()
        return snapshots[bisect_right(snapshots, lambda x: x == snap_id ) - 1]
