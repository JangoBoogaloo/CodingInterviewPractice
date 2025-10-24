# https://leetcode.com/problems/car-pooling/description/
"""
There is a car with `capacity` empty seats. The vehicle only drives east (i.e., it cannot turn around and drive west).

You are given the integer `capacity` and an array `trips` where:
`trips[i] = [numPassengers_i, from_i, to_i] indicates that
the ith trip has `numPassengers_i` passengers and the locations to pick them up and drop them off are `from_i` and `to_i` respectively.
The locations are given as the number of kilometers due east from the car's initial location.

Return true if it is possible to pick up and drop off all passengers for all the given trips, or false otherwise.

Example 1:

Input: trips = [[2,1,5],[3,3,7]], capacity = 4
Output: false
Example 2:

Input: trips = [[2,1,5],[3,3,7]], capacity = 5
Output: true
"""
from typing import List
from heapq import *

"""
[[2,1,5],[3,3,7]]
5
"""
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:

        minheap = []

        trips.sort(key=lambda x:x[1]) # sort by pickup time

        capacity -= trips[0][0]

        if capacity < 0:
            return False
        #                  end          passengers
        heappush(minheap, (trips[0][2], trips[0][0]))

        for pa, start, end in trips[1:]:
            # check getting off the car
            while minheap and start >= minheap[0][0]:
                capacity += minheap[0][1]
                heappop(minheap)
            # check validity for next
            if capacity < pa:
                return False
            
            # hopping onto the car
            heappush(minheap, (end, pa))
            capacity -= pa
        return True
    










