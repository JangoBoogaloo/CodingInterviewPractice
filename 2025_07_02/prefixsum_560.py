# https://leetcode.com/problems/subarray-sum-equals-k/description/
"""
Given an array of integers `nums` and an integer `k`, return the total number of subarrays whose sum equals to `k`.

A subarray is a contiguous non-empty sequence of elements within an array.

Constraints:
* 1 <= nums.length <= 2 * 10^4
* -1000 <= nums[i] <= 1000
* -10^7 <= k <= 10^7



sum [i..j] -> [i+1, j] or [i, j-1] ->
"""
from typing import List
from collections import Counter

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        curr_sum = 0
        sum_arr_count = Counter()
        k_sum_count = 0
        for num in nums:
            curr_sum += num
            if curr_sum == k:
                k_sum_count += 1

            extra = curr_sum - k
            k_sum_count += sum_arr_count[extra]
            sum_arr_count[curr_sum] += 1
        return k_sum_count