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


Example 1:

Input: n = 5, rides = [[2,5,4],[1,5,1]]
Output: 7
1    5        => 1
 2   5        => 4

Explanation: We can pick up passenger 0 to earn 5 - 2 + 4 = 7 dollars.


Example 2:

Input: n = 20, rides = [[1,6,1],[3,10,2],[10,12,3],[11,12,2],[12,15,2],[13,18,1]]
Output: 20
Explanation: We will pick up the following passengers:
- Drive passenger 1 from point 3 to point 10 for a profit of 10 - 3 + 2 = 9 dollars.
- Drive passenger 2 from point 10 to point 12 for a profit of 12 - 10 + 3 = 5 dollars.
- Drive passenger 5 from point 13 to point 18 for a profit of 18 - 13 + 1 = 6 dollars.
We earn 9 + 5 + 6 = 20 dollars in total.

cost per trip: 
(end_i - start_i + tip_i)



1      6                                         1
  3       10                                    2*     => 10 - 3 + 2
          10    12                              3*     => 12 - 10 + 3
             11 12                              2      => 12 - 11 + 2
                12       15                     2      => 15 - 12 + 2
                   13             18            1*     => 18 - 13 + 1

maxProfitTillHere[loc] = maxProfitTillHere[loc - 1]                   

maxProfitTillHere[end_i] = max(maxProfitTillHere[end_i], maxProfitTillHere[start_i] + (end_i - start_i + tip_i))
"""
from typing import List


class SolutionDP:
    def maxTaxiEarnings(self, locations: int, rides: List[List[int]]) -> int:
        
        # sort by destinations
        rides = sorted(rides, lambda x: x[1])

        maxProfitTillHere = [0] * locations

        # curr ride index
        curr = 0

        for i in range(locations):                        
            maxProfitTillHere[i] = maxProfitTillHere[i - 1]                   

            while curr < len(rides) and rides[curr][1] == i:
                start_i, end_i, tip_i = rides[curr]
                maxProfitTillHere[end_i] = max(maxProfitTillHere[end_i], maxProfitTillHere[start_i] + (end_i - start_i + tip_i))
                curr+=1
        return maxProfitTillHere[-1]

import heapq

class SolutionPQ:
    def maxTaxiEarnings(self, locations: int, rides: List[List[int]]) -> int:
        rides.sort()
        endHeap = []
        for start, end, tip in rides:
            currTripProfit = tip + end - start
            while endHeap and endHeap[0][0] <= start:
                maxProfit = max(maxProfit, endHeap[0][1])
                heapq.heappop(endHeap)
            maxProfit = currTripProfit + maxProfit
            heapq.heappush(endHeap, (end, maxProfit))
        
        while endHeap:
            maxProfit = max(maxProfit, endHeap[1])
            endHeap.pop()

        return maxProfit
    

















