#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#

# @lc code=start
from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        water = 0

        for index, h in enumerate(height):

            while stack and height[stack[-1]] <= h:
                top = stack.pop()

                if stack:
                    ht = min(height[stack[-1]], h) - height[top]
                    width = index - (stack[-1] + 1)

                    water += ht * width

            stack.append(index)

        return water
    
x = Solution()
x.trap([0,1,0,2,1,0,1,3,2,1,2,1])
# @lc code=end
                    

