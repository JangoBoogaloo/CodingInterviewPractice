# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
"""
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia:
“The lowest common ancestor is defined between two nodes `p` and `q`
as the lowest node in `T` that has both `p` and `q` as descendants (where we allow a node to be a descendant of itself).”
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
        def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

            def lca(curr) -> TreeNode:

                if not curr:
                    return None                
                
                if curr.val == p.val:
                    return curr
                elif curr.val == q.val:
                    return curr
                
                a = lca(curr.left)
                b = lca(curr.right)

                if a and b:
                    return curr
                elif a and not b:
                    return a
                elif b and not a:
                    return b
                return None

            return lca(root)














