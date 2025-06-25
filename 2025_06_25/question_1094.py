# https://leetcode.com/problems/car-pooling/description/
"""
There is a car with `capacity` empty seats. The vehicle only drives east (i.e., it cannot turn around and drive west).

You are given the integer `capacity` and an array `trips` where:
trips[i] = [numPassengers_i, from_i, to_i] indicates that the `ith` trip has `numPassengers_i` passengers,
and the locations to pick them up and drop them off are `from_i` and `to_i` respectively.
The locations are given as the number of kilometers due east from the car's initial location.

Return `true` if it is possible to pick up and drop off all passengers for all the given trips, or `false` otherwise.


Constraints:

* 1 <= trips.length <= 1000
* trips[i].length == 3
* 1 <= numPassengers_i <= 100
* 0 <= from_i < to_i <= 1000
* 1 <= capacity <= 10^5
"""
from typing import List


class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        return False