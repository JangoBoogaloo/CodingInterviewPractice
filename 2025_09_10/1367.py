# https://leetcode.com/problems/linked-list-in-binary-tree/
"""
Given a binary tree root and a linked list with head as the first node.

Return True if all the elements in the linked list starting from the head correspond to some downward path connected in the binary tree otherwise return False.

In this context downward path means a path that starts at some node and goes downwards.


Example 1:
      1
    /   \
  4      4
   \     /
    2   2
  /   /  \
1    6    8
         / \
        1   3
Input:
head = 4->2->8
root = (tree above)

output: true

explanation we can find the path in the tree
  4
 /
2
 \
  8
"""

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        return False