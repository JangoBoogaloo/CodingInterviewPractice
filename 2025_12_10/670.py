"""
670. Maximum Swap

You are given an integer num. You can swap two digits at most once to get the maximum valued number.

Return the maximum valued number you can get.

Example 1:

maximumSwap(123) -> 321

Example 2:
maximumSwap(1991) -> 9911

1, mono increasing
2, cambel 1 98 1
3, mono decreasing   321
4, rev-cammel   9 11 8

98117 -> 98711

98711611

98742612
   * * 

2121
 **

1. have to visit from right to left
2. less significant max, swap with more significant smaller
"""

class Solution:
    def maximumSwap(self, num: int) -> int:
        numStr = list(str(num))
        if len(numStr) < 2:
            return num

        maxDigit = len(numStr) - 1
        bigger, smaller = -1, -1

        # iter right to left
        # 19816
        for r in range(len(numStr) - 2, -1, -1):
            if numStr[maxDigit] < numStr[r]:
                maxDigit = r
            # 213
            if numStr[r] < numStr[maxDigit]:
                smaller = r
                bigger = maxDigit
            
        if smaller != -1:
            numStr[smaller], numStr[bigger] = numStr[bigger], numStr[smaller] 
        return int("".join(numStr))





