"""
11. Container With Most Water

You are given an integer array height of length n. 
There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Example 1:

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: 
* The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. 
* In this case, the max area of water (blue section) the container can contain is 49.

  | 
|*|
|*|*| 
|*|*|*|
-----
[3,0,10,0,2,0,1]

[3,3] => 3
[3,0,3] => 6


[1,8,6,2,5,4,8,3,7]

1,8 -> 1*1
1,8,6 -> 6, 1*2
1,8,6,2 -> 2, 2*2, 1*3

1, min(any 2 wall heights) * distance btw two walls

"""
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:

        l, r = 0, len(height) - 1
        res = 0

        while l < r:
            
            dist = r - l
            #[1,8,6,3,7]    7*3
            # 1, 7   dist = 4 area = 4
            #    8,7 dist = 3 area = 21
            #    8,3 dist = 2 area = 6
            #    
            l_height, r_height = height[l], height[r]

            if l_height > r_height:
                res = max(res, dist * r_height)
                r -= 1
            elif l_height <= r_height:
                res = max(res, dist * l_height)
                l += 1
            
        return res
    










