"""
You are given a 0-indexed array of positive integers w where w[i] describes the weight of the ith index.

You need to implement the function pickIndex(), which randomly picks an index in the range [0, w.length - 1] (inclusive) and returns it.
The probability of picking an index i is w[i] / sum(w).


For example, if w = [1, 3], the probability of picking index 0 is 1 / (1 + 3) = 0.25 (i.e., 25%),
and the probability of picking index 1 is 3 / (1 + 3) = 0.75 (i.e., 75%).

Constraints:

* 1 <= w.length <= 10^4
* 1 <= w[i] <= 10^5
* pickIndex will be called at most 10^4 times.



w = [1,2,3,4,5] sum = 15
     1,3,6,10,15
p = [1/15, 2/15 ...]

random % 15 = 

"""
from typing import List
from itertools import *
from collections import *
from bisect import *
from heapq import *

class Solution:
    def __init__(self, w: List[int]):

        # go through arary to get prefix sum
        # end of it, will get total sum
        self.curr = 0
        self.prefix = []
        for n in w:
            self.curr += n
            self.prefix.append(self.curr)
        self.max = self.curr
        return

    def pickIndex(self) -> int:
        target = uniform(0, 1) * self.max
        return bisect_right(self.prefix, target)