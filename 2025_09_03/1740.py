"""
Given the root of a binary tree and two integers `p` and `q`, return the distance between the nodes of value `p` and value `q` in the tree.

The distance between two nodes is the number of edges on the path from one to the other.


Constraints:

* The number of nodes in the tree is in the range [1, 10^4].
* 0 <= Node.val <= 10^9
* All Node.val are unique.
* p and q are values in the tree.


Example:
    1
   /
  5
 / \
6   2
   /
  7

p = 6, q = 7

Output 3
"""
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findDistance(self, root: Optional[TreeNode], p: int, q: int) -> int:
        return -1
