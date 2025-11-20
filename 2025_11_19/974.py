
"""
Subarray Sums Divisible by K

Given an integer array nums and an integer k, return the number of non-empty subarrays that have a sum divisible by k.

A subarray is a contiguous part of an array.


[4,5,0,-2,-3,1]
[4,9,9, 7, 4,5]

5

expect 7 but get 2
"""
from typing import List
from itertools import accumulate

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:

        # use prefix sum to quickly find sum over range l and r.
        # use combinations to enum all ranges.
        prefixSum = list(accumulate(nums))

        r, res = 0, 0

        # (prefix[right] - prefix[left]) % k = 0
        # prefix[current] % k ?
        # prefix[right] % k - prefix[left] %k = 0
        # prefix[cur2] % k = prefix[cur1] % k

        while r < len(nums):
            l = 0
            while l <= r:
                if (prefixSum[r] - prefixSum[l] + nums[l]) % k == 0:
                    res += 1
                l+=1
            r+=1


        return res


class Solution2:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        accSum = 0
        count = 0
        freqs = [0] * k
        freqs[0] = 1
        for i, num in enumerate(nums):
            accSum += num
            accSum = accSum % k
            count += freqs[accSum]
            freqs[accSum] += 1
        return count






