# https://leetcode.com/problems/binary-subarrays-with-sum/description/
"""
Binary Subarrays With Sum

Given a binary array nums and an integer goal, return the number of non-empty subarrays with a sum goal.

A subarray is a contiguous part of the array.


[1,0,1,0,1], 2

=> [101, 0101, 1010, 101] return 4


[0,1,0], 1

[0,1] [1] [1,0] [0,1,0]
"""
from typing import List


class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:

        def findSum(_goal):

            l, r, curr, res = 0, 0, 0, 0
            while r < len(nums):
                curr += nums[r]    # 0, 1
                
                #[101] goal = 2
                while l <= r and curr > _goal:
                    curr -= nums[l]
                    l += 1

                res += (r - l + 1)

        return findSum(goal) - findSum(goal - 1) 
