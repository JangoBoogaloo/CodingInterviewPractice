"""
You are given an integer num . You can swap two digits at most once to get the maximum valued number.

Return the maximum valued number you can get.


Example 1:

* Input: num = "2736"
* Output: 7236
* Explanation: Swap the number 2 and the number 7.


Constraints:
* 0 <= num <= 10^8
"""

class Solution:
    def maximumSwap(self, num: int) -> int:
        return -1