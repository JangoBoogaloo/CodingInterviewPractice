# https://leetcode.com/problems/course-schedule-ii/
"""
Return the ordering of courses you should take to finish all courses.
If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.
"""
from typing import List
from collections import defaultdict, deque

class SolutionDFS:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        dependencies = defaultdict(list)  # [1 <- 0]
        for ai, bi in prerequisites:
            dependencies[ai].append(bi)

        # for each target, searching for prerequisites
        def findCycles(target, checked_targets, whitelist, res):
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
            res.append(target)
            return False
            
        res = []
        whitelist = set()
        for c in range(numCourses):
            if findCycles(c, set(), whitelist, res):
                return []
        return res



class SolutionBFS:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        dependencies = defaultdict(list)
        prereqcount = defaultdict(int)
        for ai, bi in prerequisites:
            dependencies[bi].append(ai) # dependencies[0] = 1
            prereqcount[ai] += 1        # prereqcount[1] = 1

        ready2take = deque()

        for c in range(numCourses):
            if prereqcount[c] is 0:
                ready2take.append(c)    # ready2take = [0]
        
        res = []
        while ready2take:
            prereq = ready2take.popleft()
            res.append(prereq) 

            for target in dependencies[prereq]:
                prereqcount[target] -= 1
                
                if prereqcount[target] == 0:
                    ready2take.append(target)
                    
        if len(res) != numCourses:
            return []   
        return res

testCases = [
    (3, [[0, 1], [1, 2], [2, 0]]),
    (3, [[1, 0], [2, 1]]),
    (4, [[1, 3], [2, 1], [3, 2], [1, 0]]),
    (4, [[3, 1], [3, 2], [2, 1], [2, 0], [1, 0]]),
]

if __name__ == '__main__':
    solution = SolutionDFS()
    for numCourses, prerequisites in testCases:
        order = solution.findOrder(numCourses, prerequisites)
        print("---------------------------------------------")
        print(f"{numCourses}, {prerequisites} => {order}")