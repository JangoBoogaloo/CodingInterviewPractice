# Maximum Non-adjacent Sum
"""
Given a numeric array with number of elements not less than 3.
Take any two non-adjacent numbers. Get the sum of them.
Get the maximum sum from all the options.

Example
Input:
[1, 3, 4, 3]
Expect Output:
6
"""

from typing import List

class Solution:
    def maxNonAdjacentSum(self, nums: List[int]) -> int:
        return -1