# https://leetcode.com/problems/meeting-rooms-ii/description/
"""
Given an array of meeting time intervals intervals where intervals[i] = [start_i, end_i], return the minimum number of conference rooms required.

Constraints:
* 1 <= intervals.length <= 10^4
* 0 <= start_i < end_i <= 10^6

"""
from typing import List
from heapq import *

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        intervals.sort() # sort by start time
        res = 1
        # use start time to solve
        minheap = []
        heappush(minheap, intervals[0][1])
        
        for start, end in intervals[1:]:
            heappush(minheap, end)
            while minheap and start >= minheap[0]:
                heappop(minheap)    

            res = max(res, len(minheap))
        return res

    def minMeetingRoomsByEnds(self, intervals: List[List[int]]) -> int:

        # use end time to solve
        minheap = []

        for start, end in intervals:
            heappush(minheap, (end, start))
        
        res = 1
        # current end time
        prev_end = 0
        while minheap:
            end, start = heappop(minheap)



            if start < prev_end:
               res+=1
                        
            prev_end = end

        return res