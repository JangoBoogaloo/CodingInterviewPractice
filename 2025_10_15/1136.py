# https://leetcode.com/problems/parallel-courses/description/
"""
You are given an integer `n`, which indicates that there are `n` courses labeled from `1` to `n`.
You are also given an array `relations` where `relations[i] = [prevCoursei, nextCoursei]`,
representing a prerequisite relationship between course `prevCoursei` and course `nextCoursei`: course `prevCoursei` has to be taken before course `nextCoursei`.

In one semester, you can take any number of courses as long as you have taken all the prerequisites in the previous semester for the courses you are taking.

Return the minimum number of semesters needed to take all courses. If there is no way to take all the courses, return `-1`.
"""
from typing import List
from collections import defaultdict, deque

class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        
        maxdepth = 0

        dependencies = defaultdict(list)  # [1 <- 0]
        for ai, bi in relations:
            dependencies[ai].append(bi)

        # for each target, searching for prerequisites
        def findCycles(target, checked_targets, whitelist, depth):
            nonlocal maxdepth

            if target in whitelist:
                return False
            # target = 1
            # target = 0
            for prereq in dependencies[target]:
                # prereq = 0
                if prereq in checked_targets:
                    return True
                
                checked_targets.add(prereq)
                if findCycles(prereq, checked_targets, whitelist, depth + 1):
                    return True
                checked_targets.remove(prereq)
            whitelist.add(target)

            maxdepth = max(maxdepth, depth)
            return False
            
        whitelist = set()
        for c in range(n):
            if findCycles(c, set(), whitelist, 0):
                return -1
        return maxdepth + 1


testCases = [
    (3, [[1, 0], [2, 1], [0, 2]], -1),
    (3, [[0, 1], [1, 2]], 3),
    (4, [[1, 3], [2, 1], [3, 2], [1, 0]], -1),
    (4, [[1, 3], [2, 3], [1, 2], [0, 2], [0, 1]], 4),
]


if __name__ == '__main__':
    solution = Solution()
    for numCourses, relations, expect in testCases:
        actual = solution.minimumSemesters(numCourses, relations)
        if actual != expect:
            print("---------------------------------------------")
            print(f"expect: {numCourses}, {relations} => {expect}")
            print(f"actual: {numCourses}, {relations} => {actual}")