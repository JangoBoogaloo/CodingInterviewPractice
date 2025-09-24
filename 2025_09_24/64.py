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


class SolutionTopDown:
    def minPathSum(self, grid: List[List[int]]) -> int:
        minSumAt = [[-1] * len(grid[0]) for _ in range(len(grid))]
        minSumAt[0][0] = grid[0][0]

        def getSumAt(row, col) -> int:
            if not row and not col:
                return minSumAt[0][0]
            if minSumAt[row][col] != -1:
                return minSumAt[row][col]
            if not row:
                return grid[row][col] + getSumAt(row, col-1)
            if not col:
                return grid[row][col] + getSumAt(row-1, col)
            minSumAt[row][col] = grid[row][col] + min(getSumAt(row, col-1), getSumAt(row-1, col))
            return minSumAt[row][col]

        return getSumAt(len(grid) -1, len(grid[0]) - 1)


class SolutionBottomUp:
    def minPathSum(self, grid: List[List[int]]) -> int:
        return -1


class SolutionMemoryOptimize:
    def minPathSum(self, grid: List[List[int]]) -> int:
        for row in range(1, len(grid)):
            grid[row][0] += grid[row-1][0]
        for col in range(1, len(grid[0])):
            grid[0][col] += grid[0][col-1]

        for row in range(1, len(grid)):
            for col in range(1, len(grid[0])):
                grid[row][col] += min(grid[row-1][col], grid[row][col-1])
        return grid[-1][-1]