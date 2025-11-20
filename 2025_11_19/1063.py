# https://leetcode.com/problems/number-of-valid-subarrays/description/
"""
Given an integer array nums, return the number of non-empty subarrays with the 
leftmost element of the subarray not larger than other elements in the subarray.

A subarray is a contiguous part of an array.


[1,4,2,5,3]

=> 11

"""
from typing import List


class Solution:
    def validSubarrays(self, nums: List[int]) -> int:

        # find the next smaller
        incStk = []
        res = 0

        # number of non-empty subarrays

        for i, n in enumerate(nums):

            while incStk and nums[incStk[-1]] > n:
                prev_i = incStk.pop()

            if incStk:
                res += i - incStk[0]

            incStk.append(i)

        return res


class Solution:
    def validSubarrays(self, nums: List[int]) -> int:
        increaseNumStack = []
        valid = 0
        for i in range(len(nums)):
            while increaseNumStack and nums[i] < increaseNumStack[-1]:
                increaseNumStack.pop()
            increaseNumStack.append(nums[i])
            valid += len(increaseNumStack)
        return valid







