# https://leetcode.com/problems/maximum-subarray/description/
"""
53. Maximum Subarray

Given an integer array nums, find the subarray with the largest sum, and return its sum.
"""
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        return -1