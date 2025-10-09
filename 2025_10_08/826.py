"""
You have `n` jobs and m workers. You are given three arrays: `difficulties`, `profits`, and `workers` where:

`difficulties[i]` and `profits[i]` are the `difficulty` and the `profit` of the `ith` job, and
`workers[j]` is the ability of `jth` worker (i.e., the jth worker can only complete a job with `difficulty` at most `workers[j]`).
Every worker can be assigned at most one job, but one job can be completed multiple times.

For example, if three workers attempt the same job that pays $1, then the total profit will be $3. If a worker cannot complete any job, their profit is $0.
Return the maximum profit we can achieve after assigning the workers to the jobs.
"""

from typing import List
from bisect import bisect_right, bisect_left

class Solution1:
    def maxProfitAssignment(self, difficulties: List[int], profits: List[int], worker: List[int]) -> int:

        tasks = sorted(zip(difficulties, profits))  # sort by difficulty

        curr_max_profit = 0
        for i, (d, p) in enumerate(tasks):
            curr_max_profit = max(curr_max_profit, p)
            tasks[i] = (d, curr_max_profit)

        diffs = [d for d, _ in tasks]

        total = 0
        for w in worker:
            i = bisect_right(diffs, w) - 1
            if i >= 0:
                total += tasks[i][1]
        return total


class Solution2:
    def maxProfitAssignment(self, difficulties: List[int], profits: List[int], worker: List[int]) -> int:

        tasks = sorted(zip(profits, difficulties), reverse=True)  # sort by profit

        curr_min_diff = float('inf')
        for i, (p, d) in enumerate(tasks):
            curr_min_diff = min(curr_min_diff, d)
            tasks[i] = (p, curr_min_diff)
  
        diffs = [-d for _, d in tasks]  # [(30, 1), (20, 2), (10, 3)]

        total = 0
        for w in worker:
            i = bisect_right(diffs, -w) - 1
            if 0 <= i < len(tasks):
                print("---> {i}")
                total += tasks[i][0]
        return total
    
    """
    [2, 4, 6, 8, 10]
    [10,20,30,40,50]
    [4,5,6,7]
    
    5

    """

class Solution3:
    def maxProfitAssignment(self, difficulties: List[int], profits: List[int], worker: List[int]) -> int:
        maxAbility = max(worker)
        maxProfitForDifficulty = [0] * (maxAbility + 1)

        for i in range(len(difficulties)):
            difficulty = difficulties[i]
            profit = profits[i]
            if difficulty <= maxAbility:
                maxProfitForDifficulty[difficulty] = max(maxProfitForDifficulty[difficulty], profit)

        for difficulty in range(1, maxAbility + 1):
            maxProfitForDifficulty[difficulty] = max(maxProfitForDifficulty[difficulty], maxProfitForDifficulty[difficulty-1])

        totalProfit = 0
        for difficulty in worker:
            totalProfit += maxProfitForDifficulty[difficulty]
        return totalProfit


class Solution4:
    def maxProfitAssignment(self, difficulties: List[int], profits: List[int], worker: List[int]) -> int:
        return -1


if __name__ == '__main__':
    sol = Solution1()
    #[1, ]
    difficulties, profits, workers, expect = [1, 2, 3], [10, 20, 30], [1, 2, 3], 60
    assert sol.maxProfitAssignment(difficulties, profits, workers) == expect

    difficulties, profits, workers, expect = [1, 3, 2], [10, 30, 20], [1, 3, 2], 60
    assert sol.maxProfitAssignment(difficulties, profits, workers) == expect

    difficulties, profits, workers, expect = [1, 2, 3], [30, 20, 10], [1, 2, 3], 90
    # 1 - 30, 2 - 30, 3 - 30
    assert sol.maxProfitAssignment(difficulties, profits, workers) == expect

    difficulties, profits, workers, expect = [4, 5, 6], [10, 20, 30], [1, 2, 3], 0
    assert sol.maxProfitAssignment(difficulties, profits, workers) == expect