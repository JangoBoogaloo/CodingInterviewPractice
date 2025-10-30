# https://leetcode.com/problems/as-far-from-land-as-possible/description/
"""
Given an n x n grid containing only values 0 and 1, where 0 represents water and 1 represents land,
find a water cell such that its distance to the nearest land cell is maximized, and return the distance.
If no land or water exists in the grid, return -1.

The distance used in this problem is the Manhattan distance: the distance between two cells (x0, y0) and (x1, y1) is |x0 - x1| + |y0 - y1|.

Example 1:

grid =
[
[1, 0, 1],
[0, 0, 0],
[1, 0, 1]
]

output 2

"""
from typing import *
from collections import *


class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        
        cols, rows = len(grid[0]), len(grid)

        lands = deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    lands.append((r, c))
                    grid[r][c] = '2'

        dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        res = -1

        while lands:
            layer_size = len(lands)
            for i in range(layer_size):
                r, c = lands.popleft()                            
                for dx, dy in dirs:
                    next_r, next_c = r + dy if 0 <= r + dy < rows else r, c + dx if 0 <= c + dx < cols else c
                    if grid[next_r][next_c] is "0":
                        lands.append((next_r, next_c))
                        grid[next_r][next_c] = '2'
            res += 1
        return res if res != -1 else res + 1










