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


class Solution:
    def maxScore(self, nums: List[int]) -> int:
        return -1