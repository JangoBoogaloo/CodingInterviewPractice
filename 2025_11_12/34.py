# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/
"""
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

test1 = [1,2,3,3,5,6]  target = 3, 4, 0, 9, 2

ans10 = [2,3]
ans11 = [-1, -1]
ans12, ans13 = [-1, -1]

ans14 = [1, 1]
"""
from typing import List
from bisect import bisect_left, bisect_right

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        # nums = [1,2,3,3,5,6] 
        #             | |
        #             l r            <-   target = 3
        #                 | 
        #                 l,r        <-   target = 4
        #         |
        #         l, r               <-   target = 0
        #                   |
        #                   l, r     <-   target = 7
        l, r = bisect_left(nums, target), bisect_right(nums, target) - 1


        return [l, r] if l <= r else [-1, -1]


        




