from typing import List
class Solution:

    def buildings_with_ocean_view(self, heights: List):
        
        stack = []

        for index, height in enumerate(heights):

            while stack and heights[stack[-1]] <= height:
                stack.pop()

            stack.append(index)

        return stack
                

