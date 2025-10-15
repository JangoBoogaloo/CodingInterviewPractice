# https://leetcode.com/problems/parallel-courses/description/
"""
You are given an integer `n`, which indicates that there are `n` courses labeled from `1` to `n`.
You are also given an array `relations` where `relations[i] = [prevCoursei, nextCoursei]`,
representing a prerequisite relationship between course `prevCoursei` and course `nextCoursei`: course `prevCoursei` has to be taken before course `nextCoursei`.

In one semester, you can take any number of courses as long as you have taken all the prerequisites in the previous semester for the courses you are taking.

Return the minimum number of semesters needed to take all courses. If there is no way to take all the courses, return `-1`.
"""
from typing import List


class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        return -1


testCases = [
    (3, [[1, 0], [2, 1], [0, 2]], -1),
    (3, [[0, 1], [1, 2]], 3),
    (4, [[1, 3], [2, 1], [3, 2], [1, 0]], -1),
    (4, [[1, 3], [2, 3], [1, 2], [0, 2], [0, 1]], 4),
]


if __name__ == '__main__':
    solution = Solution()
    for numCourses, prerequisites, expect in testCases:
        assert solution.minimumSemesters(numCourses, prerequisites) == expect