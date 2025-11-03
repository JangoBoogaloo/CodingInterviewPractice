# https://leetcode.com/problems/number-of-islands-ii/description/
"""
You are given an empty 2D binary grid grid of size m x n.
The grid represents a map where 0's represent water and 1's represent land.
Initially, all the cells of grid are water cells (i.e., all the cells are 0's).

We may perform an add land operation which turns the water at position into a land.
You are given an array positions where positions[i] = [ri, ci] is the position (ri, ci) at which we should operate the ith operation.

Return an array of integers answer where answer[i] is the number of islands after turning the cell (ri, ci) into a land.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
You may assume all four edges of the grid are all surrounded by water.


Input: m = 3, n = 3, positions = [[0,0],[0,1],[1,2],[2,1]]
Output: [1, 1, 2, 3]

               1,          1,          2,          3

0, 0, 0     1, 0, 0     1, 1, 0     1, 1, 0     1, 1, 0
0, 0, 0  => 0, 0, 0  => 0, 0, 0  => 0, 0, 1  => 0, 0, 1
0, 0, 0     0, 0, 0     0, 0, 0     0, 0, 0     0, 1, 0


UF.find(data) -> rep

def find(self, data):

def union(self, data1, data2) data1 data2 with same rep

def add(self, data) // add data to set

def exist(self, data) // is data in disjoint set

"""
from collections import *
class UF:
    def __init__(self):
        self._rank = Counter()
        self._parent = defaultdict()
        self._count = 0
        return

    def add(self, data) -> None:
        if self._parent.get(data) is None:
            self._parent[data] = data
            self._count += 1

    def valid(self, data) -> bool:
        return self._parent.get(data) is not None

    def find(self, data):
        if self._parent.get(data) is None:
            raise ValueError(f"data {data} is not added")
        if self._parent.get(data) != data:
            self._parent[data] = self.find(self._parent.get(data))
        return self._parent[data]

    def union(self, data1, data2) -> None:
        data1Root, data2Root = self.find(data1), self.find(data2)
        if data1Root == data2Root:
            return
        if self._rank[data1Root] > self._rank[data2Root]:
            self._parent[data2Root] = data1Root
        elif self._rank[data1Root] < self._rank[data2Root]:
            self._parent[data1Root] = data2Root
        else:
            self._parent[data2Root] = data1Root
            self._rank[data1Root] += 1
        self._count -= 1

    def __len__(self):
        return self._count


from typing import List

#   2          1
# [1,0,1] => [1,1,1]

class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:        
        uf = UF()
        res = []
        dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        for r, c in positions:
            uf.add((r, c))
            for dy, dx in dirs:
                next_r, next_c = r + dy if 0 <= r + dy < m else r, c + dx if 0 <= c + dx < n else c

                if uf.valid((next_r, next_c)):
                    uf.union((r,c), (next_r, next_c))
                res.append(len(uf))
        return res
