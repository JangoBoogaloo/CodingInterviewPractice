# https://leetcode.com/problems/task-scheduler/description/
"""
You are given an array of CPU `tasks`, each labeled with a letter from 'A' to 'Z', and a number `n`.
Each CPU interval can be idle or allow the completion of one task.
Tasks can be completed in any order, but there's a constraint: there has to be a gap of at least `n` intervals between two tasks with the same label.

Return the minimum number of CPU intervals required to complete all tasks.

Example 1:

Input: tasks = ["A","A","A","B","B","B"], n = 2

"AAAAAAA"

"A" execute at 0 => next "A" execute at 3

Output: 8

Explanation: A possible sequence is: A -> B -> idle -> A -> B -> idle -> A -> B.

After completing task A, you must wait two intervals before doing A again.
The same applies to task B. In the 3rd interval, neither A nor B can be done, so you idle. By the 4th interval, you can do A again as 2 intervals have passed.

Example 2:

Input: tasks = ["A","C","A","B","D","B"], n = 1

Output: 6

Explanation: A possible sequence is: A -> B -> C -> D -> A -> B.

With a cooling interval of 1, you can repeat a task after just one other task.
"""
from typing import List
from collections import Counter, deque
from heapq import *

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_count = Counter(tasks)
        maxCountHeap = [-count for count in task_count.values()]
        heapify(maxCountHeap)
        time = 0
        taskQueue = deque()
        while maxCountHeap or taskQueue:
            time += 1
            if maxCountHeap:
                currentTaskCount = -heappop(maxCountHeap)
                nextTaskCount = currentTaskCount - 1
                if nextTaskCount:
                    nextTaskTime = time + n
                    taskQueue.append((nextTaskCount, nextTaskTime))
            if taskQueue and taskQueue[0][1] == time:
                remainCount, _ = taskQueue.popleft()
                heappush(maxCountHeap, -remainCount)
        return time