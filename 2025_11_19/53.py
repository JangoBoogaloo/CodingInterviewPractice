# https://leetcode.com/problems/maximum-subarray/description/
"""
53. Maximum Subarray

Given an integer array nums, find the subarray with the largest sum, and return its sum.
"""
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:


        # kadane's algo O(n)
        currSum = 0
        res = float('-inf')

        for n in nums:

            currSum+=n            
            res = max(res, currSum) 
            
            if currSum < 0:
                currSum = 0
            
        return res






