# https://leetcode.com/problems/maximum-earnings-from-taxi/description/
"""
There are n points on a road you are driving your taxi on.
The `n` points on the road are labeled from `1` to `n` in the direction you are going,
and you want to drive from point `1` to point `n` to make money by picking up passengers. You cannot change the direction of the taxi.

The passengers are represented by a 0-indexed 2D integer array rides,
where `rides[i] = [start_i, end_i, tip_i]` denotes the ith passenger requesting a ride
from point `start_i` to point `end_i` who is willing to give a `tip_i` dollar tip.

For each passenger i you pick up, you earn `end_i` - `start_i` + `tip_i` dollars.
You may only drive at most one passenger at a time.

Given `n` and `rides`, return the maximum number of dollars you can earn by picking up the passengers optimally.

Note: You may drop off a passenger and pick up a different passenger at the same point.
"""
from typing import List
from heapq import *

class SolutionDP:
    def maxTaxiEarnings(self, locations: int, rides: List[List[int]]) -> int:
        maxProfitAt = [0] * (locations+1)
        rides.sort(key=lambda r: r[1])
        rideIndex = 0
        for location in range(1, len(maxProfitAt)):
            maxProfitAt[location] = maxProfitAt[location-1]
            while rideIndex < len(rides) and location == rides[rideIndex][1]:
                start, end, tip = rides[rideIndex]
                profit = tip + end - start
                maxProfitAt[location] = max(maxProfitAt[location], maxProfitAt[start] + profit)
                rideIndex += 1
        return maxProfitAt[-1]



class SolutionPQ:
    def maxTaxiEarnings(self, locations: int, rides: List[List[int]]) -> int:
        rides.sort()
        end_profit_heap = []
        prevMaxProfit = 0
        for start, end, tip in rides:
            if end > locations:
                continue
            singleProfit = tip + end - start
            while end_profit_heap and start >= end_profit_heap[0][0]:
                prevMaxProfit = max(prevMaxProfit, end_profit_heap[0][1])
                heappop(end_profit_heap)
            currentMaxProfit = prevMaxProfit + singleProfit
            heappush(end_profit_heap, (end, currentMaxProfit))

        maxProfit = 0
        while end_profit_heap:
            _, profit = heappop(end_profit_heap)
            maxProfit = max(maxProfit, profit)
        return maxProfit