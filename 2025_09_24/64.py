# https://leetcode.com/problems/minimum-path-sum/description/
"""
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example 1:
Input: grid =
[
[1, 3, 1],
[1, 5, 1],
[4, 2, 1]
]

output: 7

Explanation:
1, 3, 1
      1
      1

"""
from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        return -1