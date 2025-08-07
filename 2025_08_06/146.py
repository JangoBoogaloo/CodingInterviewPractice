# https://leetcode.com/problems/lru-cache/description/
"""
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

* LRUCache(int capacity)
Initialize the LRU cache with positive size capacity.

* int get(int key)
Return the value of the key if the key exists, otherwise return -1.

* void put(int key, int value)
Update the value of the key if the key exists.Otherwise, add the key-value pair to the cache.
If the number of keys exceeds the capacity from this operation, evict the least recently used key.


The functions get and put must each run in O(1) average time complexity.
"""

class Node:
    def __init__(self, prev, next, val):
        self.prev, self.next, self.val = prev, next, val
        
class LRUCache:    

    def __init__(self, capacity: int):
        self.capacity = capacity

        # double linked list
        self.dummyHead, self.dummyTail = Node(None, None, -1), Node(None, None, -1)
        self.dummyHead.next = self.dummyTail
        self.dummyTail.prev = self.dummyHead
        self.cache = self.dummyHead

        # dict {key: pointer}
        self.lookup = {}
        return
 
    def connect(self, prev, curr):
        prev.next, curr.next, curr.prev, prev.next.prev = curr, prev.next, prev, curr
        return

    def get(self, key: int) -> int:
        curr = self.lookup[key]
        if not curr:
            return -1
        else:
            prev = curr.prev
            next = curr.next

            prev.next = next
            next.prev = prev

            # head is the most recent used, tail is the least recent used
            self.connect(self.dummyHead, curr)
        return curr.val
            
    def put(self, key: int, value: int) -> None:
        
        curr = self.lookup(key)

        if curr:
            curr.val = value
            return
        else:
            curr = Node(None, None, value)
            self.lookup[key] = curr

            # add to linkedlist
            self.connect(curr)

            if len(self.lookup) > self.capacity:
                remove_node = self.dummyTail.prev
                kept_node = remove_node.prev
                self.connect(kept_node, self.dummyTail)

                del remove_node
                del self.lookup[key]
        return