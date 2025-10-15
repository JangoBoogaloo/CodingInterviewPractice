# https://leetcode.com/problems/course-schedule/description/
"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1.

You are given an array `prerequisites` where `prerequisites[i] = [ai, bi]`
* indicates that you must take course `bi` first if you want to take course `ai`.

For example, the pair `[0, 1]`, indicates that to take course `0` you have to first take course `1`.
Return true if you can finish all courses. Otherwise, return false.
"""
from typing import List


class SolutionDFS:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        return False


class SolutionBFS:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        return False


testCases = [
    (3, [[0, 1], [1, 2], [2, 0]], False),
    (3, [[1, 0], [2, 1]], True),
    (4, [[1, 3], [2, 1], [3, 2], [1, 0]], False),
    (4, [[3, 1], [3, 2], [2, 1], [2, 0], [1, 0]], True),
]

if __name__ == '__main__':
    solution = SolutionDFS()
    for numCourses, prerequisites, expect in testCases:
        actual =  solution.canFinish(numCourses, prerequisites)
        if actual != expect:
            print("---------------------------------------------")
            print(f"expect: {numCourses}, {prerequisites} => {expect}")
            print(f"actual: {numCourses}, {prerequisites} => {actual}")

