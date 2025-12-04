# https://leetcode.com/problems/spiral-matrix-ii/description/
"""
59. Spiral Matrix II

Given a positive integer n, generate an n x n matrix filled with elements from 1 to n^2 in spiral order.

n = 3
123    (0,0) (0,1) (0,2)
894                (1,2)
765          (2,1) (2,2)

12
43
"""
from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        
        mat = [[0] * n] * n 

        srows= 0, scols = 0
        erows, ecols = n, n

        def spiral(r, c, num, idir):

            if mat[r][c] != 0:
                idir += 1
                idir %= 4 
                return
            
            mat[r][c] = num + 1

            if idir == 0:
                spiral(r, c + 1, num)
            if idir == 1:
                spiral(r+1, c, num)
            if idir == 2:
                spiral(r, c-1, num)
            if idir == 3:
                spiral(r-1, c, num)
            
        return []




class Solution:
    def _valid(self, newR, newC, matrix) -> bool:
        if newR < 0 or newR >= len(matrix):
            return False
        if newC < 0 or newC >= len(matrix[0]):
            return False
        return matrix[newR][newC] == 0

    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0] * n for _ in range(n)]
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        pos = (0, 0)
        directionIndex = 0
        matrix[0][0] = 1
        currNum = 2

        direction = directions[directionIndex]

        while True:
            newR, newC = pos[0] + direction[0], pos[1] + direction[1]
            if self._valid(newR, newC, matrix):
                matrix[newR][newC] = currNum
                currNum += 1
                pos = (newR, newC)
            else:
                directionIndex = (directionIndex+1) % len(directions)
                direction = directions[directionIndex]
                newR, newC = pos[0] + direction[0], pos[1] + direction[1]
                if not self._valid(newR, newC, matrix):
                    break
        return matrix


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0] * n for _ in range(n)]
        row, col = 0, 0
        dr, dc = 0, 1
        for num in range(n*n):
            matrix[row][col] = num + 1
            nr = (row + dr) % n
            nc = (col + dc) % n
            if matrix[nr][nc] != 0:
                # [(0, 1), (1, 0), (0, -1), (-1, 0)]
                dr, dc = dc, -dr
            row += dr
            col += dc
        return matrix




