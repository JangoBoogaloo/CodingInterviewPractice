# https://leetcode.com/problems/range-sum-query-immutable/description/
"""
Given an integer array nums, handle multiple queries of the following type:

Calculate the sum of the elements of `nums` between indices `left` and `right` inclusive where `left <= right`.
Implement the `NumArray` class:

* `NumArray(int[] nums)` Initializes the object with the integer array `nums`.
* `int sumRange(int left, int right)` Returns the sum of the elements of `nums` between indices `left` and `right` inclusive
  (i.e. `nums[left] + nums[left + 1] + ... + nums[right]`).

Constraints:

* 1 <= nums.length <= 10^4
* -10^5 <= nums[i] <= 10^5
* 0 <= left <= right < nums.length
* At most 10^4 calls will be made to sumRange.
"""
from typing import List


class NumArray:
    def __init__(self, nums: List[int]):
        # num = [...]
        # arr = [0-0, 0-1, 0-2, 0-3]
        # sum(1-2) = sum(0-2) - sum(0-0)
        self.arr = [0] * len(nums)
        self.arr[0] = nums[0]
        for i in range(1, len(nums)):                    #i  arr[1]               arr[2]
            self.arr[i] = nums[i] + self.arr[i - 1]      #   arr[0]+nums[1]       arr[1] + nums[2]
        return

    def sumRange(self, left: int, right: int) -> int:
        
        if left == 0:
            return self.arr[right]

        return self.arr[right] - self.arr[left - 1]