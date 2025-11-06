# https://leetcode.com/problems/max-chunks-to-make-sorted/
"""
You are given an integer array arr of length n that represents a "permutation" of the integers in the range [0, n - 1].

We split arr into some number of chunks (i.e., partitions), and individually sort each chunk. After concatenating them, the result should equal the sorted array.

Return the largest number of chunks we can make to sort the array.

Example 1:

Input: arr = [4,3,2,1,0]
Output: 1
Explanation:
Splitting into two or more chunks will not return the required result.
For example, splitting into [4, 3], [2, 1, 0] will result in [3, 4, 0, 1, 2], which isn't sorted.

Example 2:

Input: arr = [1,0,2,3,4]
Output: 4
Explanation:
We can split into two chunks, such as [1, 0], [2, 3, 4].
However, splitting into [1, 0], [2], [3], [4] is the highest number of chunks possible.

             [0,1,2,3,4]
Input: arr = [1,2,3,0,4]
Output: 2
Explanation:
[1,2,3,0][4]
 1 1 1 3

"""
from typing import List


class Solution1:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        idx, _max, res = 0, 0, 0
        while idx < len(arr): # [1,3,0,2,4] 
            _max = max(_max, arr[idx])
            if _max == idx: # kadane's algorithm 
                res += 1
            idx += 1
        return res


class Solution2:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        # [4,3,2,1,0]
        count, idx, curr_sum, res =  0, 0, 0, 0
        expectedSum = 0
        while idx < len(arr):
            expectedSum += idx
            curr_sum += arr[idx]
            if curr_sum == expectedSum:
                res += 1
            idx += 1 
        return res


class Solution3:
    def maxChunksToSorted(self, arr: List[int]) -> int:

        # [0, 1, 2] => 3
        
        # [2, 1, 0] => 1

        # [2,4,1,2,5,6,1] 
        
        # [1]
        
        """
            [1, 2, 2, 4, 5]

            [2, 4, 1, 2, 5]
            
            decStk = [2, ], [4, ], [4, 1], [4, 2], [5]
            incStk = [2, ], [2, 4], [1, ], [1, 2], [1, 2, 5]

        """

        incStk = []   # 0 -> 1 -> 2
        for idx in range(len(arr)):                     # 1,  3,  0,   2,    4
            curr_max = arr[idx]
            while incStk and arr[idx] < incStk[-1]:     #       
                prevMax = incStk.pop()
                curr_max = max(curr_max, prevMax)
                
            incStk.append(curr_max)                   #1, 1, 3  0   0,2    0,2,4   get 3 expect 2
            
        return len(incStk)