#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start
from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        i = 0
        result = set()        
        nums.sort()
        arr_len = len(nums)
        while i <  arr_len - 1:
            target = -nums[i]
            j = i + 1
            k = arr_len - 1

            while j < k:
                if nums[j] + nums[k] == target:
                    result.add((nums[i], nums[j], nums[k]))
                    j += 1
                    k -= 1

                if nums[j] + nums[k] > target:
                    k -= 1

                if nums[j] + nums[k] < target:
                    j += 1
            i += 1

        return result
    
        
# @lc code=end

