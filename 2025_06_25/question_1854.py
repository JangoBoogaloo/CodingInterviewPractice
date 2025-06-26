# https://leetcode.com/problems/maximum-population-year/description/
"""
You are given a 2D integer array logs where each logs[i] = [birth_i, death_i] indicates the birth and death years of the ith person.

The population of some year x is the number of people alive during that year.
The ith person is counted in year x's population if x is in the inclusive range [birth_i, death_i - 1].
Note that the person is not counted in the year that they die.

Return the earliest year with the maximum population.

Constraints:
* 1 <= logs.length <= 100
* 1950 <= birth_i < death_i <= 2050

O(nlogn), O(n)
"""
from typing import List
from collections import Counter

class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:

        # ordered dict {year: pop change}
        c = Counter()
    
        for b,d in logs:
            c[b] += 1 # 2000 +
            c[d] -= 1 # 2090 -

        res = 0
        max = 0
        curr = 0
        for year, change in sorted(c):
            curr += change
            if max < curr:
                max = curr
                res = year

        return res
