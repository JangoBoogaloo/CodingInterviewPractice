# https://leetcode.com/problems/course-schedule-ii/
"""
Return the ordering of courses you should take to finish all courses.
If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.
"""
from typing import List


class SolutionDFS:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        return []


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