"""
670. Maximum Swap

You are given an integer num. You can swap two digits at most once to get the maximum valued number.

Return the maximum valued number you can get.



Example 1:

maximumSwap(123) -> 321

Example 2:
maximumSwap(1991) -> 9911


"""

class Solution:
    def maximumSwap(self, num: int) -> int:
        return -1