# https://leetcode.com/problems/brightest-position-on-street/
"""
A perfectly straight street is represented by a number line.
The street has street lamp(s) on it and is represented by a 2D integer array lights.
Each `lights[i] = [position_i, range_i]` indicates that there is a street lamp at position `position_i` that
lights up the area from [position_i - range_i, position_i + range_i] (inclusive).

The brightness of a position `p` is defined as the number of street lamp that light up the position `p`.

Given `lights`, return the brightest position on the street. If there are multiple brightest positions, return the smallest one.

Constraints:

* 1 <= lights.length <= 10^5
* lights[i].length == 2
* -10^8 <= position_i <= 10^8
* 0 <= range_i <= 10^8

Example 1 (see image)
* Input: lights = [[-3,2],[1,2],[3,3]]
* Output: -1
"""
from typing import List
from collections import Counter


class Solution:
    def brightestPosition(self, lights: List[List[int]]) -> int:

        c = Counter()
                                   #      [-3,2]      [1,2]      [3,3]
        for pos, ran in lights:    # pos  -5  0       -1  4       0 7
            c[pos - range] += 1     #      1  -1       1  -1      1 -1
            c[pos + range + 1] -=1  #      -5=1   -1=1   ... 

        res = 0
        curr = 0
        max = 0
        for pos, change in sorted(c):
            curr += change # duration
            if max < curr:
                max = curr
                res = pos

        return res