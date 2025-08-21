# Maximum Non-adjacent Sum
"""
Given a numeric array with number of elements not less than 3.
Take any two non-adjacent numbers. Get the sum of them.
Get the maximum sum from all the options.

Example
Input:
[1, 3, 4, 3]
 [5, 6]
Expect Output:
6

[3,2,1,1,2,3]
 6,4,3

[1,2,3,3,2,1]
 4,5,5

[  (1,3), (2,3), (3,2), (3,1) ] 

"""

from typing import List

class Solution:
    def maxNonAdjacentSum(self, nums: List[int]) -> int:

        greatest_so_far_pre = float('-inf')
        greatest_sum = greatest_so_far_pre

        for anchor in range(1, len(nums) - 1):
            greatest_so_far_pre = max(greatest_so_far_pre, nums[anchor - 1])
            greatest_sum = max(greatest_sum, greatest_so_far_pre + nums[anchor + 1])

        return greatest_sum


import pytest

target = Solution()

@pytest.mark.parametrize("nums, expect",
[
    ([1, 3, 4, 3], 6),
    ([-10, 3, -2], -12),
    ([1, 5, 4, 1, 3], 8),
])
def test_maxNonAdjacentSum(nums, expect):
    assert target.maxNonAdjacentSum(nums) == expect