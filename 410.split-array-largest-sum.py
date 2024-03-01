#
# @lc app=leetcode id=410 lang=python3
#
# [410] Split Array Largest Sum
#

# @lc code=start
from typing import List
class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:

        def feasible(threshold):
            total = 0
            count = 1
            for num in nums:
                total += num
                if total > threshold:
                    total = num
                    count += 1
                    if count > k:
                        return False
            return True
        
        left, right = max(nums), sum(nums)

        while left < right:
            mid = left + (right - left) // 2

            if feasible(mid):
                right = mid
            else:
                left = mid + 1

        return left
        

x = Solution()
print(x.splitArray([7,2,5,10,8], 2))
# @lc code=end

