# https://leetcode.com/problems/course-schedule/description/
"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1.

You are given an array `prerequisites` where `prerequisites[i] = [ai, bi]`
* indicates that you must take course `bi` first if you want to take course `ai`.

For example, the pair `[0, 1]`, indicates that to take course `0` you have to first take course `1`.
Return true if you can finish all courses. Otherwise, return false.

"""
from typing import List
from collections import defaultdict, deque

# [[1,0]]
class SolutionDFS:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        dependencies = defaultdict(list)  # [1 <- 0]
        for ai, bi in prerequisites:
            dependencies[ai].append(bi)

        # for each target, searching for prerequisites
        def findCycles(target, checked_targets, whitelist):
            if target in whitelist:
                return False
            # target = 1
            # target = 0
            for prereq in dependencies[target]:
                # prereq = 0
                if prereq in checked_targets:
                    return True
                
                checked_targets.add(prereq)
                if findCycles(prereq, checked_targets, whitelist):
                    return True
                checked_targets.remove(prereq)
            whitelist.add(target)
            return False
            
        whitelist = set()
        for c in range(numCourses):
            if findCycles(c, set(), whitelist):
                return False
        return True


class SolutionBFS:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        dependencies = defaultdict(list)
        prereqcount = defaultdict(int)
        for ai, bi in prerequisites:
            dependencies[bi].append(ai) # dependencies[0] = 1
            prereqcount[ai] += 1        # prereqcount[1] = 1


        ready2take = deque()

        for c in range(numCourses):
            if prereqcount[c] is 0:
                ready2take.append(c)    # ready2take = [0]

        total_ready = 0
        while ready2take:
            prereq = ready2take.popleft()
            total_ready += 1 

            for target in dependencies[prereq]:
                prereqcount[target] -= 1
                
                if prereqcount[target] == 0:
                    ready2take.append(target)
                    
        if total_ready == numCourses:
            return True
        return False


testCases = [
    (3, [[0, 1], [1, 2], [2, 0]], False), #  2 <- 0, 0 <- 1, 1 <- 2,
    (3, [[1, 0], [2, 1]], True),
    (4, [[1, 3], [2, 1], [3, 2], [1, 0]], False),
    (4, [[3, 1], [3, 2], [2, 1], [2, 0], [1, 0]], True), #  
]

if __name__ == '__main__':
    solution = SolutionDFS()
    for numCourses, prerequisites, expect in testCases:
        actual =  solution.canFinish(numCourses, prerequisites)
        if actual != expect:
            print("---------------------------------------------")
            print(f"expect: {numCourses}, {prerequisites} => {expect}")
            print(f"actual: {numCourses}, {prerequisites} => {actual}")

