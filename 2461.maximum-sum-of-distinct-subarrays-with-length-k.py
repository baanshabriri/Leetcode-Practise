#
# @lc app=leetcode id=2461 lang=python3
#
# [2461] Maximum Sum of Distinct Subarrays With Length K
#

# @lc code=start
from typing import List
class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:        
        curr_sum = max_sum = 0
        elements = set()
        left = right = 0

        while right < len(nums):

            while nums[right] in elements:
                curr_sum -= nums[left]
                elements.remove(nums[left])
                left += 1

            curr_sum += nums[right]
            elements.add(nums[right])

            if right - left + 1 == k:
                max_sum = max(max_sum, curr_sum)
                curr_sum -= nums[left]
                elements.remove(nums[left])
                left += 1

            right += 1
        
        return max_sum



            




x = Solution()
print(x.maximumSubarraySum([2,4,4,4], 3))        
# @lc code=end

