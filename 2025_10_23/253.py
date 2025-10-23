# https://leetcode.com/problems/meeting-rooms-ii/description/
"""
Given an array of meeting time intervals intervals where intervals[i] = [start_i, end_i], return the minimum number of conference rooms required.

Constraints:
* 1 <= intervals.length <= 10^4
* 0 <= start_i < end_i <= 10^6

"""
from typing import List


class Solution2:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        return -1