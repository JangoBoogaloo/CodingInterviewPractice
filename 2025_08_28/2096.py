# https://leetcode.com/problems/step-by-step-directions-from-a-binary-tree-node-to-another/description/
"""
You are given the `root` of a binary tree with `n` nodes.
Each node is "uniquely assigned" a value from `1` to `n`.
You are also given an integer `startValue` representing the value of the start node `s`,
and a different integer `destValue` representing the value of the destination node t.

Find the "shortest path" starting from node `s` and ending at node `t`.
Generate step-by-step directions of such path as a string consisting of only the uppercase letters 'L', 'R', and 'U'.

Each letter indicates a specific direction:
* 'L' means to go from a node to its left child node.
* 'R' means to go from a node to its right child node.
* 'U' means to go from a node to its parent node.

Return the step-by-step directions of the shortest path from node `s` to node `t`.

Example 1
    5
  // \\
  1    2
//   // \
3   6    4

startValue = 3, destValue = 6

Output: UURL


Constraints:

* The number of nodes in the tree is n.
* 2 <= n <= 10^5
* 1 <= Node.val <= n
* All the values in the tree are unique.
* 1 <= startValue, destValue <= n
* startValue != destValue
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def _getAncestor(self, curr: Optional[TreeNode], srcVal, dstVal) -> Optional[TreeNode]:
        if not curr:
            return None
        if curr.val == srcVal or curr.val == dstVal:
            return curr
        leftA = self._getAncestor(curr.left, srcVal, dstVal)
        rightA = self._getAncestor(curr.right, srcVal, dstVal)
        if leftA and rightA:
            return curr
        if leftA:
            return leftA
        return rightA

    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        return ""
