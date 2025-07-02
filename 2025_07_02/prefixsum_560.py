# https://leetcode.com/problems/subarray-sum-equals-k/description/
"""
Given an array of integers `nums` and an integer `k`, return the total number of subarrays whose sum equals to `k`.

A subarray is a contiguous non-empty sequence of elements within an array.

Constraints:
* 1 <= nums.length <= 2 * 10^4
* -1000 <= nums[i] <= 1000
* -10^7 <= k <= 10^7
"""
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        return -1