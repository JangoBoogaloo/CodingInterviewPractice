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

[315264]


startValue = 3, destValue = 6

Output: UURL

      7
     /
    5
  // \\
  1   2
//   // \
3   6    4

Constraints:

* The number of nodes in the tree is n.
* 2 <= n <= 10^5
* 1 <= Node.val <= n
* All the values in the tree are unique.
* 1 <= startValue, destValue <= n
* startValue != destValue
"""

from typing import Optional
from enum import Enum

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def _getLca(self, currNode, startVal, dstVal) -> Optional[TreeNode]:
        if not currNode:
            return None
        if currNode.val == startVal or currNode.val == dstVal:
            return currNode
        leftA = self._getLca(currNode.left, startVal, dstVal)
        rightA = self._getLca(currNode.left, startVal, dstVal)
        if leftA and rightA:
            return currNode
        if leftA:
            return leftA
        return rightA

    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:

        lca = self._getLca(root, startValue, destValue)

        
        def DFS(curr, path, targetValue) -> bool:
            if not curr:
                return False
            if curr.val == targetValue:
                return True
            
            path.append("L")
            if DFS(curr.left, path, targetValue):
                return True
            path.pop()
            path.append("R")
            if DFS(curr.right, path, targetValue):
                return True
            path.pop()
            return False
        srcPath, dstPath = [],  []
        DFS(lca, srcPath, startValue)
        DFS(lca, dstPath, destValue)
        
        return "".join(['U' for c in l]) + "".join(r)
