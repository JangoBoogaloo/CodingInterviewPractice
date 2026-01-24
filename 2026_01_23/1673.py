"""
1673. Find the Most Competitive Subsequence

Given an integer array nums and a positive integer k, return the most competitive subsequence of nums of size k.

An array's subsequence is a resulting sequence obtained by erasing some (possibly zero) elements from the array.

We define that a subsequence a is more competitive than a subsequence b (of the same length) if in the first position where a and b differ,
subsequence a has a number less than the corresponding number in b.

For example, [1,3,4] is more competitive than [1,3,5] because the first position they differ is at the final number, and 4 is less than 5.

Example 1:

Input: nums = [3,5,2,6], k = 2
Output: [2,6]
Explanation: Among the set of every possible subsequence: {[3,5], [3,2], [3,6], [5,2], [5,6], [2,6]}, [2,6] is the most competitive.
Example 2:

Input: nums = [2,4,3,3,5,4,9,6], k = 4
Output: [2,3,3,4]

0, n-k

1. most significant, lead to from left to right
2. next num smaller, and have more thank k left 

[1,9,2,1,1,0] k=3 => 110

[9,1,2,1] k=3

[1,2,1,2,0] k=4

[1,2,3,0,9]


"""
from typing import List


class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:

        incStk = []
        n = len(nums)
        allowed_ops = n - k

        # [1,2,9,9,9,9,9,9,9,9,9,0]
        for i in range(n):
            curr = nums[i]

            while incStk and incStk[-1] < curr and allowed_ops >= 0:
                incStk.pop()
                allowed_ops -= 1
    
            incStk.append(curr)

        return incStk[:k]