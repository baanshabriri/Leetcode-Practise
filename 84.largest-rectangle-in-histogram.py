#
# @lc app=leetcode id=84 lang=python3
#
# [84] Largest Rectangle in Histogram
#

# @lc code=start
from typing import List
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        n = len(heights)
        prev_smaller = [-1] * n
        next_smaller = [n] * n
        for index, height in enumerate(heights):

            while stack and heights[stack[-1]] > height:
                top = stack.pop()
                next_smaller[top] = index

            if stack:
                prev_smaller[index] = stack[-1]

            stack.append(index)

        max_area = 0
        for index, height in enumerate(heights):
            max_width = next_smaller[index] - prev_smaller[index] - 1
            max_area = max(max_area, height * max_width)

        return max_area
    

        maxArea = 0
        stack = []

        # Iterate through each index and height in the heights array
        for index, height in enumerate(heights):
            start = index

            # Check if the stack is not empty and the height at the top of the stack is greater than the current height
            while start and stack[-1][1] > height:
                i, h = stack.pop()
                # Calculate the area for the popped element and update maxArea if needed
                maxArea = max(maxArea, (index - i) * h)
                start = i

            # Push the current index and height onto the stack
            stack.append((start, height))

        # Process any remaining elements in the stack
        for index, height in stack:
            maxArea = max(maxArea, (len(heights) - index) * height)

        return maxArea


# @lc code=end

