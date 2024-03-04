#
# @lc app=leetcode id=1493 lang=python3
#
# [1493] Longest Subarray of 1's After Deleting One Element
#

# @lc code=start
from typing import List
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        
        i, j = 0, 0
        count_0 = 0
        max_len = 0
        
        while j < len(nums):
            count_0 += 1 if nums[j] == 0 else 0
            if count_0 > 1:
                count_0 -= 1 if nums[i] == 0 else 0
                i += 1
            j += 1

        return j - i - 1


x = Solution()
print(x.longestSubarray([0,1,1,1,0,1,1,0,1]))



# @lc code=end

