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
        assert solution.canFinish(numCourses, prerequisites) == expect

