#
# @lc app=leetcode id=739 lang=python3
#
# [739] Daily Temperatures
#

# @lc code=start
from typing import List
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        n = len(temperatures)
        answer = [0] * n
        stack = []

        for i, temperature in enumerate(temperatures):

            while stack and temperatures[stack[-1]] < temperature:
                index = stack.pop()
                answer[index] = i - index

            stack.append(i)

        return answer



        # Time Limit Exceeded
        # n = len(temperatures)
        # answer = [0] * n

        # left = right = 0

        # while right < n:

        #     curr_temp = temperatures[left]

        #     if curr_temp < temperatures[right]:
                
        #         answer[left] = right - left
        #         left += 1
        #         right = left

        #     else:
        #         if right == n - 1:
        #             left += 1
        #             right = left                
        #         else:                
        #             right += 1


        # return answer
            
        
# @lc code=end

