"""
You are given a 0-indexed integer array nums. A subarray of nums is called continuous if:

* Let i, i + 1, ..., j be the indices in the subarray. Then, for each pair of indices i <= i1, i2 <= j, 0 <= |nums[i1] - nums[i2]| <= 2.

Return the total number of continuous subarrays.

A subarray is a contiguous non-empty sequence of elements within an array.

Constraints:

* 1 <= nums.length <= 10^5
* 1 <= nums[i] <= 10^9
"""
from typing import List


class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        return -1


import pytest
target = Solution()

@pytest.mark.parametrize("nums, expect",
[
    ([0, 1, 0, 1, 1, 0, 0], 1),
])
def test_continuousSubarrays(nums, expect):
    assert target.continuousSubarrays(nums) == expect