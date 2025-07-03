# https://leetcode.com/problems/product-of-array-except-self/description/
"""
Given an integer array `nums`, return an array `answer` such that `answer[i]` is equal to the product of all the elements of `nums` except `nums[i]`.

The product of any prefix or suffix of `nums` is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.


Constraints:

* 2 <= nums.length <= 10^5
* -30 <= nums[i] <= 30
* The input is generated such that `answer[i]` is guaranteed to fit in a 32-bit integer.

Follow up: Can you solve the problem in `O(1)` extra space complexity? (The output array does not count as extra space for space complexity analysis.)

Example 1:                     # n = 4, res = [0..5]
                               # 0     1      2               3                   4        5 
Input: nums = [1,2,3,4]   arrl # 1     1      2               6                  24        1
Output: [24,12,8,6]       arrr # 1     24     24              12                  4        1
Example 2:                     #   arr[1]  arr[1]*arr[3]  arr[2]*arr[4]   

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

# nums[i-1]  nums[i]  nums[...]
"""
from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = []
        preProd = 1
        for num in nums:
            answer.append(preProd)
            preProd *= num
        i = len(nums) - 1

        postProd = 1

        for num in reversed(nums):
            answer[i] = postProd
            postProd *= num

        return answer