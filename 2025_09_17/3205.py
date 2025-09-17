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
from functools import cache
from typing import List


class SolutionTopDown:
    def maxScore(self, nums: List[int]) -> int:
        @cache
        def maxScoreStartAt(startIndex):
            if startIndex == len(nums):
                return 0

            maxScoreAtStartIndex = 0
            for dstIndex in range(startIndex + 1, len(nums)):
                maxScoreAtStartIndex = max(maxScoreAtStartIndex, (dstIndex - startIndex) * nums[dstIndex] + maxScoreStartAt(dstIndex))
            return maxScoreAtStartIndex

        return maxScoreStartAt(0)


class SolutionBottomUp:
    def maxScore(self, nums: List[int]) -> int:
        maxStartingAt = [0] * len(nums)
        for j in range(1, len(nums)):
            for i in range(j):
                maxStartingAt[j] = max(maxStartingAt[j], maxStartingAt[i] + (j-i)*nums[j])
        return maxStartingAt[-1]


class SolutionMemoryOptimize:
    def maxScore(self, nums: List[int]) -> int:
        maxScore = 0
        score = 0
        for i in range(len(nums)-1, 0, -1):
            maxScore = max(maxScore, nums[i])
            score += maxScore
        return score