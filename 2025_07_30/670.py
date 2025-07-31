# https://leetcode.com/problems/maximum-swap/description/
"""
You are given an integer num . You can swap two digits at most once to get the maximum valued number.

Return the maximum valued number you can get.


Example 1:

* Input: num = "2736"
* Output: 7236
* Explanation: Swap the number 2 and the number 7.


Constraints:
* 0 <= num <= 10^8


1, 999991 -> 
2, 111119 -> 911111
3, 123456 -> 623451
4, 123432 -> 412332
5, 121212 -> 221211
6, 987898 -> 997888
7, 95088 -> 98085
8, 95087 -> 98057
9, 954476 -> 974456


   currMax = 9
    currSmall = 5

    if currNum < currMax:
       currSmall = currNum

|||||
95088 -> 98085

"""

class Solution:
    def maximumSwap(self, num: int) -> int:
        numStr = list(str(num))
        if len(numStr) < 2:
            return num

        maxDigitIndex = len(numStr)-1
        leftMostSmallNumIndex, rightMostBigIndex = -1, -1
        for i in range(len(numStr)-2, -1, -1):
            if numStr[i] > numStr[maxDigitIndex]:
                maxDigitIndex = i
            elif numStr[i] < numStr[maxDigitIndex]:
                leftMostSmallNumIndex = i
                rightMostBigIndex = maxDigitIndex

        if leftMostSmallNumIndex != -1:
            numStr[leftMostSmallNumIndex], numStr[rightMostBigIndex] = numStr[rightMostBigIndex], numStr[leftMostSmallNumIndex]
        return int("".join(numStr))