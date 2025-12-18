"""
402. Remove K Digits

Given string num representing a non-negative integer num, and an integer k, return the smallest possible integer after removing k digits from num.


Example 1:
removeKdigits("1234", 2) -> "12"

Example 2:
removeKdigits("9399", 2) -> "39"

* more sig, greater, remove

4321 -> 21
1423 -> 12
4231 -> 21
14231 -> 121
12545531 -> 124531


93929 remove 3 digits

1111234 remove 3 digits => 1111
1. iterate from left right
2. remove the more sig, greater
3. if not 2, until the end, remove remaining digits base on remaining removals
"""

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        # remove the more significant greater number
        incStk = [] # min stk

        r = 0

        for r in range(len(num)):

            while incStk and incStk[-1] > num[r]:
                incStk.pop()
                k -= 1
            
            incStk.append(num[r])

        while incStk and k > 0:
            incStk.pop()
            k -= 1

        return "".join(incStk)


class SolutionFinal:
    def removeKdigits(self, num: str, k: int) -> str:
        stepLeft = k
        remainDigits = []
        for digit in num:
            while stepLeft and remainDigits and digit < remainDigits[-1]:
                remainDigits.pop()
                stepLeft -= 1
            remainDigits.append(digit)

        if stepLeft > 0:
            remainDigits = remainDigits[:-stepLeft]

        numStr = "".join(remainDigits).lstrip('0')
        return numStr if numStr else "0"