# https://leetcode.com/problems/distribute-coins-in-binary-tree/description/
"""
You are given the root of a binary tree with n nodes where each node in the tree has node.val coins. There are n coins in total throughout the whole tree.

In one move, we may choose two adjacent nodes and move one coin from one node to another. A move may be from parent to child, or from child to parent.

Return the minimum number of moves required to make every node have exactly one coin.

Example 1:
Input:
    3
  /  \
0     0
Output: 2
Explain:
    2
  /  \
1     0
    1
  /  \
1     1
-----------------------------------------------

Example 2:

Input:
    0
  /  \
3     0

Output: 3
Explain
    1
  /  \
2     0

    2
  /  \
1     0

    1
  /  \
1     1
"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        return -1