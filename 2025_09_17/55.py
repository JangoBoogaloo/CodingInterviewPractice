
"""
You are given an integer array `nums`.
You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return `true` if you can reach the last index, or `false` otherwise.
"""
from functools import lru_cache
from typing import List

# [2,3,1,1,0]
# expect true but get false

# [3, 0, 0, 100, 100.....]
# 100 data

class Solution:
    def canJump1(self, nums: List[int]) -> bool:
        #can reach this point from beginning
        dp = [False] * len(nums)
        dp[-1] = True
        # [ .... ......2, 0, 1]
        for left in range(len(nums)-1, -1, -1):
            rightRange = min(left + nums[left], len(nums) - 1)
            for right in range(left+1, rightRange):
                if dp[right]:
                    dp[left] = True
                    break
        return dp[0]

    def canJump2(self, nums: List[int]) -> bool:
        dest = len(nums)
        max_reachable = 0
         
        for curr in range(0, dest):
            if max_reachable < curr:
                return False
            max_reachable = max(max_reachable, curr + nums[curr])
            if max_reachable >= dest - 1:
                return True
        return False

    def canJump3(self, nums: List[int]) -> bool:

        dest = len(nums) - 1

        dp = {}

        def recur(curr) -> int:

            if curr >= dest:
                return dest
            if curr in dp:
                return dp[curr]

            max_reachable = curr
            for offset in range(nums[curr], 0, -1):
                if curr + offset < dest:
                    max_reachable = max(max_reachable, recur(curr + offset))
                else:
                    dp[curr] = dest
                    return dest
            dp[curr] = max_reachable
            return max_reachable

        return dest == recur(0)