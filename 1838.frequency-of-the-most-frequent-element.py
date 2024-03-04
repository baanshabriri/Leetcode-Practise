#
# @lc app=leetcode id=1838 lang=python3
#
# [1838] Frequency of the Most Frequent Element
#

# @lc code=start
from typing import List
class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        
        nums.sort()
        i = j = 0
        sum = 0
        while j < len(nums):
            sum += nums[j]
            if (j - i + 1) * nums[j] - sum > k:
                sum -= nums[i]
                i += 1
            j += 1
        return j - i

x = Solution()
x.maxFrequency([1,2,4], 5)
# @lc code=end

