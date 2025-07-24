# https://leetcode.com/problems/daily-temperatures/
"""
Given an array of integers `temperatures` represents the daily temperatures,
return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature.
If there is no future day for which this is possible, keep answer[i] == 0 instead.

temperature = [1,3,2,4]
ans =         [1,2,1,0]

[30,50,40,60]
[1,2,1,0]

Constrain
* 30 <= temperatures[i] <= 100
"""
from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        # monotonic stack of indices of the day
        n = len(temperatures)
        d = 0
        stk = []

        res = [0] * n
        while d < n:
            while stk and temperatures[stk[-1]] < temperatures[d]:
                prev_temp_idx = stk.pop() # check prev day temp until colder    
                res[prev_temp_idx] = d - prev_temp_idx # recent colder day
            stk.append(d)
            d+=1
        return res