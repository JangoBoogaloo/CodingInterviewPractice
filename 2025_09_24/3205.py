# https://leetcode.com/problems/maximum-array-hopping-score-i/description/
"""
Given an array nums, you have to get the maximum score starting from index 0 and hopping until you reach the last element of the array.
In each hop, you can jump from index i to an index j > i, and you get a score of (j - i) * nums[j].
Return the maximum score you can get.


Example 1:

Input: nums = [1,5,8]
Output: 16

Explanation:

There are two possible ways to reach the last element:

0 -> 1 -> 2 with a score of (1 - 0) * 5 + (2 - 1) * 8 = 13.

0 -> 2 with a score of (2 - 0) * 8 = 16.

Constraints:
2 <= nums.length <= 10^3
1 <= nums[i] <= 10^5




"""
from typing import List
from functools import *

class SolutionTopDown:
    def maxScore(self, nums: List[int]) -> int:
        @cache
        def recur(upto) -> int:
            
            # exhausted all combos
            if upto is 0:
                return 0

            uptoMax = 0
            for start in range(upto):
                uptoMax = max(uptoMax, (upto - start) * nums[upto] + recur(start))            
            return uptoMax    
        return recur(len(nums) - 1)


class SolutionBottomUp:
    def maxScore(self, nums: List[int]) -> int:

        # states
        maxScore2Here = [0] * len(nums)

        # transition
        for end in range(1, len(nums)):
            for start in range(0, end):
                maxScore2Here[end] = max(maxScore2Here[end], maxScore2Here[start] + (end - start) * nums[end])
 
        return maxScore2Here[-1]


class SolutionOptimize:
    def maxScore(self, nums: List[int]) -> int:

        maxScoreReachable = 0
        #        [3,1,2]
        # nums = [1,3,2]
        #        [1,9,1,2,3]
        max_end_num = nums[-1]
        
        for end in range(len(nums)-1, 0, -1):
            max_end_num = max(max_end_num, nums[end])
            maxScoreReachable += max_end_num
        return maxScoreReachable

        