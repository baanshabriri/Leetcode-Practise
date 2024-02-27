#
# @lc app=leetcode id=713 lang=python3
#
# [713] Subarray Product Less Than K
#

# @lc code=start

from typing import List
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:

        left, count, product = 0, 0, 1
        
        for right in range(len(nums)):
            product *= nums[right]
            while product >= k and left <= right:
                product /= nums[left]
                left += 1


            count += right - left + 1
        return count


    

x = Solution()
print(x.numSubarrayProductLessThanK([10,5,2,6], 100))


# @lc code=end

