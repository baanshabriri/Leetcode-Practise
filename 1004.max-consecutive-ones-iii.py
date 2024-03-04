#
# @lc app=leetcode id=1004 lang=python3
#
# [1004] Max Consecutive Ones III
#

# @lc code=start
from typing import List
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:

        i = j = 0
        count_0 = 0
        
        while j < len(nums):
            count_0 += 1 if nums[j] == 0 else 0
            if count_0 > k:
                count_0 -= 1 if nums[i] == 0 else 0
                i += 1

            j += 1

        return j - i

        
# @lc code=end

