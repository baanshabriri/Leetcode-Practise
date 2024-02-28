#
# @lc app=leetcode id=75 lang=python3
#
# [75] Sort Colors
#

# @lc code=start
from typing import List
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        left = 0
        right = len(nums) - 1
        i = 0
        while i <= right:        
            if nums[i] == 2:
                nums[i], nums[right] = nums[right], nums[i]
                right -= 1
                continue

            if nums[i] == 0:
                nums[i], nums[left] = nums[left], nums[i]
                left += 1

            i += 1

        print(nums)

x = Solution()
x.sortColors([2,0,2,1,1,0])

# @lc code=end

