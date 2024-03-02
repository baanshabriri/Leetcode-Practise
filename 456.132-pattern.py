#
# @lc app=leetcode id=456 lang=python3
#
# [456] 132 Pattern
#

# @lc code=start
from typing import List
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:

        minimums = [0] * len(nums)                    
        stack = []

        for i, num in enumerate(nums):
            if i == 0:
                minimums[i] = 0
            else:
                if nums[i] < nums[minimums[i - 1]]:
                    minimums[i] = i
                else:
                    minimums[i] = minimums[i - 1]

            while stack and nums[stack[-1]] <= num:
                stack.pop()

            # If there is a previous greater element, stack will not be empty
            if stack:
                # If the previous minimum for the previous greater element is less than the current number, then we return true
                if nums[minimums[stack[-1]]] < num:                    
                    return True

            stack.append(i)

        return False
                    

x = Solution()
x.find132pattern([1,2,3,4])



        
# @lc code=end

