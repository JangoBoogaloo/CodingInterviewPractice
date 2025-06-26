#
"""
We are given a list `schedule` of employees, which represents the working time for each employee.

Each employee has a list of non-overlapping `Intervals`, and these intervals are in sorted order.

Return the list of finite intervals representing common, positive-length free time for all employees, also in sorted order.

(Even though we are representing `Intervals` in the form [x, y], the objects inside are Intervals, not lists or arrays.
For example, `schedule[0][0].start = 1`, `schedule[0][0].end = 2`, and `schedule[0][0][0]` is not defined).
Also, we wouldn't include intervals like [5, 5] in our answer, as they have zero length.


Constraints:
* 1 <= schedule.length , schedule[i].length <= 50
* 0 <= schedule[i].start < schedule[i].end <= 10^8


Em1  [1,2] [3,4] [5,6]
Em2  [2,3]

Common [4,5]


                   #pos    1   2   3   4    5   6     10  
e1 [1,2],[5,6]     #       1   -1           1   -1
e2 [1,3]           #       1       -1  1              -1
e3 [4,10]          #curr   2   1    0  1    2   1     0
                   #ans             s  e              
"""

from typing import List
from collections import Counter

class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end


class Solution:
    def employeeFreeTime(self, schedule: List[List[Interval]]) -> List[Interval]:

        c = Counter()
        for per in schedule:
            for work in per:          #pos  1   2  3  4   5   6 
                c[work.start] += 1    #     1  -1  1  -1  1  -1
                c[work.end] -= 1      #         1 -1
                                      #curr 1   1  1  0   1   0
                                      #              start end

        res = []
        free_start = -1
        curr_working = 0
        for pos, change in sorted(c.items()):
            curr_working += change
            
            # nobody is working, start common
            if curr_working == 0 and free_start == -1:
                free_start = pos
            elif free_start != -1:
                res.append(Interval(free_start, pos))
                free_start = -1


        return res