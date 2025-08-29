"""
You are given an m x n binary matrix grid.
An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.)
You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.


Input:
[
[0,0,1,0,0,0,0,1,0,0,0,0,0],
[0,0,0,0,0,0,0,1,1,1,0,0,0],
[0,1,1,0,1,0,0,0,0,0,0,0,0],
[0,1,0,0,1,1,0,0,1,0,1,0,0],
[0,1,0,0,1,1,0,0,1,1,1,0,0],
[0,0,0,0,0,0,0,0,0,0,1,0,0],
[0,0,0,0,0,0,0,1,1,1,0,0,0],
[0,0,0,0,0,0,0,1,1,0,0,0,0]
]
Output: 6

"""
from typing import List


class Solution:
    curr = 0
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        numRows, numCols = len(grid), len(grid[0])

        res = 0

        self.curr = 0

        def visitLand(row, col):
            if grid[row][col] == 1:
                grid[row][col] = 0
                self.curr += 1
            else:
                return

            for (dx, dy) in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = col + dx, row + dy 
                if 0 <= nx < numCols and 0<= ny < numRows: 
                    visitLand(ny, nx)



        for r in range(numRows):
            for c in range(numCols):
                if grid[r][c] == 1:
                    visitLand(r, c)
                    res = max(res, self.curr)
                    self.curr = 0
        return res
