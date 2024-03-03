#
# @lc app=leetcode id=1944 lang=python3
#
# [1944] Number of Visible People in a Queue
#

# @lc code=start
from typing import List
class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:

        answer = [0] * len(heights)
        stack = []

        for index, height in enumerate(heights):

            # next person with greater or equal height for index stack top
            while stack and heights[stack[-1]] <= height:
                top = stack.pop()
                answer[top] += 1

            # previous person with strictly greater height than person at current index
            if stack:
                answer[stack[-1]] += 1

            stack.append(index)
    
        return answer
    

x = Solution()
x.canSeePersonsCount([10,6,8,5,11,9])

        
# @lc code=end

