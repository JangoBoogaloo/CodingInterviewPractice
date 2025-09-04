# https://leetcode.com/problems/remove-nodes-from-linked-list/description/
"""
You are given the head of a linked list.

Remove every node which has a node with a greater value anywhere to the right side of it.

Return the head of the modified linked list.


Input: head = [5,2,13,3,8]
Output: [13,8]

5->2->13->13->3->8

5->2->13->3->8
   |
   5

5->3->1->2


1, have 5, carried 5 
2, have 3, carried 5
3, have 1, carried 5
3, have 2, carried 2, return 2 


13->8

"""

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# [5,2,13,3,8]
# [5,13,8]

class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def recur(curr) -> ListNode:

            if not curr:
                return None

            if not curr.next:
                return curr

            curr.next = recur(curr.next)
               
            curr_val = curr.val
            next_val = curr.next.val

            if curr_val < next_val:
                return curr.next
            return curr
               
        return recur(head)























