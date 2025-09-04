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

        def lca(curr) -> TreeNode:
            if not curr: 
                return None
            
            if curr.val == p:
                return curr
            elif curr.val == q:
                return curr
            
            l = lca(curr.left)
            r = lca(curr.right)

            if l and r:
                return curr
            elif l:
                return l
            elif r:
                return r
            return None
            
        
        LCA = lca(root)
        #.    3 
        #.  2
        def getDep(curr, target):
            if not curr:
                return -1
                       
            if curr.val == target:
                return 0
            
            l = getDep(curr.left, target)
            r = getDep(curr.right, target)

            if l is not -1:
                return l + 1
            elif r is not -1:
                return r + 1
            return -1
    
        return getDep(LCA, p) + getDep(LCA, q)
