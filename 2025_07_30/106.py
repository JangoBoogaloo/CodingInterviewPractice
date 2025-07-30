"""
Given two integer arrays inorder and postorder
where inorder is the inorder traversal of a binary tree and postorder is the postorder traversal of the same tree,
construct and return the binary tree.

Example:
  3
 / \
9   20
   /  \
  15   7

inorder = [9, 3, 15, 20, 7]
postorder = [9, 15, 7, 20, 3]
"""
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        return None