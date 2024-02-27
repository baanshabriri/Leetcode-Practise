#
# @lc app=leetcode id=1498 lang=python3
#
# [1498] Number of Subsequences That Satisfy the Given Sum Condition
#

# @lc code=start
from typing import List
class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        left = 0
        right = len(nums) - 1
        mod = 10 ** 9 + 7 
        count = 0
        while left <= right:
            if nums[left] + nums[right] > target:
                right -= 1
            else:
                # count += (2 ** (right - left)) % mod
                count += pow(2, right - left, mod=mod)
                left += 1
        return count % mod
                            

# @lc code=end

