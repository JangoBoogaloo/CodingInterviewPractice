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
from functools import *

class SolutionTopDown:
    def minPathSum(self, grid: List[List[int]]) -> int:

        @cache
        def recur(r, c) -> int:

            if r is 0 and c is 0:
                return grid[0][0]
            if r is 0:
                return grid[0][c] + recur(0, c - 1)
            if c is 0:
                return grid[r][0] + recur(r - 1, 0)
            
            return min(recur(r-1, c), recur(r, c-1)) + grid[r][c]

        return recur(len(grid) - 1, len(grid[0]) - 1)


class SolutionBottomUp:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        # state
        min2Here = [0] * cols

        # init first row
        min2Here[0] = grid[0][0]
        for i in range(1, cols):
            min2Here[i] = grid[0][i] + min2Here[i-1]

        # transition
        for r in range(1, rows):
            for c in range(cols):
                min2Here[c] = min(min2Here[c-1], min2Here[c]) + grid[r][c]

        return min2Here[-1]


class SolutionMemoryOptimize:
    def minPathSum(self, grid: List[List[int]]) -> int:  
        return -1