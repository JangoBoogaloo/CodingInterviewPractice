# https://leetcode.com/problems/single-threaded-cpu/
"""
You are given `n` tasks labeled from `0` to `n - 1` represented by a 2D integer array tasks,
where `tasks[i] = [enqueueTime_i, processingTime_i]`
means that the ith task will be available to process at `enqueueTime_i` and will take `processingTime_i` to finish processing.

You have a single-threaded CPU that can process at most one task at a time and will act in the following way:

* If the CPU is idle and there are no available tasks to process, the CPU remains idle.
* If the CPU is idle and there are available tasks, the CPU will choose the one with the shortest processing time.
  If multiple tasks have the same shortest processing time, it will choose the task with the smallest index.
* Once a task is started, the CPU will process the entire task without stopping.
* The CPU can finish a task then start a new one instantly.

Return the order in which the CPU will process the tasks.

Example 1:

Input: tasks = [[1,2],[2,4],[3,2],[4,1]]

time 1: ready, take task `0` => [1, 2]
time 2: executing...                          task `1` => [2, 4] available        [[2,4]]
time 3: ready, take task `2` [3,2]            task `2` => [3, 2] available        [[2,4]]
time 4: executing...                          task `3` => [4, 1] available        [[4,1], [2,4]]
time 5: ready, take task `3` [4,1]                                                [[2,4]]
time 6: ready, take task `1` [2,4]                                                []
.
.
.
time 10: finish all

Output: [0, 2, 3, 1]
"""
from heapq import heappush, heappop, heapify
from typing import List


class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        task_info = [(start, duration, i) for i, (start, duration) in enumerate(tasks)]
        task_info.sort()

        schedulePQ = []
        currTime = 0
        i = 0
        execution = []
        while i < len(task_info) or schedulePQ:
            if not schedulePQ:
                currTime = max(currTime, task_info[i][0])
            while i < len(task_info) and currTime >= task_info[i][0]:
                _, duration, id = task_info[i]
                heappush(schedulePQ, (duration, id))
                i += 1
            duration, id = heappop(schedulePQ)
            currTime += duration
            execution.append(id)
        return execution