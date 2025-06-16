"""
A swap is defined as taking two distinct positions in an array and swapping the values in them.

A circular array is defined as an array where we consider the first element and the last element to be adjacent.

Given a binary circular array nums, return the minimum number of swaps required to group all 1's present in the array together at any location.

Constraints:

* 1 <= nums.length <= 10^5
* nums[i] is either 0 or 1.
"""
from typing import List

class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        return -1


import pytest
target = Solution()

@pytest.mark.parametrize("nums, expect",
[
    ([1,2,3], 6),
])
def test_minSwaps(nums, expect):
    assert target.minSwaps(nums) == expect