"""
You have `n` jobs and m workers. You are given three arrays: `difficulties`, `profits`, and `workers` where:

`difficulties[i]` and `profits[i]` are the `difficulty` and the `profit` of the `ith` job, and
`workers[j]` is the ability of `jth` worker (i.e., the jth worker can only complete a job with `difficulty` at most `workers[j]`).
Every worker can be assigned at most one job, but one job can be completed multiple times.

For example, if three workers attempt the same job that pays $1, then the total profit will be $3. If a worker cannot complete any job, their profit is $0.
Return the maximum profit we can achieve after assigning the workers to the jobs.
"""

from typing import List


class Solution1:
    def maxProfitAssignment(self, difficulties: List[int], profits: List[int], worker: List[int]) -> int:
        return -1


class Solution2:
    def maxProfitAssignment(self, difficulties: List[int], profits: List[int], worker: List[int]) -> int:
        return -1


class Solution3:
    def maxProfitAssignment(self, difficulties: List[int], profits: List[int], worker: List[int]) -> int:
        return -1


class Solution4:
    def maxProfitAssignment(self, difficulties: List[int], profits: List[int], worker: List[int]) -> int:
        return -1


if __name__ == '__main__':
    sol = Solution1()
    difficulties, profits, workers, expect = [1, 2, 3], [10, 20, 30], [1, 2, 3], 60
    assert sol.maxProfitAssignment(difficulties, profits, workers) == expect

    difficulties, profits, workers, expect = [1, 3, 2], [10, 30, 20], [1, 3, 2], 60
    assert sol.maxProfitAssignment(difficulties, profits, workers) == expect

    difficulties, profits, workers, expect = [1, 2, 3], [30, 20, 10], [1, 2, 3], 90
    assert sol.maxProfitAssignment(difficulties, profits, workers) == expect

    difficulties, profits, workers, expect = [4, 5, 6], [10, 20, 30], [1, 2, 3], 0
    assert sol.maxProfitAssignment(difficulties, profits, workers) == expect