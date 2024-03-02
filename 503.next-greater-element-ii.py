#
# @lc app=leetcode id=503 lang=python3
#
# [503] Next Greater Element II
#

# @lc code=start
from typing import List
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:

        answer = [-1] * len(nums)
        stack = []

        for i in range(2):
            for index, num in enumerate(nums):

                while stack and nums[stack[-1]] < num:
                    top = stack.pop()
                    answer[top] = nums[index]
                
                stack.append(index)
        
        return answer


x = Solution()
x.nextGreaterElements([1,2,1])
        
# @lc code=end

