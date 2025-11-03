"""
Given an `m x n` 2D binary grid `grid` which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1


Input: grid = [
  ["1","1","1","1“],
  ["1","1","1","1”],
  ["1","1","1","1“]
]

Input: grid = [
  ["1","1","1","1“],
  ["1","0","1","1”],
  ["1","1","1","1“]
]

Input: grid = [
  ["0","0","0","0“],
  ["0","0","0","0”],
  ["0","0","0","0“]
]

Input: grid = [
  ["0","1","0","0“],
  ["1","1","1","0”],
  ["0","1","0","1“]
]


"""
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
      cols, rows = len(grid[0]), len(grid)

      dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]
      
      def explore(r, c) -> None:
        if grid[r][c] == "0" or grid[r][c] == "2": #water or visited
           return
        
        grid[r][c] = "2" 

        for dx, dy in dirs:
          next_c = c
          if 0 <= c + dx and c + dx < cols:
             next_c = c + dx
          next_r = r
          if 0 <= r + dy and r + dy < rows:
             next_r = r + dy 
          explore(next_r, next_c)

      res = 0
      for r in range(rows): 
        for c in range(cols):                
          if grid[r][c] == "1":
            explore(r, c)
            res+=1

      return res