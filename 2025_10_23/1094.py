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
from heapq import heappush, heappop


class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        startTimeTrips = sorted(trips, key=lambda x: x[1])
        endTimePassengersHeap = []
        passengersInCar = 0
        for passengers, start, end in trips:
            while endTimePassengersHeap and endTimePassengersHeap[0][0] <= start:
                passengersInCar -= endTimePassengersHeap[0][1]
                heappop(endTimePassengersHeap)
            passengersInCar += 1
            if passengersInCar > capacity:
                return False
            heappush(endTimePassengersHeap, (end, passengers))
        return True