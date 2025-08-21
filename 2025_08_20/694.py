# https://leetcode.com/problems/number-of-distinct-islands/
"""
You are given an `m x n` binary matrix grid.
An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.)
You may assume all four edges of the grid are surrounded by water.

An island is considered to be the same as another if and only if one island can be translated (and not rotated or reflected) to equal the other.

Return the number of distinct islands.

Example

grid =
[
[1,1,0,1,1],
[1,0,0,0,0],
[0,0,0,0,1],
[1,1,0,1,1]
]

output 3
"""
from typing import List


class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        m, n = len(grid[0]), len(grid) # m is cols, n is rows

        encode = []
        res = set()

        def uf_land(loc):
            grid[loc[1]][loc[0]] = 0 # mark as visited - water
                   
            # expand dirs only if land
            for i, (dx, dy) in enumerate([(-1, 0), (1, 0), (0, 1), (0, -1)]):
                next_loc = (loc[0] + dx, loc[1] + dy)
                encode.append(i + 1)

                if 0 <= next_loc[0] < m and 0 <= next_loc[1] < n and grid[next_loc[1]][next_loc[0]] == 1: 
                    uf_land(next_loc)

        for row in range(n):
            for col in range(m):
                if grid[row][col] == 1:
                    encode.append(0)
                    uf_land((col, row))
                
                    res.add(str(encode))
                    encode = []

        return len(res)

