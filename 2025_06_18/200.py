# https://leetcode.com/problems/number-of-islands/description/
"""
Given an m x n 2D binary grid `grid` which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

increment islands if 1s
dfs(i,j)
    action: left, right, top, down.
    condition: if water  ret
               if visited ret
               if 1s, mark as visited

"""
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        actions = [(-1,0), (1,0), (0,1), (0,-1)]

        width, height = len(grid[0]), len(grid)
        
        def dfs(i, j):
            for x,y in actions:
                next_x, next_y = i+x, j+y
                # out of bound
                if next_x < 0 or next_x >= width or next_y < 0 or next_y >= height:
                    continue
                # water
                elif grid[next_y][next_x] == '0' or grid[next_y][next_x] == '2':
                    continue
                elif grid[next_y][next_x] == '1':
                    grid[next_y][next_x] = '2' # visited
                    dfs(next_x, next_y)
                else:
                    assert(-1)
            return

        res = 0
        for j in range(height):
            for i in range(width):
                if grid[j][i] == '1':
                    res +=1 
                    dfs(i, j)

        return res