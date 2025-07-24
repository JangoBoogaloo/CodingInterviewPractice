# https://leetcode.com/problems/meeting-rooms-ii/description/
"""
Given an array of meeting time intervals intervals where intervals[i] = [start_i, end_i], return the minimum number of conference rooms required.

Constraints:
* 1 <= intervals.length <= 10^4
* 0 <= start_i < end_i <= 10^6

"""
from typing import List
from collections import defaultdict

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:

        # line sweep, convert start and end to one dimensional events
        usages = defaultdict(int)

        for start, end in intervals:
            usages[start] += 1
            usages[end] += -1 

        res = 0
        curr = 0
        for i, t in sorted(usages.items()):
            curr += t
            res = max(curr, res)

        return res


from heapq import *

class Solution2:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # pq sorted by start time
        intervals.sort()
        endTimePQ = []
        heappush(endTimePQ, intervals[0][1])
        maxRooms = 1
        for start, end in intervals[1:]:
            while endTimePQ and endTimePQ[0] <= start:
                heappop(endTimePQ)
            heappush(endTimePQ, end)
            maxRooms = max(len(endTimePQ), maxRooms)
        return maxRooms